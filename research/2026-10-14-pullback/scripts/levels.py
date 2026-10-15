import pandas as pd, numpy as np, json
def load(s): return pd.read_csv(f"data/{s.replace('^','_')}.csv", parse_dates=["date"]).set_index("date")
def avwap(df, start):
    x = df.loc[start:]; tp = (x.high+x.low+x.close)/3
    return round(float((tp*x.volume).sum()/x.volume.sum()),2)
out = {}
for s in ["NVDA","SOXX","SMH","QQQ","SPY","^GSPC","RSP","XLK","^SOX","^NDX"]:
    df = load(s); c = df.close
    r = {"last": round(float(c.iloc[-1]),2)}
    # prior closing high before the current high (for breakout levels)
    win = df.loc["2026-01-01":]
    r["closing_highs_2026_by_month"] = {str(k.date())[:7]: round(float(v),2) for k, v in win.close.resample("ME").max().items()}
    r["intraday_highs_2026_by_month"] = {str(k.date())[:7]: round(float(v),2) for k, v in win.high.resample("ME").max().items()}
    r["intraday_lows_2026_by_month"] = {str(k.date())[:7]: round(float(v),2) for k, v in win.low.resample("ME").min().items()}
    jl = df.loc["2026-07-15":"2026-08-15"]; jl_low = float(jl.low.min()); jl_d = jl.low.idxmin()
    rec = df.loc["2026-09-01":]; hi = float(rec.high.max()); hi_d = rec.high.idxmax()
    r["jul_aug_low"] = [str(jl_d.date()), round(jl_low,2)]
    r["recent_high_since_sep"] = [str(hi_d.date()), round(hi,2)]
    rng = hi - jl_low
    r["fib_retracements_of_julLow_to_recentHigh"] = {k: round(hi - rng*f, 2) for k, f in {"23.6": .236, "38.2": .382, "50": .5, "61.8": .618, "78.6": .786}.items()}
    if df.volume.sum() > 0:
        r["avwap"] = {"from_jul_aug_low": avwap(df, jl_d), "from_2026_03_30": avwap(df, "2026-03-30"), "from_ytd": avwap(df, "2026-01-02"), "from_recent_high": avwap(df, hi_d), "from_2025_04_08": avwap(df, "2025-04-08"), "from_sep_start": avwap(df, "2026-09-01")}
    # Aug-Sep range
    asr = df.loc["2026-08-01":"2026-09-24"]
    r["aug_to_sep24_range_close"] = [round(float(asr.close.min()),2), round(float(asr.close.max()),2)]
    r["aug_to_sep24_range_intraday"] = [round(float(asr.low.min()),2), round(float(asr.high.max()),2)]
    out[s] = r
json.dump(out, open("data/levels.json","w"), indent=1)
for s, r in out.items():
    print(s, r["last"], "JulLow", r["jul_aug_low"], "recentHi", r["recent_high_since_sep"], "fib", r["fib_retracements_of_julLow_to_recentHigh"], "avwap", r.get("avwap"), "AugSepRangeClose", r["aug_to_sep24_range_close"])
    print("   closing highs by month", r["closing_highs_2026_by_month"])
