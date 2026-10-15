import sys, time, json, requests, pandas as pd, os
OUT = sys.argv[1]
syms = sys.argv[2].split(",")
rng = sys.argv[3] if len(sys.argv) > 3 else "5y"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
s = requests.Session(); s.headers["User-Agent"] = UA
fails = []
for sym in syms:
    for attempt in range(4):
        try:
            host = "query1" if attempt % 2 == 0 else "query2"
            r = s.get(f"https://{host}.finance.yahoo.com/v8/finance/chart/{sym}", params={"range": rng, "interval": "1d", "includeAdjustedClose": "true", "events": "div,splits"}, timeout=30)
            if r.status_code != 200:
                time.sleep(2 ** attempt); continue
            j = r.json()["chart"]["result"][0]
            q = j["indicators"]["quote"][0]
            df = pd.DataFrame({"date": pd.to_datetime(j["timestamp"], unit="s", utc=True).tz_convert("America/New_York").date,
                               "open": q["open"], "high": q["high"], "low": q["low"], "close": q["close"], "volume": q["volume"]})
            if "adjclose" in j["indicators"]:
                df["adjclose"] = j["indicators"]["adjclose"][0]["adjclose"]
            df = df.dropna(subset=["close"])
            df.to_csv(os.path.join(OUT, sym.replace("^", "_").replace("=", "_") + ".csv"), index=False)
            print(sym, len(df), df["date"].iloc[-1], round(df["close"].iloc[-1], 2))
            break
        except Exception as e:
            time.sleep(2 ** attempt)
    else:
        fails.append(sym); print("FAIL", sym)
    time.sleep(0.4)
print("FAILS:", fails)
