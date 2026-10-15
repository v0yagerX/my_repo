import pandas as pd
D='/tmp/claude-0/-home-user-my-repo/6b8e50df-060f-5f24-bce7-cc2b24216d41/scratchpad/data/'
last=7718.94; ath=7818.93
lv={'Oct2 gap top':7700.51,'Oct2 gap bottom':7684.75,'50d SMA':7707.02,'AVWAP Jul-low':7686.6,'AVWAP Sep-start':7699.44,'3m vol node':7676.57,'38.2% fib':7641.83,'Oct1 swing low':7616.78,'Sep1 swing low':7611.2,'100d SMA':7593.85,'50% fib':7579.22,'Aug-Sep closing low':7551.81,'61.8% fib':7516.61,'Sep16 swing low':7507.77,'Aug intraday low':7504.78,'AVWAP Mar30':7450.03,'78.6% fib':7427.47,'Jul8 low':7421.82,'6m POC':7418.54,'Jul29 low':7313.92,'200d SMA':7263.43,'AVWAP YTD':7252.46,'-10% from ATH close':ath*0.9}
for k,v in lv.items(): print(f'{k:22s} {v:8.2f}  vs close {100*(v/last-1):6.2f}%  vs ATHclose {100*(v/ath-1):6.2f}%')
rl=212.09; rh=222.77
rv={'50d':216.02,'100d':213.99,'6m POC':212.96,'AVWAP Mar30':209.15,'Sep30 close low':208.02,'Jun23 low':207.64,'Oct1 low':207.16,'200d':206.51,'May22 gap top':205.52,'May22 gap bottom':204.9,'AVWAP YTD':204.05,'-10% from high':rh*0.9}
for k,v in rv.items(): print(f'RSP {k:18s} {v:7.2f} vs close {100*(v/rl-1):6.2f}% vs Aug14 high {100*(v/rh-1):6.2f}%')
def ld(s):
    df=pd.read_csv(D+s+'.csv',parse_dates=['date']).drop_duplicates('date',keep='last').set_index('date').sort_index(); return df['close']
de=(ld('XLP')+0)/1
ratio=(ld('XLP')/ld('XLP').loc['2026-08-14']+ld('XLV')/ld('XLV').loc['2026-08-14']+ld('XLU')/ld('XLU').loc['2026-08-14'])/(ld('XLY')/ld('XLY').loc['2026-08-14']+ld('XLI')/ld('XLI').loc['2026-08-14']+ld('XLF')/ld('XLF').loc['2026-08-14'])
print('defensive/cyclical (equal-wt XLP,XLV,XLU vs XLY,XLI,XLF, =1 on Aug14): Oct6',round(ratio.loc['2026-10-06'],4),'last',round(ratio.iloc[-1],4))
for s in ['XLF','XLI','XLY','XLP','XLV','XLU','IWM','MDY']:
    x=ld(s); print(s,'since Aug14',round(100*(x.iloc[-1]/x.loc['2026-08-14']-1),2),'%')
# IWM vs 200d
iwm=ld('IWM'); print('IWM vs 200d', round(100*(iwm.iloc[-1]/iwm.rolling(200).mean().iloc[-1]-1),2), 'IWM from 52w high', round(100*(iwm.iloc[-1]/iwm.iloc[-252:].max()-1),2))
b=pd.read_csv(D+'breadth_timeseries.csv',parse_dates=['date']).set_index('date')
print('first date with pct_above_200d:', b['pct_above_200d'].first_valid_index().date())
