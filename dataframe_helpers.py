import pandas as pd
from pandas.tseries.offsets import BDay

import datetime_helpers as dth
from datetime_helpers import datetime
import strings
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


def return_days_in_range(df=pd.DataFrame, starting_minute=datetime.datetime,
                         ending_minute=datetime.datetime):

    """

    :param df: Master data frame
    :param starting_minute: user-selected start date
    :param ending_minute: user-selected end date
    :return: dataframe containing all of the individual day charts
    """
    rng = pd.date_range(starting_minute, ending_minute)

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


def return_day_stats(df=pd.DataFrame, *mmm):
    """
    Returns stats for the selected datachart
    :param df:

    :return:
    """

    maxi = df[strings.Categories.high].nlargest(1, 'first')
    mini = df[strings.Categories.low].nsmallest(1, 'first')
    close = df[' Close'].mean()
    volume_sum = df[strings.Categories.volume].sum()

    x = {'High': maxi, 'Low': mini, 'Close': close, 'Total Volume': volume_sum}
    if mmm:
        x = {"Prev." + ' High': maxi, "Prev." + ' Low': mini, 'Prev.' + ' Close':close, "Prev."+
              ' Total Volume': volume_sum}

    return x


def return_stats_for_days(df=pd.DataFrame, starting_minute=datetime.datetime,
                         ending_minute=datetime.datetime):
    """

    :param df:
    :param starting_minute:
    :param ending_minute:
    :return:
    """

    all_days = return_days_in_range(df, starting_minute, ending_minute)
    new_list = []

    new_df = all_days['Date'].unique()

    for i in new_df:

        dto = dth.createDateTimeObjectFromStringWithSlash(i)

        current_day = datetime.datetime(dto.year,dto.month,dto.day)

        previous_day = (current_day - BDay() * 1)

        h = return_day_chart(df,dto)
        z = return_day_stats(h)
        q = return_day_chart(df,previous_day)
        qs = return_day_stats(q, "SOMETHING")
        z.update(qs)
        new_list.append(z)

    return new_list


def attach_stats_from_day(dto=datetime.datetime, df=pd.DataFrame, *argse):

    """

    :param argse:
    :return:
    :param df: dataframe you want to attach the stats from
    :param dto: original time
    :param x: should be status from single day chart
    :return: original array with status from previous day
    """

    maxi = df[strings.Categories.high].nlargest(1, 'first')
    mini = df[strings.Categories.low].nsmallest(1, 'first')
    volume_sum = df[strings.Categories.volume].sum()

    x = {str(dto.day) + ' High': maxi, str(dto.day) + ' Low': mini, str(dto.day) +
                            ' Total Volume': volume_sum}
    old_stats = list(argse)

    old_stats.append(x)

    return old_stats


def percent_which_cross_benchmark(df=pd.DataFrame,positive=True,x1=strings.Categories,x2=strings.Categories):
    """

    :param df: dataframe to search over
    :param positive: which direction are we checking for? True = Up, False = Down
    :param x1: first parameter
    :param x2: second parameter
    :return: Float: the percentage of results which fit our criteria
    """

    entries_which_fit_criteria = 0
    entries_which_do_not_fit_criteria = 0

    # first iterate over the days in the df
    # get the stats for each day and previous day
    # compare the stats for the criteria
    # add results to the ints above


