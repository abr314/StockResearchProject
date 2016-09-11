import datetime
__author__ = 'abr314'


def genDateString(x=datetime.date):
    """Generates string from a date"""
    return '' + str(x.year) + '/' + str(x.month) + '/' + str(x.day)


def createDateTimeObject(year=int, month=int, day=int):
    """
    Generates pandas datetime object from user input"""
    return datetime.date(year, month, day)


def dayPreviousTradingDaysBackFrom(original_date=datetime.date, i=int):
    """

    :param original_date: Starting date
    :param i: Number of trading days to go back. Skips none business days (needs testing for confirmation)
    :return: The trading day the requested number of days back
    """

    from pandas.tseries.offsets import BDay
    x = original_date - BDay() * i
    return x