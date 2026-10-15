import pandas as pd, numpy as np
base='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/'
def fred(n):
    d=pd.read_csv(base+f'fred_{n}.csv',parse_dates=['observation_date']).set_index('observation_date')
    s=pd.to_numeric(d.iloc[:,0],errors='coerce').dropna(); return s
def yf(sym):
    d=pd.read_csv(base+f'data/{sym}.csv',parse_dates=['date']).set_index('date'); return d
def chg(s,label,unit=''):
    last=s.index[-1]; v=s.iloc[-1]
    out={'label':label,'last_date':last.date(),'last':round(v,3)}
    for name,days in [('1w',7),('1m',30),('3m',91),('6m',182),('1y',365)]:
        ref=s[:last-pd.Timedelta(days=days)]
        if len(ref): out[name]=round(v-ref.iloc[-1],3)
    ytd=s[s.index.year==last.year]
    out['ytd_start']=round(s[:pd.Timestamp(f'{last.year-1}-12-31')].iloc[-1],3)
    out['ytd_high']=round(ytd.max(),3); out['ytd_high_date']=ytd.idxmax().date()
    out['ytd_low']=round(ytd.min(),3); out['ytd_low_date']=ytd.idxmin().date()
    out['max_since_2024']=round(s.max(),3); out['max_date']=s.idxmax().date()
    return out
for n,l in [('DGS10','10y UST (FRED)'),('DGS2','2y UST (FRED)'),('T10Y2Y','10y-2y (FRED)'),('BAMLH0A0HYM2','HY OAS (FRED)'),('VIXCLS','VIX (FRED)')]:
    s=fred(n); print(chg(s,l))
for sym,l in [('_TNX','10y Yahoo ^TNX'),('_TYX','30y Yahoo ^TYX'),('_IRX','13w Yahoo ^IRX'),('DX-Y.NYB','DXY'),('GLD','GLD'),('TLT','TLT'),('HYG','HYG'),('LQD','LQD'),('JNK','JNK'),('BTC-USD','BTC'),('_VIX','VIX'),('_VIX3M','VIX3M'),('XLE','XLE')]:
    d=yf(sym); s=d['close'].dropna(); print(chg(s,l))
# last 15 rows yields
t=pd.concat({'10y':fred('DGS10'),'2y':fred('DGS2'),'2s10s':fred('T10Y2Y'),'HY':fred('BAMLH0A0HYM2')},axis=1)
print(t.tail(25))
tnx=yf('_TNX')[['close']].rename(columns={'close':'TNX'}); tyx=yf('_TYX')[['close']].rename(columns={'close':'TYX'}); irx=yf('_IRX')[['close']].rename(columns={'close':'IRX'})
print(pd.concat([tnx,tyx,irx],axis=1).tail(15))
# HY OAS percentiles
hy=fred('BAMLH0A0HYM2'); last=hy.index[-1]
for yrs in [1,2]:
    w=hy[last-pd.DateOffset(years=yrs):]
    print(f'HY OAS {yrs}y window: min {w.min()} ({w.idxmin().date()}), max {w.max()} ({w.idxmax().date()}), pct rank of last {hy.iloc[-1]}: {(w<hy.iloc[-1]).mean()*100:.1f}%')
w=hy; print(f'HY OAS full file since {hy.index[0].date()}: min {w.min()} ({w.idxmin().date()}), max {w.max()} ({w.idxmax().date()}), pct rank {(w<hy.iloc[-1]).mean()*100:.1f}%')
print(hy.tail(30).to_string())
