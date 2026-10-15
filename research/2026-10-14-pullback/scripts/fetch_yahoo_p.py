import sys, time, requests, pandas as pd, os
OUT=sys.argv[1]; syms=sys.argv[2].split(",")
s=requests.Session(); s.headers["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
for sym in syms:
    r=s.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}",params={"period1":0,"period2":int(time.time()),"interval":"1d","includeAdjustedClose":"true"},timeout=60)
    j=r.json()["chart"]["result"][0]; q=j["indicators"]["quote"][0]
    df=pd.DataFrame({"date":pd.to_datetime(j["timestamp"],unit="s",utc=True).tz_convert("America/New_York").date,"close":q["close"],"high":q["high"],"low":q["low"]})
    if "adjclose" in j["indicators"]: df["adjclose"]=j["indicators"]["adjclose"][0]["adjclose"]
    df=df.dropna(subset=["close"]); df.to_csv(os.path.join(OUT,sym.replace("^","_")+".csv"),index=False)
    print(sym,len(df),df.date.iloc[0],df.date.iloc[-1],round(df.close.iloc[-1],2)); time.sleep(0.5)
