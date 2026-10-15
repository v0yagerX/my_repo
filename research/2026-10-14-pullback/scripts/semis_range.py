import pandas as pd, numpy as np, os
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data'
def load(s):
    df=pd.read_csv(os.path.join(D,s.replace('^','_')+'.csv'),parse_dates=['date']).set_index('date').sort_index()
    return df[~df.index.duplicated(keep='last')]
for s in ['SOXX','SMH','^SOX','NVDA','QQQ']:
    df=load(s); c=df.close
    a=df.loc['2026-08-01':'2026-09-16']
    print(f'\n## {s} last {c.iloc[-1]:.2f}')
    print(f' Aug1-Sep16: close range {a.close.min():.2f} ({a.close.idxmin().date()}) - {a.close.max():.2f} ({a.close.idxmax().date()}); intraday {a.low.min():.2f} ({a.low.idxmin().date()}) - {a.high.max():.2f} ({a.high.idxmax().date()})')
    lo,hi=a.close.min(),a.close.max(); mid=(lo+hi)/2
    print(f' position of last close in Aug1-Sep16 close range: {(c.iloc[-1]-lo)/(hi-lo)*100:.0f}% ; midpoint {mid:.2f}')
    b=df.loc['2026-07-29':'2026-07-29']
    print(f' Jul29 low close {b.close.iloc[0]:.2f} intraday low {b.low.iloc[0]:.2f}')
    # first close above Aug1-Sep16 high close
    post=c.loc['2026-09-17':]
    above=post[post>hi]
    print(f' first close above range high: {above.index[0].date() if len(above) else None}; n closes above: {len(above)}; last close above: {above.index[-1].date() if len(above) else None}')
    # Sep-Oct high
    s2=df.loc['2026-09-17':]
    print(f' Sep17-> high close {s2.close.max():.2f} ({s2.close.idxmax().date()}), intraday {s2.high.max():.2f} ({s2.high.idxmax().date()})')
    print(f' Oct14 low {df.low.iloc[-1]:.2f}')
    # Sep 16 close (pre-breakout gap) and gap zone Sep17
    print(' Sep16 close', round(c.loc['2026-09-16'],2), 'Sep17 low', round(df.low.loc['2026-09-17'],2))
    # weekly closes since Jun
    w=c.resample('W-FRI').last().loc['2026-06-01':]
    print(' weekly closes:', ', '.join(f'{d.strftime("%m-%d")}:{v:.1f}' for d,v in w.items()))
    # 200d sma and 50d/100d
    print(f' SMA50 {c.rolling(50).mean().iloc[-1]:.2f} SMA100 {c.rolling(100).mean().iloc[-1]:.2f} SMA200 {c.rolling(200).mean().iloc[-1]:.2f}; SMA50 vs 20d ago {c.rolling(50).mean().iloc[-21]:.2f}')
    # Fib of Jul29 low -> Oct high (close basis)
    L=c.loc['2026-07-29']; H=s2.close.max()
    print(' fib closes (Jul29 low->Sep/Oct high):', {k: round(H-(H-L)*k,2) for k in [0.382,0.5,0.618,0.786]})
