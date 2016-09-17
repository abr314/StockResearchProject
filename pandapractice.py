import pandas as pd
import urllib2
import datetime
import strings
import pandas.io.data as web
import matplotlib as mp
import numpy as np
import matplotlib.pyplot as plt
import datetime_helpers
import dataframe_helpers
#import statsmodels.api as sm

from pandas.tseries.offsets import Week, FY5253, BDay, BMonthBegin

start_day = 16
start_month = 3
start_year = 2016
start_hour = 10
start_minute = 6
start_second = 4

end_day = 19
end_month = 7
end_year = 2016
end_hour = 10
end_minute = 6
end_second = 4


day = 15
month = 6
year = 2016
days_back = 5
minutes_back = 5
current_minute = 30

df = pd.read_csv('CL.20160900.CME_NY.txt')

dto = datetime_helpers.createDateTimeObjectFromInts(year, month, day)
daychart = dataframe_helpers.return_day_chart(df, dto)
prev_dto = datetime_helpers.dayPreviousTradingDaysBackFrom(dto, days_back)
prev_daychart = dataframe_helpers.return_day_chart(df, prev_dto)

dto_for_minutes = datetime.datetime(dto.year, dto.month, dto.day, minute=current_minute)
mins = datetime_helpers.returnMinutesBack(dto_for_minutes, minutes_back)

start_minute_dto = datetime.datetime(start_year, start_month, start_day, hour=start_hour,
                                     minute=current_minute, second=start_second)

end_minute_dto = datetime.datetime(end_year, end_month, end_day, hour= end_hour, minute=end_minute,
                                   second=end_second)
#z = dataframe_helpers.return_all_minutes_since(df, start_minute_dto, end_minute_dto)


#print(x)
'''
'''

#get day

day_chart = dataframe_helpers.return_day_chart(df, start_minute_dto)
#get day to compare
other_day_chart = dataframe_helpers.return_day_chart(df, end_minute_dto)
#get stats of first day
day_chart_stats_l = dataframe_helpers.return_day_stats(day_chart)
#get stats of second day
other_day_chart_stats = dataframe_helpers.return_day_stats(other_day_chart)

aa = dataframe_helpers.attach_stats_from_day(dto,other_day_chart,day_chart_stats_l)
stats_for_day_range = dataframe_helpers.return_stats_for_days(df, start_minute_dto,end_minute_dto)


yes = 0
no = 0
for i in stats_for_day_range:

    if i['High'].sum() > i['Prev. High'].sum():
        yes += 1
    else:
        no += 1



    #print type(i['High'].values)


print(yes)
print(no)









