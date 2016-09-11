import args as args
import pandas as pd
import datetime_helpers as dth
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


def return_all_days_since(df=pd.DataFrame, dto=dth.datetime.date, days=int):

    """

    :param df: Takes the original data frame
    :param dto: Reference datetime object
    :param days: Days to count back, skips non-business days
    :return: array with all of the days charts
    """
    rng = pd.date_range(dth.dayPreviousTradingDaysBackFrom(dto, days), dto)

    s = rng.to_series()
    new_df = []

    for i in s:

        date_string = dth.genDateString(s[i])
        day_chart = df[df.Date.isin([date_string])]
        new_df.append(day_chart)

    print(new_df)

def earliest_date_from_chart(df=pd.DataFrame):
    print(df['Date'].min())
    x = dth.createDateTimeObjectFromStringWithSlash(df['Date'].min())
    return x


def latest_date_from_chart(df=pd.DataFrame):
    print(df['Date'].max())
    x = dth.createDateTimeObjectFromStringWithSlash(df['Date'].max())
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