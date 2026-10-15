import pandas as pd, numpy as np
S='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad'
def ld(p, col='close'):
    x=pd.read_csv(p,parse_dates=['date']).set_index('date')
    x=x[~x.index.duplicated(keep='last')]
    return x
ndx=ld(f'{S}/analysis/sent/long/_NDX.csv')['close'].dropna()
spx=ld(f'{S}/analysis/sent/long/_GSPC.csv')['close'].dropna()
sox=ld(f'{S}/analysis/sent/long/_SOX.csv')['close'].dropna()
print('NDX last',ndx.index[-1].date(),ndx.iloc[-1],'ATH',ndx.max(),ndx.idxmax().date(),'DD',round((ndx.iloc[-1]/ndx.max()-1)*100,2))
# ATH-to-ATH episodes (close basis)
def episodes(s):
    rm=s.cummax(); dd=s/rm-1
    eps=[]; inep=False
    for i,(d,v) in enumerate(dd.items()):
        if v<0 and not inep:
            inep=True; start=s.index[i-1] if i>0 else d; 
        if inep and v==0:
            seg=dd[start:d]; eps.append((start, seg.idxmin(), seg.min(), d)); inep=False
    if inep:
        seg=dd[start:]; eps.append((start, seg.idxmin(), seg.min(), None))
    return eps, dd
eps,dd=episodes(ndx)
sma200=ndx.rolling(200).mean()
def cond(eps, dd, thr, s, extra=None, label=''):
    rows=[]
    for st,tr,depth,end in eps:
        if depth> -thr: continue
        seg=dd[st:]
        if end is not None: seg=dd[st:end]
        hit=seg[seg<=-thr].index[0]
        if extra is not None and not extra(hit, st): continue
        if end is None and hit==dd.index[-1]: continue  # current
        if end is None: continue
        days=len(dd[hit:tr])-1
        rows.append(dict(start=st.date(),hit=hit.date(),trough=tr.date(),depth=round(depth*100,1),extra_days=days))
    df=pd.DataFrame(rows)
    if len(df)==0: print(label,'n=0'); return df
    d=-df.depth
    print(f'{label} given reached -{thr*100:.2f}%: n={len(df)}, median final {(-d.median()):.1f}%, '
          f'%>=8%: {(d>=8).mean()*100:.0f}, %>=10%: {(d>=10).mean()*100:.0f}, %>=13%: {(d>=13).mean()*100:.0f}, %>=15%: {(d>=15).mean()*100:.0f}, %>=20%: {(d>=20).mean()*100:.0f}; median sessions hit->trough {df.extra_days.median()}')
    return df
thr=0.0404
df_all=cond(eps,dd,thr,ndx,label='NDX 1985-')
df_200=cond(eps,dd,thr,ndx,extra=lambda h,st: ndx[h]>sma200[h] and sma200[h]>sma200.shift(20)[h],label='NDX above rising 200d at hit')
# SPX within 2% of its ATH when NDX hits -4%
spx_dd=spx/spx.cummax()-1
df_narrow=cond(eps,dd,thr,ndx,extra=lambda h,st: h in spx_dd.index and spx_dd[h]>-0.02,label='NDX -4% while SPX within 2% of ATH')
df_narrow200=cond(eps,dd,thr,ndx,extra=lambda h,st: h in spx_dd.index and spx_dd[h]>-0.02 and ndx[h]>sma200[h],label='... and NDX>200d')
# SOX >=10% below its 20d high at hit
sox20=sox/sox.rolling(20).max()-1
df_sox=cond(eps,dd,thr,ndx,extra=lambda h,st: h in sox20.index and sox20[h]<=-0.10,label='NDX -4% & SOX>=10% below 20d high')
# fast: hit within 10 sessions of ATH
df_fast=cond(eps,dd,thr,ndx,extra=lambda h,st: len(ndx[st:h])<=10,label='NDX -4% within 10 sessions of ATH')
df_fast200=cond(eps,dd,thr,ndx,extra=lambda h,st: len(ndx[st:h])<=10 and ndx[h]>sma200[h],label='... fast & >200d')
df5=cond(eps,dd,0.05,ndx,label='NDX 1985- (given -5%, ~overnight)')
df5b=cond(eps,dd,0.05,ndx,extra=lambda h,st: ndx[h]>sma200[h] and sma200[h]>sma200.shift(20)[h],label='NDX -5% above rising 200d')
for name,df in [('narrow',df_narrow),('narrow200',df_narrow200),('fast200',df_fast200),('sox',df_sox)]:
    print(name); print(df.to_string())
# post-2009 subset
eps2=[e for e in eps if e[0]>=pd.Timestamp('2009-03-01')]
cond(eps2,dd,thr,ndx,label='NDX 2009-')
cond(eps2,dd,thr,ndx,extra=lambda h,st: ndx[h]>sma200[h],label='NDX 2009- >200d')
