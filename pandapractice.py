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

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)


def abs_diff(x, y):
    return abs(x-y)

df = pd.read_csv('CL.20160900.CME_NY.txt')

dto = datetime_helpers.createDateTimeObject(2016, 3, 17)
daychart = dataframe_helpers.return_day_chart(df, dto)
prev_dto = datetime_helpers.dayPreviousTradingDaysBackFrom(dto, 1)
prev_daychart = dataframe_helpers.return_day_chart(df, dto - BDay())

print(daychart)
print(prev_daychart)
day_chart_stats = dataframe_helpers.return_day_stats(daychart)
print(day_chart_stats)







