import pandas as pd, numpy as np
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/'
sox=pd.read_csv(D+'analysis/sent/long/_SOX.csv',parse_dates=['date']).set_index('date')
c=sox['close']
print('SOX long range',c.index[0].date(),c.index[-1].date(),len(c))

# 1) Swing pullbacks from a rolling 60-session closing high: episodes that reached -11.9% (current SOXX swing DD)
def swing_episodes(c,thr=0.08,win=60):
    # define episodes: start at a close that is the max of prior `win` sessions; end when price exceeds that high
    out=[]; i=0; n=len(c); vals=c.values; idx=c.index
    while i<n-1:
        # find a local high: max over trailing window
        hi=vals[i]; hi_i=i
        j=i+1; trough=hi; trough_i=i
        while j<n and vals[j]<=hi:
            if vals[j]<trough: trough=vals[j]; trough_i=j
            j+=1
        dd=trough/hi-1
        if dd<=-thr:
            out.append(dict(peak=idx[hi_i].date(),peak_px=hi,trough=idx[trough_i].date(),trough_px=trough,dd=dd*100,days=trough_i-hi_i,recovered=(j<n)))
        i=j if j>i else i+1
    return pd.DataFrame(out)
# That definition is ATH-to-ATH on the running max; instead use swing highs = rolling-60 highs not exceeded for next k days
def swing_from_local_high(c,look=60,thr=0.119):
    vals=c.values; idx=c.index; n=len(vals); res=[]
    rollmax=c.rolling(look,min_periods=20).max()
    # signal: first day DD from 60d rolling closing high <= -thr ; de-cluster: next signal only after price makes a new 60d high
    armed=True
    for t in range(look,n):
        hi=rollmax.iloc[t]
        dd=vals[t]/hi-1
        if armed and dd<=-thr:
            hi_i=int(np.argmax(vals[t-look+1:t+1]))+t-look+1
            # forward: until close exceeds hi (recovery) or 250 sessions
            fw=vals[t:min(n,t+250)]
            rec=np.where(fw>hi)[0]
            end=rec[0] if len(rec) else len(fw)
            seg=fw[:end] if end>0 else fw[:1]
            tmin=int(np.argmin(seg)); mn=seg[tmin]
            res.append(dict(peak=idx[hi_i].date(),hi=hi,signal=idx[t].date(),sig_px=vals[t],final_dd=(mn/hi-1)*100,extra=(mn/vals[t]-1)*100,days_peak_to_trough=(t+tmin)-hi_i,days_signal_to_trough=tmin,trough=idx[t+tmin].date(),ath_dd_at_peak=(hi/c.iloc[:hi_i+1].max()-1)*100))
            armed=False
        if not armed and vals[t]>=hi*0.999 and t>0 and vals[t]==c.iloc[max(0,t-look+1):t+1].max():
            armed=True
    return pd.DataFrame(res)
r=swing_from_local_high(c)
pd.set_option('display.width',250); pd.set_option('display.max_rows',500)
for lab,sub in [('SOX since 2023-10',r[pd.to_datetime(r.signal)>='2023-10-01']),('SOX since 2021-10',r[pd.to_datetime(r.signal)>='2021-10-01']),('SOX all 1994-',r)]:
    s=sub.iloc[:-1] if str(sub.signal.iloc[-1])>='2026-10-01' else sub
    print('\n==',lab,'n=',len(s),'(excl current)')
    print(s[['peak','signal','trough','final_dd','extra','days_peak_to_trough','days_signal_to_trough','ath_dd_at_peak']].round(1).to_string())
    print('median final_dd',round(s.final_dd.median(),1),'median extra',round(s.extra.median(),1),'pct extra worse than -5%:',round((s.extra<-5).mean()*100),'pct extra worse than -10%:',round((s.extra<-10).mean()*100),'median days signal->trough',s.days_signal_to_trough.median(),'median peak->trough',s.days_peak_to_trough.median())
    # conditional on the swing high being a LOWER HIGH (peak >=10% below ATH)
    lh=s[s.ath_dd_at_peak<=-10]
    print('  subset: swing high >=10% below ATH (lower-high rallies) n=',len(lh),'median final',round(lh.final_dd.median(),1),'median extra',round(lh.extra.median(),1),'pct extra<-5:',round((lh.extra<-5).mean()*100) if len(lh) else None,'pct extra<-10:',round((lh.extra<-10).mean()*100) if len(lh) else None, 'median days sig->trough',lh.days_signal_to_trough.median())
    print(lh[['peak','signal','trough','final_dd','extra','days_signal_to_trough','ath_dd_at_peak']].round(1).to_string())
