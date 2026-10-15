import pandas as pd, numpy as np, sys
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data/'
def load(s):
    df=pd.read_csv(D+s+'.csv',parse_dates=['date']).set_index('date')
    return df
nv=load('NVDA'); sx=load('SOXX'); qq=load('QQQ')
c=nv.close
print('rows',len(c),c.index[0].date(),c.index[-1].date())

# A. 200d projection
print('\n== A. 200d SMA projection ==')
for path,label in [(None,'flat 221.30'),('lin205','linear to 205 by +15 sessions'),('lin200','linear to 200 by +15')]:
    out=[]
    for n in [10,15,25]:
        if path is None: fut=[221.30]*n
        else:
            tgt=205 if path=='lin205' else 200
            fut=list(np.linspace(221.30,tgt,16)[1:])+[tgt]*max(0,n-15)
            fut=fut[:n]
        s=pd.concat([c,pd.Series(fut)],ignore_index=True)
        out.append((n,round(s.iloc[-200:].mean(),2),round(s.iloc[-50:].mean(),2),round(s.iloc[-100:].mean(),2)))
    print(label,'(sessions, 200d, 50d, 100d):',out)

# B. Unbiased conditional drawdown from running ATH close (5y data)
print('\n== B. Unbiased conditional (ATH-close drawdown episodes, since 2021-10) ==')
ath=c.cummax(); dd=c/ath-1
sma200=c.rolling(200).mean()
# episodes: from a new ATH to next new ATH
eps=[]; i=0; idx=c.index
peak_i=0
for j in range(1,len(c)):
    if c.iloc[j]>=ath.iloc[j-1] and c.iloc[j]==ath.iloc[j]:
        if j-peak_i>1:
            seg=c.iloc[peak_i:j]
            eps.append((peak_i,j,seg))
        peak_i=j
# ongoing
eps.append((peak_i,len(c),c.iloc[peak_i:]))
for thr in [0.075,0.087,0.0907,0.10]:
    rows=[]
    for (pi,ej,seg) in eps:
        d=seg/seg.iloc[0]-1
        if d.min()<=-thr:
            hit=d[d<=-thr].index[0]
            trough=d.idxmin()
            ongoing = ej==len(c)
            below200=(seg< sma200.loc[seg.index]).any()
            rows.append(dict(peak=seg.index[0].date(),final=round(d.min()*100,1),trough=trough.date(),
                             extra_days=int(c.index.get_loc(trough)-c.index.get_loc(hit)),ongoing=ongoing,below200=bool(below200)))
    r=pd.DataFrame(rows); comp=r[~r.ongoing]
    print(f'thr {thr*100:.2f}%: n_completed={len(comp)} median final={comp.final.median()} ; shallower than -10%: {(comp.final>-10).mean()*100:.0f}% ; -15: {(comp.final>-15).mean()*100:.0f}% ; -20: {(comp.final>-20).mean()*100:.0f}% ; closed<200d: {comp.below200.mean()*100:.0f}% ; median extra sessions {comp.extra_days.median()}')
    print(comp.to_string(index=False))

# C. Holdout catch-down: SOXX <= -10% from 60d closing high while NVDA >= -9% from its own 60d closing high
print('\n== C. Holdout catch-down ==')
df=pd.DataFrame({'nv':c,'sx':sx.close,'qq':qq.close}).dropna()
df['sxdd']=df.sx/df.sx.rolling(60).max()-1
df['nvdd']=df.nv/df.nv.rolling(60).max()-1
sig=df[(df.sxdd<=-0.10)&(df.nvdd>=-0.09)&(df.nvdd<=-0.04)]
last=None; picks=[]
for d in sig.index:
    if last is None or (df.index.get_loc(d)-df.index.get_loc(last))>=10:
        picks.append(d); last=d
