import pandas as pd, numpy as np, glob, os, json
P = "data/spx"
closes, highs, lows = {}, {}, {}
for f in glob.glob(f"{P}/*.csv"):
    s = os.path.basename(f)[:-4]
    df = pd.read_csv(f, parse_dates=["date"]).set_index("date")
    closes[s] = df.close; highs[s] = df.high; lows[s] = df.low
C = pd.DataFrame(closes).sort_index(); H = pd.DataFrame(highs).sort_index(); L = pd.DataFrame(lows).sort_index()
C = C.loc[C.index >= C.index[-1] - pd.Timedelta(days=740)]
n_names = C.shape[1]
out = {"n_constituents_loaded": int(n_names), "caveat": "current constituents only (survivorship bias); Yahoo split-adjusted closes"}
def pct_above(n):
    ma = C.rolling(n, min_periods=n).mean()
    valid = ma.notna() & C.notna()
    return ((C > ma) & valid).sum(axis=1) / valid.sum(axis=1) * 100
ab = {n: pct_above(n) for n in (20, 50, 100, 200)}
hi52 = C.rolling(252, min_periods=200).max(); lo52 = C.rolling(252, min_periods=200).min()
nh = (C >= hi52).sum(axis=1); nl = (C <= lo52).sum(axis=1)
ret = C.pct_change()
adv = (ret > 0).sum(axis=1); dec = (ret < 0).sum(axis=1)
adline = (adv - dec).cumsum()
off_hi = (C / hi52 - 1)
pct_10_off = (off_hi <= -0.10).sum(axis=1) / off_hi.notna().sum(axis=1) * 100
pct_20_off = (off_hi <= -0.20).sum(axis=1) / off_hi.notna().sum(axis=1) * 100
median_dd = off_hi.median(axis=1) * 100
ts = pd.DataFrame({"pct_above_20d": ab[20], "pct_above_50d": ab[50], "pct_above_100d": ab[100], "pct_above_200d": ab[200], "new_52w_highs": nh, "new_52w_lows": nl, "adv": adv, "dec": dec, "ad_line": adline, "pct_10pct_below_52wH": pct_10_off, "pct_20pct_below_52wH": pct_20_off, "median_pct_below_52wH": median_dd}).round(1)
ts = ts.loc[ts.index >= "2025-03-01"]
ts.to_csv("data/breadth_timeseries.csv")
last = ts.iloc[-1]
out["latest"] = {k: (float(v) if not pd.isna(v) else None) for k, v in last.items()}; out["latest_date"] = str(ts.index[-1].date())
out["last_25_days"] = ts.iloc[-25:].reset_index().astype(str).values.tolist(); out["columns"] = ["date"] + list(ts.columns)
ref = {}
for d in ["2025-04-08", "2025-11-20", "2026-03-30", "2026-06-10", "2026-07-29", "2026-08-14", "2026-09-16", "2026-10-06"]:
    dd = ts.index[ts.index.get_indexer([pd.Timestamp(d)], method="nearest")[0]]
    ref[d] = {k: float(v) for k, v in ts.loc[dd].items()}
out["at_reference_dates"] = ref
# AD line vs SPX: highs
spx = pd.read_csv("data/_GSPC.csv", parse_dates=["date"]).set_index("date").close
adl = ts.ad_line
out["ad_line_high_date"] = str(adl.idxmax().date()); out["ad_line_last_vs_high"] = float(adl.iloc[-1] - adl.max())
out["spx_high_date_since_2025_03"] = str(spx.loc["2025-03-01":].idxmax().date())
# sector breadth (pct above 50d / 200d by GICS sector)
cons = pd.read_csv("data/spx_constituents.csv"); cons["sym"] = cons.Symbol.str.replace(".", "-", regex=False)
sec = cons.set_index("sym")["GICS Sector"]
ma50 = C.rolling(50).mean().iloc[-1]; ma200 = C.rolling(200).mean().iloc[-1]; lastc = C.iloc[-1]
sb = {}
for s_, g in sec.groupby(sec):
    names = [x for x in g.index if x in C.columns]
    sb[s_] = {"n": len(names), "pct_above_50d": round(float((lastc[names] > ma50[names]).mean()*100),1), "pct_above_200d": round(float((lastc[names] > ma200[names]).mean()*100),1),
              "median_1w_ret": round(float(((C[names].iloc[-1]/C[names].iloc[-6])-1).median()*100),2), "median_1m_ret": round(float(((C[names].iloc[-1]/C[names].iloc[-22])-1).median()*100),2)}
out["sector_breadth"] = sb
# Oct 8 and Oct 14 day breadth
for d in ["2026-10-08", "2026-10-09", "2026-10-12", "2026-10-13", "2026-10-14"]:
    if pd.Timestamp(d) in ts.index:
        out[f"day_{d}"] = {"adv": int(ts.loc[d, "adv"]), "dec": int(ts.loc[d, "dec"])}
json.dump(out, open("data/breadth.json", "w"), indent=1, default=str)
print(json.dumps({k: out[k] for k in ["n_constituents_loaded","latest_date","latest","ad_line_high_date","ad_line_last_vs_high","spx_high_date_since_2025_03"]}, indent=1))
print(json.dumps(out["at_reference_dates"], indent=0))
print(json.dumps(out["sector_breadth"], indent=0))
print({k: v for k, v in out.items() if k.startswith("day_")})
print(ts.iloc[-12:].to_string())
