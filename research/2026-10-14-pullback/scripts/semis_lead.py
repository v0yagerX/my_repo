import pandas as pd, numpy as np, os
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data'
def load(s):
    f=os.path.join(D,s.replace('^','_')+'.csv')
    df=pd.read_csv(f,parse_dates=['date']).set_index('date').sort_index()
    df=df[~df.index.duplicated(keep='last')]
    return df
groups={
 'ETFs/Index':['SOXX','SMH','^SOX','QQQ','XLK','SPY','RSP'],
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
        df=load(s); c=df['close']
        last=c.iloc[-1]; ld=c.index[-1]
        def at(d):
            return c.loc[:d].iloc[-1]
        r=lambda base: (last/base-1)*100
        ytdbase=c.loc[:'2025-12-31'].iloc[-1]
        hi52=c.iloc[-252:].max(); hid=c.iloc[-252:].idxmax()
        # Jun22 to Jul/Aug low: min close Jun22..Aug31
        seg=c.loc['2026-06-22':'2026-08-31']
        lowJA=seg.min(); lowd=seg.idxmin()
        # Sep-Oct rally high (Sep1..Oct14)
        seg2=c.loc['2026-09-01':]
        hiSO=seg2.max(); hiSOd=seg2.idxmax()
        rows.append(dict(group=g,sym=s,last=round(last,2),
          jun22=r(at('2026-06-22')),oct6=r(at('2026-10-06')),oct8=r(at('2026-10-08')),
          w1=r(c.iloc[-6]),m1=r(c.iloc[-22]),m3=r(c.iloc[-64]),ytd=r(ytdbase),
          dd52=(last/hi52-1)*100,hi52d=hid.date(),
          JunAugLow=(lowJA/at('2026-06-22')-1)*100, lowd=lowd.date(),
          vsSepOctHi=(last/hiSO-1)*100, hiSOd=hiSOd.date(),
          vsLowJA=(last/lowJA-1)*100,
          vs50=(last/c.iloc[-50:].mean()-1)*100, vs200=(last/c.iloc[-200:].mean()-1)*100 if len(c)>=200 else np.nan))
T=pd.DataFrame(rows)
pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
print(T.round(1).to_string(index=False))
T.to_csv('/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/analysis/semis_leadership_returns.csv',index=False)
# group medians
num=['jun22','oct6','oct8','w1','m1','m3','ytd','dd52','vsLowJA','vs50','vs200']
print(T.groupby('group',sort=False)[num].median().round(1).to_string())
# check dates exist
c=load('SOXX')['close']; print(c.loc['2026-06-19':'2026-06-24']); print(c.index[-22],c.index[-64],c.index[-6])
