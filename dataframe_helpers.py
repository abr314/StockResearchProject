import args as args
import pandas as pd
import datetime_helpers as dth
__author__ = 'abr314'


def return_day_chart(df=pd.DataFrame, dto=dth.datetime.date):

    """
    Takes the original data frame and any day and returns for the day
    :param df:
    :param dto:
    :return:
    """
    date_string = dth.genDateString(dto)
    day_chart = df[df.Date.isin([date_string])]
    return day_chart


def add_indicator_to_chart(df=pd.DataFrame, column=str, indicator=str, *args):

    """
    Takes a dataframe, column name, indicator name and an arbitrary list
    of parameters for various indicators.

    :param args:
    :param df:
    :param column:
    :return:
    """

    sma = df[indicator] = pd.stats.moments.rolling_mean(df[' High'], 30)
    df[indicator] = sma
    return df


def return_day_stats(df=pd.DataFrame):
    """
    Returns stats for the selected datachart
    :param df:

    :return:
    """

    maxi = df[' High'].nlargest(1, 'first')
    mini = df[' Low'].nsmallest(1, 'first')

    x = {'High': maxi, 'Low': mini}
    return x