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

df = pd.read_csv('CL.20160900.CME_NY.txt')

dto = datetime_helpers.createDateTimeObjectFromInts(2016, 6, 15)
daychart = dataframe_helpers.return_day_chart(df, dto)
prev_dto = datetime_helpers.dayPreviousTradingDaysBackFrom(dto, 5)
prev_daychart = dataframe_helpers.return_day_chart(df, dto - BDay())

#print(daychart)
#print(prev_daychart)
day_chart_stats = dataframe_helpers.return_day_stats(daychart)
#print(day_chart_stats)
x = dataframe_helpers.return_all_days_since(df, dto, 6)
print(x)







