from datetime import datetime
import pandas as pd

startdate = '2019-01-01'
enddate = '2019-12-31'
holiday = ['01-01', '05-01']

datalist = list(pd.date_range(start=startdate, end=enddate))
df = pd.DataFrame({'date':datalist})

df['month'] = df['date'].apply(lambda x: x.month) 
df['day'] = df['date'].apply(lambda x: x.day) 
df['weekday'] = df['date'].apply(lambda x: x.weekday()+1)

#工作日与休息日
isrest = ((df['weekday'] == 6) | (df['weekday'] == 7))  
df['label'] = isrest*1
#节假日
for h in holiday:
	print(h)
    #h = '01-01'
    h_month,h_day = h.split('-')
    h_index = ((df['month'] == int(h_month)) & (df['day'] == int(h_day)))
    df.loc[h_index, 'label'] = 2