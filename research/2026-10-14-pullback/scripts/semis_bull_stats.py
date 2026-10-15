import pandas as pd, numpy as np
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data/'
def load(s):
    df=pd.read_csv(D+s+'.csv',parse_dates=['date']).set_index('date')
    return df
for sym in ['SOXX','SMH']:
    df=load(sym); c=df['close']; lo=df['low']
    sma200=c.rolling(200).mean(); sma200_slope=sma200/sma200.shift(20)-1
    # zigzag on closes, threshold 8%
    th=0.08
    piv=[]; mode=None; hi_i=0; lo_i=0
    vals=c.values; idx=c.index
    ext_i=0; trend=0  # 1 up, -1 down
    last_hi=0; last_lo=0
    for i in range(1,len(vals)):
        if trend>=0:
            if vals[i]>vals[last_hi]: last_hi=i
            if vals[i]<=vals[last_hi]*(1-th):
                if trend==1 or trend==0: piv.append(('H',last_hi)); 
                trend=-1; last_lo=i
        else:
            if vals[i]<vals[last_lo]: last_lo=i
            if vals[i]>=vals[last_lo]*(1+th):
                piv.append(('L',last_lo)); trend=1; last_hi=i
    print(f'\n=== {sym} zigzag 8% down legs (close basis), since {idx[0].date()} ===')
    print('peak_date peak trough_date trough depth% sessions above200@peak slope200@peak  fastest_hit_-11.9%_in_sessions')
    rows=[]
    for k in range(len(piv)-1):
        if piv[k][0]=='H' and piv[k+1][0]=='L':
            h=piv[k][1]; l=piv[k+1][1]
            depth=vals[l]/vals[h]-1
            above=vals[h]>sma200.iloc[h] if not np.isnan(sma200.iloc[h]) else None
            sl=sma200_slope.iloc[h]
            # sessions to first reach -11.9%
            seg=vals[h:l+1]/vals[h]-1
            hit=np.where(seg<=-0.119)[0]
            hit_s=int(hit[0]) if len(hit) else None
            rows.append((idx[h].date(),round(vals[h],2),idx[l].date(),round(vals[l],2),round(depth*100,1),l-h,above,None if np.isnan(sl) else round(sl*100,2),hit_s))
    for r in rows: print(*r)
    # current leg
    print('last pivot:',piv[-1][0],idx[piv[-1][1]].date(),round(vals[piv[-1][1]],2))
    r=pd.DataFrame(rows,columns=['pk','pkv','tr','trv','depth','n','above200','slope200','hit119'])
    big=r[r.depth<=-11.9]
    print('legs reaching -11.9%:',len(big),'median depth',big.depth.median(),'depths',list(big.depth))
    up=big[(big.above200==True)]
    print('  of which peak above 200d:',len(up),'depths',list(up.depth),'sessions',list(up.n))
    # fast declines: 7-session return <= -10% while above rising 200d
    r7=c/c.shift(7)-1
    cond=(r7<=-0.10)&(c>sma200)&(sma200_slope>0)
    sig=[]; last=None
    for d in c.index[cond]:
        if last is None or (c.index.get_loc(d)-c.index.get_loc(last))>15:
            sig.append(d)
        last=d if (last is None or (c.index.get_loc(d)-c.index.get_loc(last))>15) else last
    print(f'\n{sym}: 7-session return <=-10% while close>rising 200d (de-clustered 15d): n={len(sig)}')
    out=[]
    for d in sig:
        i=c.index.get_loc(d)
        f=c.iloc[i:i+41]; fl=lo.iloc[i+1:i+41]
        def fw(n):
            return (c.iloc[i+n]/c.iloc[i]-1)*100 if i+n<len(c) else np.nan
        def mae(n):
            seg=c.iloc[i+1:i+n+1]
            return (seg.min()/c.iloc[i]-1)*100 if len(seg)==n else np.nan
        # sessions until min close within 40
        seg=c.iloc[i:i+41]
        tmin=int(np.argmin(seg.values))
        out.append((d.date(),round(c.iloc[i],2),round(r7.iloc[i]*100,1),round(fw(10),1),round(fw(20),1),round(fw(40),1),round(mae(10),1),round(mae(20),1),round(mae(40),1),tmin))
    o=pd.DataFrame(out,columns=['date','close','r7','f10','f20','f40','mae10','mae20','mae40','sess_to_min40'])
    print(o.to_string(index=False))
    print('median:',o[['f10','f20','f40','mae10','mae20','mae40','sess_to_min40']].median().round(1).to_dict())
    # consecutive down closes
    dn=(c.diff()<0).astype(int)
    streak=dn.groupby((dn!=dn.shift()).cumsum()).cumsum()*dn
    print(f'{sym} current down streak: {streak.iloc[-1]}; occurrences of streak>=7 since start:', [d.date() for d in streak.index[(streak==7)]])
    # SMA200 projection assuming flat price
    cc=c.copy()
    for p in [510.0,500.0]:
        ext=pd.concat([c,pd.Series([p]*15,index=pd.bdate_range(c.index[-1]+pd.Timedelta(days=1),periods=15))])
        s2=ext.rolling(200).mean()
        print(sym,'SMA200 if flat at',p,': Oct21',round(s2.iloc[len(c)+4],2),'Oct28',round(s2.iloc[len(c)+9],2),'Nov4',round(s2.iloc[len(c)+14],2))
