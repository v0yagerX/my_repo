# Reproduces semis_bear.md level math: SOXX 200d projection, AVWAPs, down-leg ratios, beta mapping, 3m volume bins
import pandas as pd, numpy as np
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data/'
L=lambda s: pd.read_csv(D+s+'.csv',parse_dates=['date']).set_index('date')
sx,q,sm=L('SOXX'),L('QQQ'),L('SMH')
bd=pd.bdate_range('2026-10-15','2026-12-15',freq='C',holidays=['2026-11-26'])
for nm,df,X in [('SOXX',sx,490),('SOXX',sx,465),('SMH',sm,sm.close.iloc[-1]*0.93)]:
    path=pd.Series(np.linspace(df.close.iloc[-1],X,11)[1:].tolist()+[X]*(len(bd)-10),index=bd)
    sma=pd.concat([df.close,path]).rolling(200).mean()
    print(nm,'->',round(X,1),{d:round(sma.loc[d],1) for d in ['2026-10-28','2026-11-04','2026-11-18']})
tp=(sx.high+sx.low+sx.close)/3
for a in ['2026-03-30','2026-06-22','2026-07-29','2026-10-05']:
    s=sx.loc[a:]; print('AVWAP',a,round((tp.loc[a:]*s.volume).sum()/s.volume.sum(),2))
for a,b in [('2026-06-22','2026-07-29'),('2026-10-06','2026-10-14')]:
    rs=sx.close.loc[b]/sx.close.loc[a]-1; rq=q.close.loc[b]/q.close.loc[a]-1; print(a,b,round(rs*100,1),round(rq*100,1),round(rs/rq,2))
r=pd.concat([sx.close.pct_change(),q.close.pct_change()],axis=1,keys=['s','q']).dropna().iloc[-252:]
b=lambda d: np.cov(d.s,d.q)[0,1]/d.q.var(); print('beta all/down/up',round(b(r),2),round(b(r[r.q<0]),2),round(b(r[r.q>0]),2))
s3=sx.iloc[-63:]; h=pd.Series(s3.volume.values,index=pd.cut((s3.high+s3.low+s3.close)/3,np.arange(440,620,8))).groupby(level=0,observed=False).sum()
print((h/h.sum()*100).round(1).to_string())
