import pandas as pd, numpy as np, os
S='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad'
cons=pd.read_csv(f'{S}/data/spx_constituents.csv')
it=cons[cons['GICS Sector']=='Information Technology'].Symbol.tolist()
cl={}
for s in it:
    f=f'{S}/data/spx/{s.replace(".","-")}.csv'
    if not os.path.exists(f): f=f'{S}/data/spx/{s}.csv'
    if not os.path.exists(f): continue
    x=pd.read_csv(f,parse_dates=['date']).set_index('date'); x=x[~x.index.duplicated(keep='last')]
    cl[s]=x['close']
c=pd.DataFrame(cl)
print('IT members loaded',c.shape[1])
a50=(c>c.rolling(50).mean()).sum(1)/c.notna().sum(1)*100
a200=(c>c.rolling(200).mean()).sum(1)/c.notna().sum(1)*100
hi52=c.rolling(252,min_periods=200).max(); nh=(c>=hi52).sum(1)
for d in ['2026-06-18','2026-07-29','2026-08-14','2026-09-16','2026-10-06','2026-10-08','2026-10-13','2026-10-14']:
    print(d,'IT pct>50d %.1f  pct>200d %.1f  new52wH %d'%(a50[d],a200[d],nh[d]))
med_dd=(c.iloc[-1]/c['2025-10-14':].max()-1).median()*100
print('IT median pct below 1y closing high: %.1f; share >=20pct below: %.0f'%(med_dd,((c.iloc[-1]/c['2025-10-14':].max()-1)<=-0.2).mean()*100))
r=c.pct_change()
for d in ['2026-10-08','2026-10-14']:
    print(d,'IT median %.2f%%, share up %.0f%%'%(r.loc[d].median()*100,(r.loc[d]>0).mean()*100))
q=pd.read_csv(f'{S}/data/QQQ.csv',parse_dates=['date']).set_index('date')
print('QQQ Jul29 close',q.close['2026-07-29'],'low',q.low['2026-07-29'],' Sep16 close',q.close['2026-09-16'])
x=pd.read_csv(f'{S}/data/XLK.csv',parse_dates=['date']).set_index('date')
print('XLK Jul29 close',x.close['2026-07-29'],'low',x.low['2026-07-29'],' Sep14 close',x.close['2026-09-14'], 'Aug24 close', x.close['2026-08-24'])
for lv in [746.45,744.85,726.66,724.0,721.12,719.62,712.0,700.0,697.13,690,685.82,683.7,682.91,675,662,661.14,660.34,645.7,642.18,634.77]:
    print(f'QQQ {lv}: {(lv/728.95-1)*100:+.2f}% vs close, {(lv/759.66-1)*100:+.2f}% vs ATH close')
for lv in [198.16,197.08,192.4,189.9,189.2,188.04,184.86,183.87,180.51,178.82,178,176.54,174.33,174.0,173.04,171.7,168,167.1,166.46,164.97]:
    print(f'XLK {lv}: {(lv/190.43-1)*100:+.2f}% vs close, {(lv/202.0-1)*100:+.2f}% vs ATH close')
