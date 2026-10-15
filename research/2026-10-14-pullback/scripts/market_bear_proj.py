import pandas as pd, numpy as np
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data/'
c=pd.read_csv(D+'_GSPC.csv',parse_dates=['date']).drop_duplicates('date',keep='last').set_index('date')['close']
r=pd.read_csv(D+'RSP.csv',parse_dates=['date']).drop_duplicates('date',keep='last').set_index('date')['close']
bd=pd.bdate_range('2026-10-15','2026-12-11')
for name,s,target in [('SPX',c,7400.0),('SPX',c,7700.0),('RSP',r,205.0)]:
    n=len(bd); path=np.linspace(s.iloc[-1],target,n)
    ext=pd.concat([s,pd.Series(path,index=bd)])
    sma=ext.rolling(200).mean()
    print(name,'path to',target,'| 200d on Nov 20:',round(sma.loc['2026-11-20'],2),'Dec 11:',round(sma.loc['2026-12-11'],2))
# Aug-Sep range measured move
lo,hi=7504.78,7816.70; print('measured move', round(lo-(hi-lo),2), round(100*((lo-(hi-lo))/7718.94-1),2))
