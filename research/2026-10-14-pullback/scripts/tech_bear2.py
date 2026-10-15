import pandas as pd, numpy as np, json
S='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad'
def yj(p):
    j=json.load(open(p))['chart']['result'][0]
    ts=pd.to_datetime(j['timestamp'],unit='s').normalize()
    q=j['indicators']['quote'][0]
    return pd.DataFrame({'close':q['close'],'high':q['high'],'low':q['low'],'volume':q['volume']},index=ts).dropna()
xlk=yj(f'{S}/dl_techbear/XLK.json')['close']; xlk=xlk[~xlk.index.duplicated(keep='last')]
print('XLK long',xlk.index[0].date(),xlk.index[-1].date(),xlk.iloc[-1],xlk.max(),xlk.idxmax().date())
sox=pd.read_csv(f'{S}/analysis/sent/long/_SOX.csv',parse_dates=['date']).set_index('date')['close']
spx=pd.read_csv(f'{S}/analysis/sent/long/_GSPC.csv',parse_dates=['date']).set_index('date')['close']
def episodes(s):
    rm=s.cummax(); dd=s/rm-1; eps=[]; inep=False
    for i,(d,v) in enumerate(dd.items()):
        if v<0 and not inep: inep=True; start=s.index[i-1]
        if inep and v==0:
            seg=dd[start:d]; eps.append((start,seg.idxmin(),seg.min(),d)); inep=False
    if inep: seg=dd[start:]; eps.append((start,seg.idxmin(),seg.min(),None))
    return eps,dd
eps,dd=episodes(xlk)
sox20=sox/sox.rolling(20).max()-1
spxdd=spx/spx.cummax()-1
def cond(thr,extra=None,label=''):
    rows=[]
    for st,tr,depth,end in eps:
        if depth>-thr or end is None: continue
        hit=dd[st:end][dd[st:end]<=-thr].index[0]
        if extra and not extra(hit,st): continue
        rows.append(dict(start=st.date(),hit=hit.date(),trough=tr.date(),depth=round(depth*100,1),days=len(dd[hit:tr])-1))
    df=pd.DataFrame(rows); d=-df.depth
    print(f'{label} XLK given -{thr*100:.2f}%: n={len(df)} median {-d.median():.1f}% | %>=10: {(d>=10).mean()*100:.0f} %>=13: {(d>=13).mean()*100:.0f} %>=15: {(d>=15).mean()*100:.0f} %>=20: {(d>=20).mean()*100:.0f} | med days hit->trough {df.days.median()}')
    return df
a=cond(0.0573,label='1998-')
b=cond(0.0573,extra=lambda h,st: h in sox20.index and sox20[h]<=-0.10,label='SOX>=10% off 20d high')
print(b.to_string())
c=cond(0.0573,extra=lambda h,st: h in spxdd.index and spxdd[h]>-0.025,label='SPX within 2.5% of ATH')
print(c.to_string())
e=cond(0.0573,extra=lambda h,st: st>=pd.Timestamp('2009-01-01'),label='2009-')
print(e.to_string())
