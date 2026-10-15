import pandas as pd, numpy as np, glob, os
S='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad'
D=f'{S}/data'
def ld(s):
    x=pd.read_csv(f'{D}/{s}.csv',parse_dates=['date']).set_index('date'); return x[~x.index.duplicated(keep='last')]
px={s:ld(s) for s in ['QQQ','XLK','SPY','RSP','QQQE','SOXX','AAPL','MSFT','GOOGL','AMZN','META','NVDA','AVGO','TSLA','ORCL','AMD','MU','PLTR','_NDX']}
c=pd.DataFrame({k:v['close'] for k,v in px.items()})
# relative strength ratio peaks
for num,den in [('QQQ','SPY'),('XLK','SPY'),('QQQE','QQQ'),('QQQ','RSP')]:
    r=(c[num]/c[den]).dropna()
    r1=r['2025-10-14':]
    print(f'{num}/{den}: Oct6 {r["2026-10-06"]:.4f}, last {r.iloc[-1]:.4f}, 1y max {r1.max():.4f} on {r1.idxmax().date()}, Oct6 vs max {(r["2026-10-06"]/r1.max()-1)*100:.1f}%, last vs max {(r.iloc[-1]/r1.max()-1)*100:.1f}%, last vs Jul29 {(r.iloc[-1]/r["2026-07-29"]-1)*100:.1f}%')
# distribution days (close down >=0.2% on higher volume than prior day), last 25 sessions
for s in ['QQQ','SPY','XLK']:
    df=px[s]; ch=df.close.pct_change(); vu=df.volume>df.volume.shift(1)
    dist=(ch<=-0.002)&vu
    last25=dist.iloc[-25:]
    print(s,'distribution days last 25 sessions:',int(last25.sum()),list(last25[last25].index.strftime('%m-%d')))
    v50=df.volume.rolling(50).mean()
    print('  vol/50d Oct8 %.2f Oct14 %.2f'%(df.volume['2026-10-08']/v50['2026-10-07'], df.volume['2026-10-14']/v50['2026-10-13']))
# mega caps
print('\nMega-caps: last, %from 52w closing high, vs50d, vs200d, since Oct6, since Jul 29 close, 1-day after July earnings')
for s in ['AAPL','MSFT','NVDA','GOOGL','AMZN','META','AVGO','TSLA','ORCL','AMD','MU','PLTR']:
    x=c[s].dropna(); h=x['2025-10-14':].max(); hd=x['2025-10-14':].idxmax().date()
    s50=x.rolling(50).mean().iloc[-1]; s200=x.rolling(200).mean().iloc[-1]
    print(f'{s:5s} {x.iloc[-1]:8.2f} {((x.iloc[-1]/h)-1)*100:6.1f}% (hi {hd}) vs50 {((x.iloc[-1]/s50)-1)*100:5.1f}% vs200 {((x.iloc[-1]/s200)-1)*100:5.1f}% sinceOct6 {((x.iloc[-1]/x["2026-10-06"])-1)*100:5.1f}% sinceJul29 {((x.iloc[-1]/x["2026-07-29"])-1)*100:5.1f}%')
for s,d in [('MSFT','2026-07-30'),('AMZN','2026-07-31'),('GOOGL','2026-07-23'),('META','2026-07-30')]:
    x=c[s]; i=x.index.get_loc(pd.Timestamp(d))
    print(f'{s} reaction close {d}: {x.iloc[i]:.2f} ({(x.iloc[i]/x.iloc[i-1]-1)*100:.1f}%), last {x.iloc[-1]:.2f} = {(x.iloc[-1]/x.iloc[i]-1)*100:.1f}% vs post-earnings close, vs pre-earnings close {(x.iloc[-1]/x.iloc[i-1]-1)*100:.1f}%')
# Fib of Mar 30 2026 low -> Oct 6 high (intraday)
for s in ['QQQ','XLK']:
    df=px[s]; lo=df.low['2026-03-25':'2026-04-03'].min(); lod=df.low['2026-03-25':'2026-04-03'].idxmin().date(); hi=df.high['2026-10-06']
    print(s,'Mar low',lod,lo,'Oct6 hi',hi, {k: round(hi-(hi-lo)*k,2) for k in [0.236,0.382,0.5,0.618]})
    # 200d projection flat path and bear path
    cl=df.close.copy()
    for label,path in [('flat',None),('-1%/wk drift',None)]:
        pass
    last=cl.iloc[-1]; fut=pd.bdate_range('2026-10-15','2026-12-04')
    flat=pd.concat([cl,pd.Series(last,index=fut)])
    s200=flat.rolling(200).mean()
    print('  200d flat-path: Oct 14 %.2f, Oct 28 %.2f, Nov 6 %.2f, Nov 20 %.2f, Dec 4 %.2f'%(s200['2026-10-14'],s200['2026-10-28'],s200['2026-11-06'],s200['2026-11-20'],s200['2026-12-04']))
    # path down linearly to -9% by Nov 6 then flat
    tgt=last*0.91; n1=len(pd.bdate_range('2026-10-15','2026-11-06'))
    path=list(np.linspace(last,tgt,n1))+[tgt]*(len(fut)-n1)
    bp=pd.concat([cl,pd.Series(path,index=fut)]); s200b=bp.rolling(200).mean(); s50b=bp.rolling(50).mean()
    print('  200d bear-path(-9%% by Nov6): Nov 6 %.2f Nov 20 %.2f'%(s200b['2026-11-06'],s200b['2026-11-20']))
# realized beta in this pullback
r=c[['QQQ','SPY','XLK','RSP']].pct_change()
print('Oct6->Oct14 QQQ %.2f SPY %.2f XLK %.2f RSP %.2f'%tuple(((c.loc['2026-10-14',k]/c.loc['2026-10-06',k])-1)*100 for k in ['QQQ','SPY','XLK','RSP']))
print('6-session beta QQQ/SPY (Oct7-14):', round(np.polyfit(r.SPY['2026-10-07':],r.QQQ['2026-10-07':],1)[0],2))
# QQQ Jul 2024 and Jun-Jul 2026 analog paths: drawdown at session 6, final, sessions
for st,tr in [('2024-07-10','2024-08-07'),('2026-06-02','2026-07-29'),('2025-02-19','2025-04-08'),('2024-12-16','2025-01-14'),('2024-03-22','2024-04-19'),('2025-10-29','2026-03-30')]:
    x=c.QQQ[st:]; dd=x/x.iloc[0]-1
    y=c.RSP[st:]; ddr=y/y.iloc[0]-1
    print(f'QQQ ep {st}: DD at session6 {dd.iloc[6]*100:.1f}%, RSP at s6 {ddr.iloc[6]*100:.1f}%, final {dd[:tr].min()*100:.1f}% on {dd[:tr].idxmin().date()} (session {len(dd[:dd[:tr].idxmin()])-1})')
