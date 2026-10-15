import pandas as pd, numpy as np, json, sys, os
D = sys.argv[1]
OUT = sys.argv[2]
syms = sys.argv[3].split(",")

def load(sym):
    df = pd.read_csv(os.path.join(D, sym.replace("^","_") + ".csv"), parse_dates=["date"]).set_index("date")
    return df

def rsi(c, n=14):
    d = c.diff(); up = d.clip(lower=0).ewm(alpha=1/n, adjust=False).mean(); dn = (-d.clip(upper=0)).ewm(alpha=1/n, adjust=False).mean()
    return 100 - 100/(1+up/dn)

def atr(df, n=14):
    tr = pd.concat([df.high-df.low, (df.high-df.close.shift()).abs(), (df.low-df.close.shift()).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1/n, adjust=False).mean()

def vol_profile(df, days=126, bins=40):
    x = df.iloc[-days:]
    tp = (x.high + x.low + x.close)/3
    hist, edges = np.histogram(tp, bins=bins, weights=x.volume.fillna(0))
    mids = (edges[:-1]+edges[1:])/2
    order = np.argsort(hist)[::-1]
    poc = mids[order[0]]
    top = sorted([(round(float(mids[i]),2), round(float(hist[i]/hist.sum()*100),1)) for i in order[:8]], key=lambda t: -t[0])
    return {"window_days": days, "poc": round(float(poc),2), "top_nodes_price_pctvol": top}

def unfilled_gaps(df, lookback=180):
    x = df.iloc[-lookback:]
    gaps = []
    for i in range(1, len(x)):
        prev, cur = x.iloc[i-1], x.iloc[i]
        if cur.low > prev.high:  # gap up
            lo, hi = prev.high, cur.low
            after = x.iloc[i+1:]
            filled = (after.low <= lo).any() if len(after) else False
            if not filled:
                partial_min = after.low.min() if len(after) else np.nan
                gaps.append({"date": str(x.index[i].date()), "type": "up", "zone": [round(lo,2), round(hi,2)], "lowest_since": None if np.isnan(partial_min) else round(float(partial_min),2)})
        elif cur.high < prev.low:
            lo, hi = cur.high, prev.low
            after = x.iloc[i+1:]
            filled = (after.high >= hi).any() if len(after) else False
            if not filled:
                gaps.append({"date": str(x.index[i].date()), "type": "down", "zone": [round(lo,2), round(hi,2)]})
    return gaps

def swing_lows(df, lookback=260, w=5):
    x = df.iloc[-lookback:]
    out = []
    for i in range(w, len(x)-w):
        if x.low.iloc[i] == x.low.iloc[i-w:i+w+1].min():
            out.append((str(x.index[i].date()), round(float(x.low.iloc[i]),2)))
    return out[-12:]

def swing_highs(df, lookback=260, w=5):
    x = df.iloc[-lookback:]
    out = []
    for i in range(w, len(x)-w):
        if x.high.iloc[i] == x.high.iloc[i-w:i+w+1].max():
            out.append((str(x.index[i].date()), round(float(x.high.iloc[i]),2)))
    return out[-12:]

def anchored_vwap(df, start):
    x = df.loc[start:]
    tp = (x.high+x.low+x.close)/3
    return round(float((tp*x.volume).sum()/x.volume.sum()),2) if x.volume.sum() > 0 else None

def episodes(df, col="close", min_depth=0.05, years=3.0, use_low=False):
    """Peak-to-trough drawdown episodes (close-based). An episode runs from a closing high until the next new closing high."""
    x = df.copy()
    x["sma200"] = x.close.rolling(200).mean()
    x["sma50"] = x.close.rolling(50).mean()
    start = x.index[-1] - pd.Timedelta(days=int(365*years))
    c = x.close.values; lo = x.low.values; idx = x.index
    peak_i = 0; eps = []; i = 1
    n = len(x)
    while i < n:
        if c[i] >= c[peak_i]:
            peak_i = i; i += 1; continue
        # in drawdown from peak_i; find end (next new high) or end of data
        j = i
        while j < n and c[j] < c[peak_i]: j += 1
        seg = slice(peak_i, j)
        tr_i = peak_i + int(np.argmin(c[seg]))
        depth_c = c[tr_i]/c[peak_i]-1
        tr_low_i = peak_i + int(np.argmin(lo[seg]))
        depth_l = lo[tr_low_i]/c[peak_i]-1
        if depth_c <= -min_depth and idx[peak_i] >= start:
            eps.append({
                "peak_date": str(idx[peak_i].date()), "peak_close": round(float(c[peak_i]),2),
                "trough_date": str(idx[tr_i].date()), "trough_close": round(float(c[tr_i]),2),
                "depth_close_pct": round(depth_c*100,1), "depth_intraday_low_pct": round(depth_l*100,1),
                "days_to_trough": int(tr_i-peak_i),
                "days_trough_to_recover": (int(j-tr_i) if j < n else None),
                "recovered": bool(j < n),
                "above_200d_at_peak": bool(c[peak_i] > x.sma200.iloc[peak_i]) if not np.isnan(x.sma200.iloc[peak_i]) else None,
                "trough_vs_50d_pct": round((c[tr_i]/x.sma50.iloc[tr_i]-1)*100,1) if not np.isnan(x.sma50.iloc[tr_i]) else None,
                "trough_vs_200d_pct": round((c[tr_i]/x.sma200.iloc[tr_i]-1)*100,1) if not np.isnan(x.sma200.iloc[tr_i]) else None,
                "ongoing": bool(j >= n),
            })
        peak_i = j if j < n else peak_i
        i = j + 1 if j < n else n
    return eps

res = {}
for sym in syms:
    df = load(sym)
    c = df.close
    last = df.iloc[-1]
    smas = {f"sma{n}": round(float(c.rolling(n).mean().iloc[-1]),2) for n in (10,20,50,100,200)}
    emas = {f"ema{n}": round(float(c.ewm(span=n, adjust=False).mean().iloc[-1]),2) for n in (8,21,50)}
    slope = {f"sma{n}_slope_20d_pct": round(float((c.rolling(n).mean().iloc[-1]/c.rolling(n).mean().iloc[-21]-1)*100),2) for n in (50,200)}
    hi_close = c.max(); hi_close_d = c.idxmax(); hi_intra = df.high.max(); hi_intra_d = df.high.idxmax()
    hi52 = df.high.iloc[-252:].max(); lo52 = df.low.iloc[-252:].min()
    a = atr(df).iloc[-1]
    r = {
        "last_date": str(df.index[-1].date()), "last_close": round(float(last.close),2),
        "last_ohlc": [round(float(last.open),2), round(float(last.high),2), round(float(last.low),2), round(float(last.close),2)],
        "ath_close": round(float(hi_close),2), "ath_close_date": str(hi_close_d.date()),
        "ath_intraday": round(float(hi_intra),2), "ath_intraday_date": str(hi_intra_d.date()),
        "dd_from_close_high_pct": round(float((last.close/hi_close-1)*100),2),
        "dd_from_intraday_high_pct": round(float((last.close/hi_intra-1)*100),2),
        "high_52w": round(float(hi52),2), "low_52w": round(float(lo52),2),
        **smas, **emas, **slope,
        "dist_pct": {k: round(float((last.close/v-1)*100),2) for k, v in {**smas, **emas}.items()},
        "rsi14": round(float(rsi(c).iloc[-1]),1),
        "atr14": round(float(a),2), "atr14_pct": round(float(a/last.close*100),2),
        "vol_20d_avg": int(df.volume.iloc[-20:].mean()) if df.volume.iloc[-20:].sum() > 0 else None,
        "vol_last_vs_50d": round(float(df.volume.iloc[-1]/df.volume.iloc[-50:].mean()),2) if df.volume.iloc[-50:].sum() > 0 else None,
        "last_15_days": [[str(d.date()), round(float(o),2), round(float(h),2), round(float(l),2), round(float(cl),2), int(v) if not np.isnan(v) else None] for d, o, h, l, cl, v in zip(df.index[-15:], df.open[-15:], df.high[-15:], df.low[-15:], df.close[-15:], df.volume[-15:])],
        "swing_lows_1y": swing_lows(df), "swing_highs_1y": swing_highs(df),
        "unfilled_gaps_180d": unfilled_gaps(df),
        "realized_vol_20d_ann_pct": round(float(np.log(c).diff().iloc[-20:].std()*np.sqrt(252)*100),1),
        "returns_pct": {k: round(float((c.iloc[-1]/c.iloc[-n-1]-1)*100),2) for k, n in {"1w":5,"1m":21,"3m":63,"6m":126,"1y":252}.items()},
    }
    if df.volume.iloc[-126:].sum() > 0:
        r["volume_profile_6m"] = vol_profile(df, 126)
        r["volume_profile_3m"] = vol_profile(df, 63, 30)
    res[sym] = r
json.dump(res, open(OUT, "w"), indent=1, default=str)
print("ok", len(res))
