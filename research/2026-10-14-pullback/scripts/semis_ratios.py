import pandas as pd, numpy as np
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data'
def c(s): return pd.read_csv(f'{D}/{s}.csv',parse_dates=['date']).set_index('date')['close'].dropna()
pairs=[('SOXX','SPY'),('SMH','QQQ'),('NVDA','SOXX'),('NVDA','SMH'),('NVDA','QQQ'),('RSP','SPY'),('QQQ','SPY'),('XLK','SPY'),('QQQE','QQQ'),('IWM','SPY'),('_SOX','_NDX'),('MU','SOXX'),('TSM','SOXX'),('AVGO','SOXX'),('AMD','SOXX')]
print(f"{'ratio':12s} {'last':>8s} {'vs50%':>7s} {'vs200%':>7s} {'20dchg%':>8s} {'50dMA 20d slope%':>16s} {'50>200':>6s} {'sinceJun22%':>11s} {'sinceOct6%':>10s} {'1yHighDate':>11s} {'%off1yHi':>8s}")
for a,b in pairs:
    r=(c(a)/c(b)).dropna()
    m50=r.rolling(50).mean(); m200=r.rolling(200).mean()
    last=r.iloc[-1]
    hi=r[-252:].max(); hid=r[-252:].idxmax()
    print(f"{(a+'/'+b).replace('_',''):12s} {last:8.4f} {(last/m50.iloc[-1]-1)*100:7.1f} {(last/m200.iloc[-1]-1)*100:7.1f} {(last/r.iloc[-21]-1)*100:8.1f} {(m50.iloc[-1]/m50.iloc[-21]-1)*100:16.2f} {str(m50.iloc[-1]>m200.iloc[-1]):>6s} {(last/r[:'2026-06-22'].iloc[-1]-1)*100:11.1f} {(last/r[:'2026-10-06'].iloc[-1]-1)*100:10.1f} {hid.strftime('%Y-%m-%d'):>11s} {(last/hi-1)*100:8.1f}")
# Sector rotation
print('\nSector ETF returns (%):')
secs=['XLK','XLC','XLY','XLF','XLI','XLB','XLE','XLU','XLV','XLP','XLRE','SPY','RSP','IWM','MDY','QQQ','SOXX','GLD','TLT','HYG','LQD']
rows=[]
spy=c('SPY')
for s in secs:
    x=c(s)
    def back(n): return (x.iloc[-1]/x.iloc[-1-n]-1)*100
    def frm(d): return (x.iloc[-1]/x[:d].iloc[-1]-1)*100
    m50=x.rolling(50).mean().iloc[-1]; m200=x.rolling(200).mean().iloc[-1]
    rows.append(dict(sym=s,r1w=back(5),since_oct6=frm('2026-10-06'),r1m=back(21),r3m=back(63),since_jun22=frm('2026-06-22'),ytd=frm('2025-12-31'),vs50=(x.iloc[-1]/m50-1)*100,vs200=(x.iloc[-1]/m200-1)*100, rel1m_vs_spy=back(21)-((spy.iloc[-1]/spy.iloc[-22]-1)*100)))
df=pd.DataFrame(rows).sort_values('r1w',ascending=False)
print(df.round(1).to_string(index=False))
