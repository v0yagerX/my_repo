import pandas as pd, numpy as np
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data/'
names='NVDA AMD AVGO MRVL ARM ALAB CRDO TSM ASML AMAT LRCX KLAC TER MU SNDK WDC STX LITE COHR CIEN ANET TXN ADI NXPI ON MCHP INTC QCOM MPWR'.split()
cl={}
for n in names:
    df=pd.read_csv(D+n+'.csv',parse_dates=['date']).set_index('date'); cl[n]=df['close']
C=pd.DataFrame(cl)
m50=C.rolling(50).mean(); above=(C>m50).astype(float).where(m50.notna())
pct=(above.sum(axis=1)/above.notna().sum(axis=1).replace(0,np.nan))*100
s=pd.read_csv(D+'SOXX.csv',parse_dates=['date']).set_index('date')['close']
sma200=s.rolling(200).mean(); sl=sma200/sma200.shift(20)-1
pct=pct.reindex(s.index)
print('basket pct>50d last:',round(pct.iloc[-1],1),'n names',int(above.notna().sum(1).iloc[-1]))
cond=(pct<=17)&(s>sma200)&(sl>0)
sig=[];last=-99
for d in s.index[cond]:
    i=s.index.get_loc(d)
    if i-last>15: sig.append(d)
    last=i if i-last>15 else last
rows=[]
for d in sig:
    i=s.index.get_loc(d)
    f=lambda n:(s.iloc[i+n]/s.iloc[i]-1)*100 if i+n<len(s) else np.nan
    m=lambda n:(s.iloc[i+1:i+n+1].min()/s.iloc[i]-1)*100 if i+n<len(s) else np.nan
    seg=s.iloc[i:i+21]; t=int(np.argmin(seg.values))
    rows.append((d.date(),round(pct.loc[d],1),round(s.iloc[i],2),round(f(10),1),round(f(20),1),round(m(10),1),round(m(20),1),t))
o=pd.DataFrame(rows,columns=['date','pct50','soxx','f10','f20','mae10','mae20','sess_to_min20'])
print('Signals: semis basket <=17% above 50d while SOXX > rising 200d (de-clustered 15d)')
print(o.to_string(index=False))
oo=o.dropna()
print('completed n=',len(oo),'median',oo[['f10','f20','mae10','mae20','sess_to_min20']].median().to_dict())
# fast-decline analog medians excluding current
# check the 572.78 close
print(s[(s.index>='2026-09-15')&(s.index<='2026-10-02')].round(2).to_string())
# Oct6-14 moves
for t in ['SOXX','SMH','QQQ','NVDA','TSM','AVGO']:
    x=pd.read_csv(D+t+'.csv',parse_dates=['date']).set_index('date')['close']
    print(t,'Oct5->Oct14',round((x.loc['2026-10-14']/x.loc['2026-10-05']-1)*100,2),'Oct6->Oct14',round((x.loc['2026-10-14']/x.loc['2026-10-06']-1)*100,2))
# volume ratio
v=pd.read_csv(D+'SOXX.csv',parse_dates=['date']).set_index('date')['volume']
print('SOXX vol/50d last 8:',(v/v.rolling(50).mean()).tail(8).round(2).to_dict())
