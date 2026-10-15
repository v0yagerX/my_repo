import pandas as pd, numpy as np
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data/'
def L(s):
    df=pd.read_csv(D+s+'.csv',parse_dates=['date']).set_index('date')
    return df
vix=L('_VIX'); v3=L('_VIX3M'); vv=L('_VVIX'); spx=L('_GSPC'); nd=L('_NDX'); sox=L('_SOX'); nv=L('NVDA')
df=pd.DataFrame({'vix':vix.close,'vixh':vix.high,'v3':v3.close,'vv':vv.close,'vvh':vv.high,'spx':spx.close,'spxl':spx.low,'ndx':nd.close,'sox':sox.close,'nvda':nv.close}).dropna(subset=['vix'])
df['ratio']=df.vix/df.v3
last=df.iloc[-1]
print('Last row', df.index[-1].date()); print(last.round(3))
# percentiles
for win,lab in [(252,'1y'),(504,'2y'),(1250,'5y')]:
    s=df.vix.iloc[-win:]
    print(lab,'VIX pct rank of last', round((s<last.vix).mean()*100,1), 'min',round(s.min(),2),'median',round(s.median(),2),'max',round(s.max(),2))
    r=df.ratio.dropna().iloc[-win:]
    print(lab,'ratio pct', round((r<last.ratio).mean()*100,1),'median',round(r.median(),3), 'days>1:',(r>1).sum())
    w=df.vv.dropna().iloc[-win:]
    print(lab,'VVIX pct', round((w<last.vv).mean()*100,1),'median',round(w.median(),2),'max',round(w.max(),2))
print('VIX last 25 days'); print(df[['vix','vixh','v3','ratio','vv','spx']].iloc[-25:].round(3).to_string())
# daily change
print('VIX 1d chg', round(df.vix.iloc[-1]-df.vix.iloc[-2],2), round((df.vix.iloc[-1]/df.vix.iloc[-2]-1)*100,1),'%')
print('VVIX 1d chg', round(df.vv.iloc[-1]-df.vv.iloc[-2],2))
# 1y VIX history: rolling stats
print('2026 YTD VIX max/min', df.loc['2026'].vix.max(), df.loc['2026'].vix.idxmax().date(), df.loc['2026'].vix.min(), df.loc['2026'].vix.idxmin().date())
df.to_pickle('/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/scripts/voldf.pkl')
