import pandas as pd, numpy as np, os, json
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data'
def load(s):
    df=pd.read_csv(f'{D}/{s}.csv',parse_dates=['date']).set_index('date')
    return df
groups={
 'ETFs/indices':['SOXX','SMH','_SOX','QQQ','XLK','SPY','RSP'],
 'AI compute':['NVDA','AMD','AVGO','MRVL','ARM','ALAB','CRDO'],
 'Foundry/equipment':['TSM','ASML','AMAT','LRCX','KLAC','TER'],
 'Memory/storage':['MU','SNDK','WDC','STX'],
 'Optics/networking':['LITE','COHR','CIEN','ANET'],
 'Analog/legacy':['TXN','ADI','NXPI','ON','MCHP','INTC','QCOM','MPWR'],
 'AI infra/neoclouds':['ORCL','CRWV','NBIS','DELL','SMCI','VRT','CEG','VST'],
}
rows=[]
for g,syms in groups.items():
    for s in syms:
        df=load(s); c=df['close'].dropna(); h=df['high']
        last=c.index[-1]
        def ret_from(d):
            # close on date d (or last before)
            base=c[:d].iloc[-1]; return (c.iloc[-1]/base-1)*100
        def ret_back(n):
            return (c.iloc[-1]/c.iloc[-1-n]-1)*100
        ytd_base=c[:'2025-12-31'].iloc[-1]
        hi=c['2025-10-14':].max(); hid=c['2025-10-14':].idxmax()
        sma50=c.rolling(50).mean().iloc[-1]; sma200=c.rolling(200).mean().iloc[-1]
        rows.append(dict(group=g,sym=s.replace('_','^'),last=round(c.iloc[-1],2),
            since_jun22=ret_from('2026-06-22'),since_oct6=ret_from('2026-10-06'),since_oct8=ret_from('2026-10-08'),
            r1w=ret_back(5),r1m=ret_back(21),r3m=ret_back(63),ytd=(c.iloc[-1]/ytd_base-1)*100,
            dd_52w=(c.iloc[-1]/hi-1)*100,hi_date=hid.strftime('%Y-%m-%d'),
            vs50=(c.iloc[-1]/sma50-1)*100,vs200=(c.iloc[-1]/sma200-1)*100))
df=pd.DataFrame(rows)
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
print(df.round(1).to_string(index=False))
df.to_csv('/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data/semis_returns_table.csv',index=False)
# group medians
num=['since_jun22','since_oct6','since_oct8','r1w','r1m','r3m','ytd','dd_52w','vs50','vs200']
print(df[df.group!='ETFs/indices'].groupby('group')[num].median().round(1).to_string())
# check base dates exist
c=load('NVDA')['close']; print([d for d in ['2026-06-22','2026-10-06','2026-10-08','2025-12-31'] if pd.Timestamp(d) in c.index])
print(c.index[-1-5], c.index[-1-21], c.index[-1-63])
