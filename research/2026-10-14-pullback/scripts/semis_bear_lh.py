import pandas as pd, numpy as np
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/'
sox=pd.read_csv(D+'analysis/sent/long/_SOX.csv',parse_dates=['date']).set_index('date')
c=sox['close']; v=c.values; idx=c.index; n=len(v)
LOOK=60; THR=0.11
rows=[]; armed=True; last_R=None
for t in range(260,n):
    w0=t-LOOK+1
    R_i=w0+int(np.argmax(v[w0:t+1])); R=v[R_i]
    if not armed:
        if v[t]>=v[t-LOOK+1:t+1].max(): armed=True
        continue
    if v[t]/R-1>-THR: continue
    # 1y high before R
    y0=max(0,R_i-252); H_i=y0+int(np.argmax(v[y0:R_i+1])); H=v[H_i]
    if H_i==R_i: # R itself is the 1y high -> not a lower-high setup
        cond_lh=False; T=np.nan; T_i=None
    else:
        T_i=H_i+int(np.argmin(v[H_i:R_i+1])); T=v[T_i]
        cond_lh=(R/H-1<=-0.08) and (T/H-1<=-0.20) and (R/T-1>=0.15)
    fw=v[t:min(n,t+250)]
    rec=np.where(fw>R)[0]; end=rec[0] if len(rec) else len(fw)
    seg=fw[:max(end,1)]; k=int(np.argmin(seg)); mn=seg[k]
    rows.append(dict(signal=idx[t].date(),H=idx[H_i].date(),T=idx[T_i].date() if T_i is not None else None,R=idx[R_i].date(),
        R_vs_H=(R/H-1)*100,T_vs_H=(T/H-1)*100 if T_i is not None else np.nan,rally=(R/T-1)*100 if T_i is not None else np.nan,
        lh=cond_lh,final_from_R=(mn/R-1)*100,extra=(mn/v[t]-1)*100,undercut_T=(mn<T) if T_i is not None else None,
        d_sig_trough=k,trough=idx[t+k].date(),recovered_R=bool(len(rec)),ongoing=(t+250>n and not len(rec))))
    armed=False; last_R=R
df=pd.DataFrame(rows)
pd.set_option('display.width',250); pd.set_option('display.max_rows',500)
lh=df[df.lh]
print(lh.round(1).to_string())
s=lh[pd.to_datetime(lh.signal)<'2026-10-01']
print('\nLower-high failure analogs (SOX 1995-2026) n=',len(s))
print('median extra',round(s.extra.median(),1),'mean',round(s.extra.mean(),1),'pct undercut T1',round(s.undercut_T.astype(bool).mean()*100),'pct extra<-5',round((s.extra<-5).mean()*100),'pct extra<-10',round((s.extra<-10).mean()*100),'median days sig->trough',s.d_sig_trough.median(),'median final from R',round(s.final_from_R.median(),1))
q=s.extra.quantile([.25,.5,.75]).round(1); print('extra quartiles',q.to_dict())
# relax: lower high vs 1y high by >=5%, prior trough >=20% below H, rally >=15%
print('\nAll signals (any setup) since 1995: n=',len(df[pd.to_datetime(df.signal)<'2026-10-01']),'median extra',round(df[pd.to_datetime(df.signal)<'2026-10-01'].extra.median(),1))
nl=df[(~df.lh)&(pd.to_datetime(df.signal)<'2026-10-01')]
print('Non-lower-high signals n=',len(nl),'median extra',round(nl.extra.median(),1),'pct extra<-10',round((nl.extra<-10).mean()*100))
for _,r in s.iterrows():
    pass
allp=df[pd.to_datetime(df.signal)<'2026-10-01'].copy()
for lab,sub in [('all 1995-',allp),('2009-',allp[pd.to_datetime(allp.signal)>='2009-06-01']),('2016-',allp[pd.to_datetime(allp.signal)>='2016-01-01'])]:
    print(f"\n[{lab}] n={len(sub)} median extra {sub.extra.median():.1f}; q25 {sub.extra.quantile(.25):.1f}; pct extra<-3 {(sub.extra<-3).mean()*100:.0f}%; <-5 {(sub.extra<-5).mean()*100:.0f}%; <-10 {(sub.extra<-10).mean()*100:.0f}%; <-20 {(sub.extra<-20).mean()*100:.0f}%; median days sig->trough {sub.d_sig_trough.median()}; pct trough within 5 sessions {(sub.d_sig_trough<=5).mean()*100:.0f}%; pct >20 sessions {(sub.d_sig_trough>20).mean()*100:.0f}%")
print(allp[pd.to_datetime(allp.signal)>='2016-01-01'][['signal','R','extra','d_sig_trough','trough']].round(1).to_string())
