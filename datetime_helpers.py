import datetime
import timeit
import pandas as pd
from pandas.tseries.offsets import Minute

__author__ = 'abr314'


def genDateString(x=datetime.date):
    """Generates string from a date"""
    return '' + str(x.year) + '/' + str(x.month) + '/' + str(x.day)


def createDateTimeObjectFromInts(year=int, month=int, day=int):
    """
    Generates pandas datetime object from user input"""
    return datetime.date(year, month, day)

def returnMinutesBack(x=datetime.date, i=int):
    """

    :param x: dto, requires specific minutes
    :return:
    """

    y = x - pd.DateOffset(minutes=i)

    return y

def earliest_date_from_chart(df=pd.DataFrame):
    x = createDateTimeObjectFromStringWithSlash(df['Date'].min())
    return x


def latest_date_from_chart(df=pd.DataFrame):
    print(df['Date'].max())
    x = createDateTimeObjectFromStringWithSlash(df['Date'].max())
    return x


def createDateTimeObjectFromStringWithSlash(string=str):
    """

    :param string:
    :return:
    """

    dt = pd.to_datetime(string, infer_datetime_format=True)
#    timeit.Timer(dt).timeit()
    return dt


def dayPreviousTradingDaysBackFrom(original_date=datetime.date, i=int):
    """

    :param original_date: Starting date
    :param i: Number of trading days to go back. Skips non-business days (needs testing for confirmation)
    :return: The trading day the requested number of days back
    """

    from pandas.tseries.offsets import BDay
    x = original_date - pd.DateOffset(days=i)

    return x