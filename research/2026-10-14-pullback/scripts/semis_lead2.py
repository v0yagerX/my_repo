import pandas as pd, numpy as np, os
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data'
def load(s):
    df=pd.read_csv(os.path.join(D,s.replace('^','_')+'.csv'),parse_dates=['date']).set_index('date').sort_index()
    return df[~df.index.duplicated(keep='last')]
C={s:load(s)['close'] for s in ['SOXX','SMH','^SOX','SPY','QQQ','NVDA','RSP','XLK','MU','AVGO','TSM','AMD','QQQE','IWM','XLU','XLP','XLV','XLF','XLE','XLI','XLB','XLRE','XLC','XLY','GLD','TLT','MDY','HYG','^GSPC']}
px=pd.DataFrame(C).dropna(how='all')
# daily % moves Jun 15 - Aug 10
r=px[['SOXX','NVDA','MU','AVGO','TSM','AMD','QQQ','SPY','RSP']].pct_change()*100
print(r.loc['2026-06-15':'2026-08-12'].round(2).to_string())
print('\n=== Sep10-Oct14 daily')
print(r.loc['2026-09-08':].round(2).to_string())
print('\n=== RATIOS')
pairs=[('SOXX','SPY'),('SMH','QQQ'),('NVDA','SOXX'),('RSP','SPY'),('QQQ','SPY'),('XLK','SPY'),('NVDA','QQQ'),('NVDA','SMH'),('SOXX','QQQ'),('QQQE','QQQ'),('IWM','SPY')]
out=[]
for a,b in pairs:
    q=(px[a]/px[b]).dropna()
    m50=q.rolling(50).mean(); m200=q.rolling(200).mean()
    last=q.iloc[-1]
    out.append(dict(ratio=f'{a}/{b}',last=round(last,4),vs50=(last/m50.iloc[-1]-1)*100,vs200=(last/m200.iloc[-1]-1)*100,
      chg20=(last/q.iloc[-21]-1)*100, ma20slope=(q.rolling(20).mean().iloc[-1]/q.rolling(20).mean().iloc[-21]-1)*100,
      ma50slope20=(m50.iloc[-1]/m50.iloc[-21]-1)*100,
      chg5=(last/q.iloc[-6]-1)*100, since_oct6=(last/q.loc[:'2026-10-06'].iloc[-1]-1)*100, since_jun22=(last/q.loc[:'2026-06-22'].iloc[-1]-1)*100,
      hi1y=q.iloc[-252:].idxmax().date(), pct_rank_1y=(q.iloc[-252:]<last).mean()*100,
      above50=last>m50.iloc[-1], above200=last>m200.iloc[-1], m50_vs_m200=(m50.iloc[-1]/m200.iloc[-1]-1)*100))
print(pd.DataFrame(out).round(2).to_string(index=False))
print('\n=== SECTOR ETFs')
secs=['XLK','XLC','XLY','XLF','XLI','XLE','XLB','XLU','XLP','XLV','XLRE','SPY','RSP','QQQ','IWM','MDY','SOXX','SMH','GLD','TLT','HYG']
o=[]
for s in secs:
    c=px[s].dropna()
    o.append(dict(sym=s,d1=(c.iloc[-1]/c.iloc[-2]-1)*100,w1=(c.iloc[-1]/c.iloc[-6]-1)*100,w2=(c.iloc[-1]/c.iloc[-11]-1)*100,m1=(c.iloc[-1]/c.iloc[-22]-1)*100,
      since_oct6=(c.iloc[-1]/c.loc[:'2026-10-06'].iloc[-1]-1)*100,m3=(c.iloc[-1]/c.iloc[-64]-1)*100,
      since_jun22=(c.iloc[-1]/c.loc[:'2026-06-22'].iloc[-1]-1)*100,
      rel_spy_1m=((c.iloc[-1]/c.iloc[-22])/(px['SPY'].iloc[-1]/px['SPY'].iloc[-22])-1)*100,
      vs50=(c.iloc[-1]/c.iloc[-50:].mean()-1)*100))
S=pd.DataFrame(o).sort_values('w1',ascending=False)
print(S.round(2).to_string(index=False))
