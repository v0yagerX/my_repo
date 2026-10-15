import pandas as pd
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data'
def c(s): return pd.read_csv(f'{D}/{s}.csv',parse_dates=['date']).set_index('date')['close']
syms=['SOXX','NVDA','MU','AVGO','TSM','AMD','QQQ','SPY','RSP','_TNX']
df=pd.concat({s:c(s) for s in syms},axis=1)
r=df.pct_change()*100
r['_TNX']=df['_TNX'].diff()*100  # bp... TNX in %, diff*100 = bp
w=r['2026-06-01':]
big=w[abs(w.SOXX)>=2.5]
print(big.round(2).to_string())
