import args as args
import pandas as pd
import datetime_helpers as dth
from datetime_helpers import datetime
import numpy
__author__ = 'abr314'


def return_day_chart(df=pd.DataFrame, dto=dth.datetime.date):

    """
    Takes the original data frame and any day and returns for the day
    :param df: Original data frame loaded from .txt or .csv
    :param dto: The chosen Pandas datetime object day
    :return: Chart corresponding to the chosen dto
    """

    try:
        date_string = dth.genDateString(dto)
        day_chart = df[df.Date.isin([date_string])]
        return day_chart
    except IndexError as e:
        print('Error: ' + e)


def return_days_in_range(df=pd.DataFrame, starting_minute=datetime.datetime.minute,
                         ending_minute=datetime.datetime.minute):

    """

    :param df: Master data frame
    :param starting_minute: user-selected start date
    :param ending_minute: user-selected end date
    :return: dataframe containing all of the individual day charts
    """
    rng = pd.date_range(starting_minute, ending_minute)
  #  print rng
    s = rng.to_series()
    new_df = []

    for i in s:
        date_string = dth.genDateString(s[i])
        day_chart = df[df.Date.isin([date_string])]
        new_df.append(day_chart)

    x = pd.concat(new_df)

    return x


def return_minutes_in_range(df=pd.DataFrame, starting_minute=datetime.datetime,
                            ending_minute=datetime.datetime):
    """

    :param df: takes a dataframe, can be narrowed
    :param starting_minute:
    :param ending_minute:
    :return: dataframe with correct minutes
    """

    new_df = []

    for index, row in df.iterrows():
        d = str(row['Date']) + str(row[' Time'])
        s = pd.to_datetime(d, infer_datetime_format=True)

        if starting_minute < s < ending_minute:
            new_df.append(row)

    x = pd.concat(new_df)
    return x


def add_indicator_to_chart(df=pd.DataFrame, column=str, indicator_name=str, *args):

    """
    Takes a dataframe, column name, indicator name and an arbitrary list
    of parameters for various indicators.

    :param df: The chart to add the indicator to
    :param column: The column to enter into the indicator
    :param args: Optional additional arguments which may be required by the indicator
    :param indicator_name: The name of the indicator

    :return: chart now with an indicator attached
    """

    sma = df[indicator_name] = pd.stats.moments.rolling_mean(df[' High'], 30)
    df[indicator_name] = sma
    return df

'''
Panda Series Crossovers for Signals
'''


def return_day_stats(df=pd.DataFrame):
    """
    Returns stats for the selected datachart
    :param df:

    :return:
    """

    maxi = df[' High'].nlargest(1, 'first')
    mini = df[' Low'].nsmallest(1, 'first')
    volume_sum = df[' Volume'].sum()

    x = {'High': maxi, 'Low': mini, 'Total Volume': volume_sum}
    return x



