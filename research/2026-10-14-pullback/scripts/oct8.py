import pandas as pd, sys
syms=["NVDA","AMD","AVGO","ORCL","CRWV","MSFT","TSM","MU","SOXX","SMH","QQQ","_GSPC","RSP","_NDX","XLK","_SOX","META","GOOGL","AMZN","AAPL","NBIS","PLTR","CEG","VST","ANET","DELL","SMCI","VRT","ARM","COHR","LITE","CRDO","ALAB","SNDK","WDC","STX","ASML","AMAT","LRCX","KLAC","INTC","MRVL","IWM","TSLA","CIEN","_VIX","_TNX"]
rows=[]
for s in syms:
    df=pd.read_csv(f"data/{s}.csv",parse_dates=["date"]).set_index("date")
    df["ret"]=df.close.pct_change()*100
    df["absret"]=df.ret.abs()
    df["avgabs20"]=df.absret.shift(1).rolling(20).mean()
    d=df.loc["2026-10-01":"2026-10-14"]
    r={"sym":s}
    for dt in d.index:
        r[dt.strftime("%m-%d")]=round(d.loc[dt,"ret"],2)
    o8=df.loc["2026-10-08"]
    prev=df.loc["2026-10-07"]
    r["gap8"]=round((o8.open/prev.close-1)*100,2)
    r["low8_vs_prev"]=round((o8.low/prev.close-1)*100,2)
    r["avgabs20@8"]=round(o8.avgabs20,2)
    r["z8"]=round(o8.ret/o8.avgabs20,2)
    hi=df.loc[:"2026-10-14","close"].max(); hidt=df.loc[:"2026-10-14","close"].idxmax()
    r["from_ATHclose"]=round((df.loc["2026-10-14","close"]/hi-1)*100,2); r["ATHdate"]=hidt.strftime("%Y-%m-%d")
    r["oct7_14"]=round((df.loc["2026-10-14","close"]/df.loc["2026-10-07","close"]-1)*100,2)
    r["vol8_vs20"]=round(o8.volume/df.volume.shift(1).rolling(20).mean().loc["2026-10-08"],2) if o8.volume>0 else None
    rows.append(r)
out=pd.DataFrame(rows).set_index("sym")
pd.set_option("display.width",250); pd.set_option("display.max_columns",40)
print(out)