res=[]
for d in picks:
    k=df.index.get_loc(d)
    for h in [20,40]:
        pass
    f20=df.nv.iloc[k+1:k+21]; f40=df.nv.iloc[k+1:k+41]
    s20=df.sx.iloc[k+1:k+21]
    res.append(dict(date=d.date(),nvdd=round(df.nvdd.iloc[k]*100,1),sxdd=round(df.sxdd.iloc[k]*100,1),
        nv_mae20=round((f20.min()/df.nv.iloc[k]-1)*100,1) if len(f20) else np.nan,
        nv_ret20=round((f20.iloc[-1]/df.nv.iloc[k]-1)*100,1) if len(f20)==20 else np.nan,
        nv_mae40=round((f40.min()/df.nv.iloc[k]-1)*100,1) if len(f40) else np.nan,
        nv_ret40=round((f40.iloc[-1]/df.nv.iloc[k]-1)*100,1) if len(f40)==40 else np.nan,
        sx_mae20=round((s20.min()/df.sx.iloc[k]-1)*100,1) if len(s20) else np.nan))
r=pd.DataFrame(res); print(r.to_string(index=False))
rc=r.dropna(subset=['nv_ret20'])
print('n',len(rc),'median nv MAE20',rc.nv_mae20.median(),'median ret20',rc.nv_ret20.median(),'share MAE20<=-5%',(rc.nv_mae20<=-5).mean())

# D. down-day betas
print('\n== D. NVDA beta to SOXX/QQQ on SOXX down days ==')
rt=df[['nv','sx','qq']].pct_change().dropna()
for win,lab in [(252,'1y'),(63,'3m')]:
    x=rt.iloc[-win:]
    dn=x[x.sx<0]; up=x[x.sx>0]
    b=lambda a,bb: np.cov(a,bb)[0,1]/np.var(bb,ddof=1)
    print(lab,'down-day beta vs SOXX',round(b(dn.nv,dn.sx),2),'up-day',round(b(up.nv,up.sx),2),
          '| down-QQQ-day beta vs QQQ',round(b(x[x.qq<0].nv,x[x.qq<0].qq),2))
# big SOXX down days (<-3%) NVDA average ratio
big=rt[rt.sx<-0.03].iloc[-40:]
print('SOXX <-3% days (last 40 since', big.index[0].date(),'): median NVDA/SOXX move ratio',round((big.nv/big.sx).median(),2), 'n',len(big))

# E. failed breakouts above a prior closing high (>=40 sessions old) reversed within 5 sessions
print('\n== E. Failed breakouts above an old closing high ==')
rows=[]
cc=c.values
for t in range(130,len(c)-1):
    prior=c.iloc[t-120:t]
    ph=prior.max(); phi=prior.idxmax()
    age=t-c.index.get_loc(phi)
    if cc[t]>ph and cc[t-1]<=ph and age>=40:
        # within next 5 sessions close back below ph?
        for u in range(t+1,min(t+6,len(c))):
            if cc[u]<ph:
                f=c.iloc[u+1:u+41]
                rows.append(dict(breakout=c.index[t].date(),prior_high=round(ph,2),fail=c.index[u].date(),
                    ret20=round((c.iloc[u+20]/cc[u]-1)*100,1) if u+20<len(c) else np.nan,
                    mae20=round((c.iloc[u+1:u+21].min()/cc[u]-1)*100,1) if u+1<len(c) else np.nan,
                    ret40=round((c.iloc[u+40]/cc[u]-1)*100,1) if u+40<len(c) else np.nan,
                    mae40=round((f.min()/cc[u]-1)*100,1) if len(f) else np.nan))
                break
print(pd.DataFrame(rows).to_string(index=False))

# F. Volume at price, last 63 and 126 sessions, 2-dollar bins 186-232
print('\n== F. Volume-at-price (typical price allocation) ==')
for win in [63,126]:
    x=nv.iloc[-win:]
    tp=(x.high+x.low+x.close)/3
    bins=np.arange(186,246,2)
    h=pd.cut(tp,bins).value_counts(sort=False)
    v=x.volume.groupby(pd.cut(tp,bins),observed=False).sum()
    pct=(v/v.sum()*100).round(1)
    print(win, {str(k):p for k,p in pct.items() if p>0})
