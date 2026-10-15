import pandas as pd, numpy as np
df=pd.read_pickle('/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/scripts/voldf.pkl')
def episodes(col, thresh):
    s=df[col]; peak=s.cummax(); dd=s/peak-1
    eps=[]; inep=False
    for d,v in dd.items():
        if not inep and v<=-thresh:
            inep=True; start=peak.loc[:d].idxmax() if False else s.loc[:d][s.loc[:d]==peak.loc[d]].index[-1]
        if inep and v==0:
            seg=dd.loc[start:d]; low=seg.idxmin()
            eps.append((start,low,d,seg.min())); inep=False
    if inep:
        seg=dd.loc[start:]; low=seg.idxmin(); eps.append((start,low,None,seg.min()))
    return eps
for col,th in [('spx',0.05),('ndx',0.07),('sox',0.12),('nvda',0.15)]:
    print('====',col,'drawdowns >=',th)
    for st,low,rec,mdd in episodes(col,th):
        w=df.loc[st:low]
        r=df.loc[low]
        print(f"peak {st.date()} low {low.date()} ({(low-st).days}d, {len(w)-1} sess) dd {mdd*100:.1f}% | at low: VIX {r.vix:.2f} VIX3M {r.v3:.2f} ratio {r.ratio:.3f} VVIX {r.vv:.1f} | maxVIX in ep {w.vix.max():.2f} on {w.vix.idxmax().date()} maxRatio {w.ratio.max():.3f} maxVVIX {w.vv.max():.1f} | rec {rec.date() if rec is not None else 'open'}")
