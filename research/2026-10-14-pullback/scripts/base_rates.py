import pandas as pd, numpy as np, json, sys
sys.path.insert(0, sys.argv[1] + "/scripts")
D = sys.argv[1] + "/data"
def load(s): return pd.read_csv(f"{D}/{s.replace('^','_')}.csv", parse_dates=["date"]).set_index("date")

def episodes(df, min_depth, start_date):
    x = df.copy(); x["sma200"] = x.close.rolling(200).mean(); x["sma50"] = x.close.rolling(50).mean(); x["sma100"]=x.close.rolling(100).mean()
    c = x.close.values; lo = x.low.values; idx = x.index; n = len(x)
    out = []; peak = 0; i = 1
    while i < n:
        if c[i] >= c[peak]: peak = i; i += 1; continue
        j = i
        while j < n and c[j] < c[peak]: j += 1
        seg = slice(peak, j)
        t = peak + int(np.argmin(c[seg])); tl = peak + int(np.argmin(lo[seg]))
        dc = c[t]/c[peak]-1; dl = lo[tl]/c[peak]-1
        if dc <= -min_depth and idx[peak] >= pd.Timestamp(start_date):
            def rel(k, col): 
                v = x[col].iloc[k]; return None if np.isnan(v) else round((c[k]/v-1)*100,1)
            out.append(dict(peak=str(idx[peak].date()), peak_close=round(c[peak],2), trough=str(idx[t].date()), trough_close=round(c[t],2),
                depth_close=round(dc*100,1), depth_raw=float(dc*100), depth_low=round(dl*100,1), days_to_trough=int(t-peak), cal_days_to_trough=int((idx[t]-idx[peak]).days),
                days_to_recover=(int(j-t) if j<n else None), ongoing=bool(j>=n),
                above200_at_peak=(None if np.isnan(x.sma200.iloc[peak]) else bool(c[peak]>x.sma200.iloc[peak])),
                trough_vs_sma50=rel(t,"sma50"), trough_vs_sma100=rel(t,"sma100"), trough_vs_sma200=rel(t,"sma200"),
                closed_below_200d_during=bool((x.close.iloc[peak:j] < x.sma200.iloc[peak:j]).any())))
        if j >= n: break
        peak = j; i = j + 1
    return out

def conditional(df, start_date, thresholds):
    """For every drawdown episode (min 3%), given DD reached threshold T (close basis), distribution of final depth and extra days to trough."""
    eps = episodes(df, 0.03, start_date)
    res = {}
    x = df.close
    for T in thresholds:
        rows = []
        for e in eps:
            if e["depth_raw"] <= -T:
                seg = x.loc[e["peak"]:e["trough"]]
                pk = x.loc[e["peak"]]; first_hit = seg[seg/pk-1 <= -T/100 + 1e-9].index[0]
                rows.append(dict(peak=e["peak"], final_depth=e["depth_close"], extra_pct=round((e["trough_close"]/x.loc[first_hit]-1)*100,1),
                                 extra_days=int(len(x.loc[first_hit:e["trough"]])-1), ongoing=e["ongoing"]))
        done = [r for r in rows if not r["ongoing"]]
        fd = [r["final_depth"] for r in done]
        res[f"reached_{T}pct"] = dict(n_total=len(rows), n_completed=len(done),
            median_final_depth=(float(np.median(fd)) if fd else None),
            pct_ending_shallower_than=( {f"{k}%": round(float(np.mean([f > -k for f in fd]))*100,0) for k in [T+2.5, T+5, T+10, T+15]} if fd else None),
            median_extra_downside_from_hit=(float(np.median([r["extra_pct"] for r in done])) if done else None),
            median_extra_days=(float(np.median([r["extra_days"] for r in done])) if done else None),
            cases=rows)
    return eps, res

SYMS = {"NVDA":[5,7.5,10,15], "SOXX":[5,10,15,20], "SMH":[5,10,15,20], "^SOX":[5,10,15,20], "^GSPC":[2,3,5,7.5,10], "QQQ":[3,5,7.5,10], "XLK":[3,5,7.5,10], "RSP":[3,5,7.5,10]}
OUT = {}
for s, th in SYMS.items():
    df = load(s)
    big = {"NVDA":0.08, "SOXX":0.08, "SMH":0.08, "^SOX":0.08}.get(s, 0.04)
    eps3 = episodes(df, big, "2023-10-14")
    _, cond = conditional(df, "2023-10-14", th)
    _, cond5 = conditional(df, "2021-10-14", th)
    depths = [e["depth_close"] for e in eps3 if not e["ongoing"]]
    up = [e for e in eps3 if not e["ongoing"] and e["above200_at_peak"]]
    OUT[s] = dict(threshold_for_list=big*100, episodes_3y=eps3,
        summary_3y=dict(n=len(depths), median_depth=float(np.median(depths)) if depths else None, mean_depth=float(np.mean(depths)) if depths else None,
            min_depth=min(depths) if depths else None, max_depth=max(depths) if depths else None,
            median_days_to_trough=float(np.median([e["days_to_trough"] for e in eps3 if not e["ongoing"]])) if depths else None,
            median_days_to_recover=float(np.median([e["days_to_recover"] for e in eps3 if e["days_to_recover"]])) if depths else None,
            uptrend_only_n=len(up), uptrend_only_median_depth=float(np.median([e["depth_close"] for e in up])) if up else None,
            pct_breaking_200d=round(np.mean([e["closed_below_200d_during"] for e in eps3 if not e["ongoing"]])*100,0) if depths else None),
        conditional_3y=cond, conditional_5y={k:{kk:vv for kk,vv in v.items() if kk!="cases"} for k,v in cond5.items()})
json.dump(OUT, open(sys.argv[1] + "/data/base_rates.json","w"), indent=1, default=str)
for s in OUT:
    S = OUT[s]["summary_3y"]; print(s, S)
    for e in OUT[s]["episodes_3y"]: print("   ", e["peak"], "->", e["trough"], e["depth_close"], "low", e["depth_low"], "d", e["days_to_trough"], "rec", e["days_to_recover"], "200d broken" if e["closed_below_200d_during"] else "", "ONGOING" if e["ongoing"] else "", "vs50", e["trough_vs_sma50"], "vs100", e["trough_vs_sma100"], "vs200", e["trough_vs_sma200"])
    for k, v in OUT[s]["conditional_3y"].items():
        print("   COND3y", k, {kk: vv for kk, vv in v.items() if kk != "cases"})
