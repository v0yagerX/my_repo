import json, pandas as pd, numpy as np, datetime as dt, sys
j=json.load(open(sys.argv[1]))['chart']['result'][0]
ts=pd.to_datetime(j['timestamp'],unit='s').tz_localize('UTC').tz_convert('America/New_York').normalize().tz_localize(None)
c=pd.Series(j['indicators']['quote'][0]['close'],index=ts).dropna()
c=c[~c.index.duplicated(keep='last')]
print('range',c.index[0].date(),c.index[-1].date(),c.iloc[-1])
def eday(y):
    d=dt.date(y,11,1)
    while d.weekday()!=0: d+=dt.timedelta(days=1)  # first Monday
    return pd.Timestamp(d+dt.timedelta(days=1))
def px(d,how='before'):
    if how=='before': return c[:d].iloc[-1], c[:d].index[-1]
    s=c[d:]; return s.iloc[0], s.index[0]
rows=[]
for y in range(1950,2026,4):
    y=y+2 if y%4==0 else y
for y in [1954+4*k for k in range(18)]:
    if y>2022: break
    ed=eday(y)
    p_oct14,_=px(pd.Timestamp(y,10,14))
    p_ed,_=px(ed - pd.Timedelta(days=1))  # close before election day (Monday)
    p_dec,_=px(pd.Timestamp(y,12,31))
    p_prevdec,_=px(pd.Timestamp(y-1,12,31))
    yr=c[str(y)]
    low_d=yr.idxmin(); 
    # max drawdown within year
    dd=(yr/yr.cummax()-1); mdd=dd.min()
    # after election: 3m, 6m, 12m from close on election-eve
    after={}
    for nm,days in [('3m',91),('6m',182),('12m',365)]:
        p,_=px(ed - pd.Timedelta(days=1)+pd.Timedelta(days=days)); after[nm]=p/p_ed-1
    # Oct14 to Nov-low? max drawdown from Oct14 to election
    seg=c[pd.Timestamp(y,10,14):ed]
    seg_dd=seg.min()/p_oct14-1
    rows.append(dict(year=y,ytd_to_oct14=p_oct14/p_prevdec-1,oct14_to_eday=p_ed/p_oct14-1,min_oct14_to_eday=seg_dd,oct14_to_dec31=p_dec/p_oct14-1,
                     year_ret=p_dec/p_prevdec-1,year_low_date=low_d.date(),max_dd_in_year=mdd,**{'post_'+k:v for k,v in after.items()}))
df=pd.DataFrame(rows).set_index('year')
pd.set_option('display.width',250)
fmt=df.copy()
for col in fmt.columns:
    if col!='year_low_date': fmt[col]=(fmt[col]*100).round(1)
print(fmt.to_string())
num=df.drop(columns='year_low_date')
print('\nMEAN %'); print((num.mean()*100).round(1).to_string())
print('\nMEDIAN %'); print((num.median()*100).round(1).to_string())
print('\n% positive'); print(((num>0).mean()*100).round(0).to_string())
print('\nyear low month counts:'); print(pd.Series([d.month for d in df.year_low_date]).value_counts().sort_index().to_string())
# Subset: strong years (ytd to Oct14 > +10%)
s=df[df.ytd_to_oct14>0.10]; print('\nStrong YTD>10% by Oct14 years:', list(s.index)); print((s.drop(columns='year_low_date')*100).round(1).to_string())
# All years baseline: Oct14->Dec31, non-midterm
allr=[]
for y in range(1950,2026):
    a,_=px(pd.Timestamp(y,10,14)); b,_=px(pd.Timestamp(y,12,31)); allr.append((y,b/a-1))
a=pd.Series(dict(allr)); nm=a[[y for y in a.index if y not in df.index]]
print('\nOct14->Dec31 all years 1950-2025 mean %.2f%% median %.2f%% pos %.0f%%; non-midterm mean %.2f%% median %.2f%%'%(a.mean()*100,a.median()*100,(a>0).mean()*100,nm.mean()*100,nm.median()*100))
# 2026 context
p25=c[:'2025-12-31'].iloc[-1]; print('2026 YTD to Oct14: %.2f%%'%((c.iloc[-1]/p25-1)*100), 'last',c.index[-1].date(),c.iloc[-1])
