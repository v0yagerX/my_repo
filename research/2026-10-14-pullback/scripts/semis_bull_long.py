import pandas as pd, numpy as np
P='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/'
L=pd.read_csv(P+'analysis/sent/long/_SOX.csv',parse_dates=['date']).set_index('date')
S=pd.read_csv(P+'data/_SOX.csv',parse_dates=['date']).set_index('date')
j=L['close'].reindex(S.index).dropna()
print('cross-check overlap rows',len(j),'max abs pct diff',round(((j/S['close'].reindex(j.index)-1).abs().max())*100,4))
c=L['close']; c=c[~c.index.duplicated()]
sma200=c.rolling(200).mean(); sl=sma200/sma200.shift(20)-1
vals=c.values; idx=c.index; th=0.08
piv=[]; trend=0; last_hi=0; last_lo=0
for i in range(1,len(vals)):
    if trend>=0:
        if vals[i]>vals[last_hi]: last_hi=i
        if vals[i]<=vals[last_hi]*(1-th):
            piv.append(('H',last_hi)); trend=-1; last_lo=i
    else:
        if vals[i]<vals[last_lo]: last_lo=i
        if vals[i]>=vals[last_lo]*(1+th):
            piv.append(('L',last_lo)); trend=1; last_hi=i
rows=[]
for k in range(len(piv)-1):
    if piv[k][0]=='H' and piv[k+1][0]=='L':
        h=piv[k][1]; l=piv[k+1][1]
        seg=vals[h:l+1]/vals[h]-1
        hit=np.where(seg<=-0.119)[0]
        rows.append(dict(pk=idx[h].date(),tr=idx[l].date(),depth=(vals[l]/vals[h]-1)*100,n=l-h,
            above=bool(vals[h]>sma200.iloc[h]) if not np.isnan(sma200.iloc[h]) else None,
            rising=bool(sl.iloc[h]>0) if not np.isnan(sl.iloc[h]) else None,
            hit=int(hit[0]) if len(hit) else None))
r=pd.DataFrame(rows)
print('last pivot',piv[-1][0],idx[piv[-1][1]].date(),round(vals[piv[-1][1]],2))
base=r[(r.depth<=-11.9)&(r.above==True)&(r.rising==True)]
def summ(x,label):
    d=x.depth
    print(f'\n{label}: n={len(x)} median depth {d.median():.1f}%, mean {d.mean():.1f}%')
    for t in [13.5,15,17,20,25,30]: print(f'  shallower than -{t}%: {(d>-t).mean()*100:.0f}%')
    print('  median sessions peak->trough',x.n.median(),' 25/75pct',x.n.quantile(.25),x.n.quantile(.75))
summ(base,'SOX swing legs (zigzag 8%) reaching -11.9%, peak above rising 200d, 1995-2026')
fast=base[base.hit<=7]
summ(fast,'  ...and reached -11.9% within 7 sessions of the peak')
print(fast[['pk','tr','depth','n','hit']].to_string(index=False))
# condition: reached -13.4% (overnight equivalent)
b2=r[(r.depth<=-13.4)&(r.above==True)&(r.rising==True)]
summ(b2,'Legs reaching -13.4% (overnight-equivalent), peak above rising 200d')
# post-2009 only
b3=base[pd.to_datetime(base.pk)>=pd.Timestamp('2009-06-01')]
summ(b3,'Same as base, 2009-06 onward')
print(b3[['pk','tr','depth','n','hit']].to_string(index=False))
# all legs reaching -11.9% regardless of trend
summ(r[r.depth<=-11.9],'ALL legs reaching -11.9% (any trend), 1995-2026')
# fast-decline analog long history: 7-session <=-10% while above rising 200d
r7=c/c.shift(7)-1
cond=(r7<=-0.10)&(c>sma200)&(sl>0)
sig=[]; last=-999
for d in c.index[cond]:
    i=c.index.get_loc(d)
    if i-last>15: sig.append(i)
    last=i if i-last>15 else last
out=[]
for i in sig:
    if i+40>=len(c): out.append((idx[i].date(),np.nan,np.nan,np.nan,np.nan)); continue
    f20=(c.iloc[i+20]/c.iloc[i]-1)*100; f40=(c.iloc[i+40]/c.iloc[i]-1)*100
    mae=(c.iloc[i+1:i+41].min()/c.iloc[i]-1)*100
    t=int(np.argmin(c.iloc[i:i+41].values))
    out.append((idx[i].date(),round(f20,1),round(f40,1),round(mae,1),t))
o=pd.DataFrame(out,columns=['date','f20','f40','mae40','sess_to_min']).dropna()
print('\nSOX 7-session <=-10% while above rising 200d, 1995-2026, de-clustered 15d: n=',len(o))
print(o.to_string(index=False))
print('median',o[['f20','f40','mae40','sess_to_min']].median().to_dict())
print('mae40 shallower than -5%:',(o.mae40>-5).mean().round(2),' -10%:',(o.mae40>-10).mean().round(2),' f40>0:',(o.f40>0).mean().round(2))
print('min-at-signal (sess_to_min==0):',(o.sess_to_min==0).mean().round(2))
