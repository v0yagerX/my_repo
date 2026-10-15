import pandas as pd, numpy as np, os
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data'
def load(s):
    df=pd.read_csv(os.path.join(D,s.replace('^','_')+'.csv'),parse_dates=['date']).set_index('date').sort_index()
    return df[~df.index.duplicated(keep='last')]
semis=['NVDA','AMD','AVGO','MRVL','ARM','ALAB','CRDO','TSM','ASML','AMAT','LRCX','KLAC','TER','MU','SNDK','WDC','STX','LITE','COHR','CIEN','ANET','TXN','ADI','NXPI','ON','MCHP','INTC','QCOM','MPWR']
infra=['ORCL','CRWV','NBIS','DELL','SMCI','VRT','CEG','VST']
C=pd.DataFrame({s:load(s).close for s in semis+infra}).loc['2025-06-01':]
def breadth(cols):
    c=C[cols]
    m50=c.rolling(50).mean(); m200=c.rolling(200,min_periods=150).mean()
    a50=(c>m50).sum(1)/c.notna().sum(1)*100; a200=(c>m200).sum(1)/m200.notna().sum(1)*100
    hi=c.rolling(252,min_periods=100).max(); bear=((c/hi-1)<-0.20).sum(1)/c.notna().sum(1)*100
    return pd.DataFrame({'pct>50d':a50,'pct>200d':a200,'pct_bear(>20%off52wHi)':bear})
b=breadth(semis)
for d in ['2026-06-22','2026-07-29','2026-08-17','2026-09-14','2026-09-25','2026-10-06','2026-10-08','2026-10-13','2026-10-14']:
    print(d, b.loc[d].round(0).to_dict())
print('infra now', breadth(infra).iloc[-1].round(0).to_dict())
# median drawdown
c=C[semis]; dd=(c.iloc[-1]/c.iloc[-252:].max()-1)*100
print('semis median DD from 52w closing high %.1f; mean %.1f' % (dd.median(), dd.mean()))
print(dd.sort_values().round(1).to_string())
# volumes
for s in ['SOXX','SMH','NVDA','QQQ']:
    df=load(s); v=df.volume
    print(s,'Oct14 vol/50d avg %.2f; max ratio last 10d %.2f' % (v.iloc[-1]/v.iloc[-51:-1].mean(), (v.iloc[-10:]/v.rolling(50).mean().shift(1).iloc[-10:]).max()))
    # compare to Jun23, Jul29, Jun5
    for d in ['2026-06-05','2026-06-23','2026-07-29','2026-09-14']:
        i=v.index.get_loc(pd.Timestamp(d)); print('   ',d,'vol/50d %.2f'%(v.iloc[i]/v.iloc[i-50:i].mean()))
# ratio levels vs Jul29 and Sep14
px=pd.DataFrame({s:load(s).close for s in ['SOXX','SPY','SMH','QQQ','NVDA']})
for a,b2 in [('SOXX','SPY'),('SMH','QQQ'),('NVDA','SOXX')]:
    q=px[a]/px[b2]
    print(a,b2,'now vs Jul29 %.1f%%, vs Sep14 %.1f%%, vs Jun22 %.1f%%' % ((q.iloc[-1]/q.loc['2026-07-29']-1)*100,(q.iloc[-1]/q.loc['2026-09-14']-1)*100,(q.iloc[-1]/q.loc['2026-06-22']-1)*100))
# SOXX drawdowns: compare Jun22->Jul29
s=px.SOXX
print('SOXX Jun22->Jul29 close %.1f%%; Jul29->Oct5 %.1f%%; Oct5->Oct14 %.1f%%' % ((s.loc['2026-07-29']/s.loc['2026-06-22']-1)*100,(s.loc['2026-10-05']/s.loc['2026-07-29']-1)*100,(s.iloc[-1]/s.loc['2026-10-05']-1)*100))
print('Retracement of Jul29->Oct5 rally: %.0f%%' % ((s.loc['2026-10-05']-s.iloc[-1])/(s.loc['2026-10-05']-s.loc['2026-07-29'])*100))
n=px.NVDA
print('NVDA retrace of Jul29->Oct6 rally: %.0f%%' % ((n.loc['2026-10-06']-n.iloc[-1])/(n.loc['2026-10-06']-n.loc['2026-07-29'])*100))
# consecutive down days SOXX
r=s.pct_change(); k=0
for x in r.iloc[::-1]:
    if x<0: k+=1
    else: break
print('SOXX consecutive down closes:',k)
# SOXX RSI14
d=s.diff(); up=d.clip(lower=0).ewm(alpha=1/14).mean(); dn=(-d.clip(upper=0)).ewm(alpha=1/14).mean(); rsi=100-100/(1+up/dn)
print('SOXX RSI14 now %.1f; at Jul29 %.1f; at Sep14 %.1f' % (rsi.iloc[-1], rsi.loc['2026-07-29'], rsi.loc['2026-09-14']))
