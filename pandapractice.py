import pandas as pd
import urllib2
import datetime

import pandas.io.data as web
import matplotlib as mp
import numpy as np
import matplotlib.pyplot as plt
import datetime_helpers
import dataframe_helpers
#import statsmodels.api as sm

from pandas.tseries.offsets import Week, FY5253, BDay, BMonthBegin

start_day = 15
start_month = 5
start_year = 2016
start_hour = 10
start_minute = 6
start_second = 4

end_day = 15
end_month = 6
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

day_chart_stats = dataframe_helpers.return_day_stats(daychart)

day_chart_stats[str(prev_dto)] = dataframe_helpers.return_day_stats(prev_daychart)
#print(day_chart_stats)

dto_for_minutes = datetime.datetime(dto.year, dto.month, dto.day, minute=current_minute)
mins = datetime_helpers.returnMinutesBack(dto_for_minutes, minutes_back)

start_minute_dto = datetime.datetime(start_year, start_month, start_day, hour=start_hour,
                                     minute=current_minute, second=start_second)

end_minute_dto = datetime.datetime(end_year, end_month, end_day, hour= end_hour, minute=end_minute,
                                   second=end_second)
#z = dataframe_helpers.return_all_minutes_since(df, start_minute_dto, end_minute_dto)

x = dataframe_helpers.return_days_in_range(df,start_minute_dto,end_minute_dto)
h = dataframe_helpers.return_minutes_in_range(x,start_minute_dto,end_minute_dto)
#print(x)






