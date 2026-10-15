import pandas as pd
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data'
def L(s): return pd.read_csv(f'{D}/{s}.csv',parse_dates=['date']).set_index('date')
for s in ['SOXX','SMH','_SOX','NVDA','QQQ','XLK']:
    df=L(s)
    for a,b in [('2026-07-30','2026-09-30'),('2026-08-01','2026-09-24'),('2026-08-18','2026-09-24')]:
        w=df[a:b]
        print(s,a,b,'closes',round(w.close.min(),2),w.close.idxmin().date(),round(w.close.max(),2),w.close.idxmax().date(),'| intraday',round(w.low.min(),2),w.low.idxmin().date(),round(w.high.max(),2),w.high.idxmax().date())
    w=df['2026-08-01':'2026-09-24']; lo,hi=w.close.min(),w.close.max(); last=df.close.iloc[-1]
    print('   last',round(last,2),'pos in Aug1-Sep24 close range: %.0f%%'%((last-lo)/(hi-lo)*100), ' mid',round((lo+hi)/2,2))
    # first close above range top
    after=df['2026-09-25':]
    above=after[after.close>hi]
    print('   first close above range top:', above.index[0].date() if len(above) else None, ' closes above top count', len(above), ' last close above', above.index[-1].date() if len(above) else None)
    print('   Jun22 close',round(df.close['2026-06-22'],2),' Jul29 low',round(df.low['2026-07-29'],2), 'Jul29 close', round(df.close['2026-07-29'],2))
# weekly closes SOXX since June
for s in ['SOXX','SMH','NVDA']:
    df=L(s); wk=df.close.resample('W-FRI').last()['2026-06-01':]
    print(s,'weekly closes:',', '.join(f"{d.strftime('%m-%d')}:{v:.1f}" for d,v in wk.items()))
# daily SOXX Sep 10 - Oct 14
print(L('SOXX')['2026-09-10':][['open','high','low','close','volume']].round(2).to_string())
