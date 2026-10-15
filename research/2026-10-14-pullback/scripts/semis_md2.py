import pandas as pd, numpy as np, os
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data'
def load(s):
    df=pd.read_csv(os.path.join(D,s.replace('^','_')+'.csv'),parse_dates=['date']).set_index('date').sort_index()
    return df[~df.index.duplicated(keep='last')].close
syms=['SOXX','SMH','SPY','QQQ','NVDA','RSP','XLK','QQQE','IWM','XLU','XLP','XLV','XLF','XLE','XLI','XLB','XLRE','XLC','XLY','GLD','TLT','HYG','MDY']
px=pd.DataFrame({s:load(s) for s in syms})
pairs=[('SOXX','SPY'),('SMH','QQQ'),('NVDA','SOXX'),('RSP','SPY'),('QQQ','SPY'),('XLK','SPY'),('NVDA','QQQ'),('QQQE','QQQ'),('IWM','SPY')]
print('| Ratio | vs 50d MA | vs 200d MA | Above 50d? | Above 200d? | 20d change | 20d-MA slope (20d) | 50d-MA slope (20d) | 5d change | Since Oct 6 | Since Jun 22 | 1y pct-rank | 1y high date |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for a,b in pairs:
    q=(px[a]/px[b]).dropna(); m50=q.rolling(50).mean(); m200=q.rolling(200).mean(); m20=q.rolling(20).mean(); l=q.iloc[-1]
    g=lambda x:f'{x:+.1f}%'
    print(f'| {a}/{b} | {g((l/m50.iloc[-1]-1)*100)} | {g((l/m200.iloc[-1]-1)*100)} | {"yes" if l>m50.iloc[-1] else "NO"} | {"yes" if l>m200.iloc[-1] else "NO"} | {g((l/q.iloc[-21]-1)*100)} | {g((m20.iloc[-1]/m20.iloc[-21]-1)*100)} | {g((m50.iloc[-1]/m50.iloc[-21]-1)*100)} | {g((l/q.iloc[-6]-1)*100)} | {g((l/q.loc[:"2026-10-06"].iloc[-1]-1)*100)} | {g((l/q.loc[:"2026-06-22"].iloc[-1]-1)*100)} | {(q.iloc[-252:]<l).mean()*100:.0f} | {q.iloc[-252:].idxmax().date()} |')
print()
secs=['XLE','XLP','XLV','XLRE','XLU','XLF','XLB','XLY','XLC','XLI','RSP','SPY','MDY','IWM','QQQ','XLK','SMH','SOXX','TLT','GLD','HYG']
rows=[]
for s in secs:
    c=px[s].dropna(); sp=px['SPY']
    rows.append((s,(c.iloc[-1]/c.iloc[-2]-1)*100,(c.iloc[-1]/c.iloc[-6]-1)*100,(c.iloc[-1]/c.iloc[-22]-1)*100,(c.iloc[-1]/c.loc[:'2026-10-06'].iloc[-1]-1)*100,(c.iloc[-1]/c.iloc[-64]-1)*100,
       ((c.iloc[-1]/c.iloc[-6])/(sp.iloc[-1]/sp.iloc[-6])-1)*100,((c.iloc[-1]/c.iloc[-22])/(sp.iloc[-1]/sp.iloc[-22])-1)*100,(c.iloc[-1]/c.iloc[-50:].mean()-1)*100))
rows.sort(key=lambda r:-r[2])
print('| ETF | 1d (Oct 14) | 1w | 1m | Since Oct 6 | 3m | 1w vs SPY | 1m vs SPY | vs 50d |')
print('|---|---|---|---|---|---|---|---|---|')
for r in rows: print('| '+r[0]+' | '+' | '.join(f'{x:+.1f}' for x in r[1:])+' |')
