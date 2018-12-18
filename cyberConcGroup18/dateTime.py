#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém

# Import project modules
import constants as C



def getDateFromString(date_entry):
    """
    Converts a date string into integer variables representing the year, month and day.
        REQUIRES: date_entry is str, represents a date in the format "yyyy-mm-dd".

        ENSURES: year, month and day, all int and represent the yyyy, mm and dd, respectively.
    """
    date_entry = date_entry.split("-")

    year = int(date_entry[C.YEAR])
    month = int(date_entry[C.MONTH])
    day = int(date_entry[C.DAY])

    return year, month, day


def dateToString(date_tuple):
    """
    Converts a date_tuple to a string.
        REQUIRES: a date_tuple in which the first element is year, int >= 0
                                        the second element is month, 0 < int <= 12
                                        the third element is day, 0 < day <= 30

        ENSURES: a str representing the year (y), month (m) and day (d) specified in the format "yyyy-mm-dd"
    """

    year = date_tuple[C.YEAR]

    month = date_tuple[C.MONTH]

    day = date_tuple[C.DAY]

    if month < 10 and day < 10:
        month = "0" + str(month)
        day = "0" + str(day)
    elif month < 10:
        month = "0" + str(month)
    elif day < 10:
        day = "0" + str(day)

    return str(year) + "-" + str(month) + "-" + str(day)


def getTimeFromString(time_entry, delimiter=":"):
    """
    Converts a time string into integer variables representing the hours and minutes.
        REQUIRES: time_entry is str, represents a time in the format "hh:mm".

        ENSURES: hour and minute are int and represent the hh and mm in the time entry.
        """

    time = time_entry.split(delimiter)

    hour = int(time[C.HOUR])
    minute = int(time[C.MINUTE])

    return (hour, minute)


def timeToString(time_tuple):
    """
       Converts a time_tuple to a string.
           REQUIRES: a time_tuple in which the first element is hour, 0 <= int < 24
                                           the second element is minute, 0 < int < 60

           ENSURES: a str representing the hour (hh) and minute (mm) specified in the format "hh:mm"
       """

    hour = (time_tuple[C.HOUR])
    minute = (time_tuple[C.MINUTE])

    if 0 <= hour <= 9 and 0 <= minute <= 9:
        hour = "0" + str(hour)
        minute = "0" + str(minute)

    elif 0 <= hour <= 9:
        hour = "0" + str(hour)

    elif 0 <= minute <= 9:
        minute = "0" + str(minute)

    time_string = str(hour) + ":" + str(minute)

    return time_string


def addPeriodToTime(time, period_in_hours, period_in_minutes, time_delimiter=":"):
    """
    Adds period_in_hours and period_in_minutes to time.
        REQUIRES: time is str, represents time in the format "hh:mm".
                  period_in_hours, is int >= 0
                  period_in_minutes, is int >= 0
                  time_delimiter is str and represents the delimiter between hh and mm in time.

        ENSURES: a str with the updated time (with the added periods) in the format "hh:mm"
            an int >= 0, days_to_add that represent the number of days to be added to a date.
    """

    hour, minute = getTimeFromString(time, time_delimiter)

    summed_hours = hour + period_in_hours
    hour_to_minutes = summed_hours * C.MINUTES_PER_HOUR

    new_time = hour_to_minutes + minute + period_in_minutes

    minutes_to_hour = new_time // C.MINUTES_PER_HOUR
    minutes = new_time % C.MINUTES_PER_HOUR

    # default number of days to add
    days_to_add = 0

    if minutes_to_hour >= C.HOUR_PER_DAY:
        days_to_add = minutes_to_hour // C.HOUR_PER_DAY

    time_tuple = (minutes_to_hour, minutes)

    return timeToString(time_tuple), days_to_add


def addDaysToDate(date_string, number_of_days_to_add):
    """
    Adds a number of days to a date.
        REQUIRES: date_string is a str, representing a date in the format "yyyy-mm-dd"
            number_of_days_to_add is int >= 0

        ENSURES: a str representing an updated date (as result of the addition of a specified
            number of days.

    >>> addDaysToDate("2018-11-1", 1)
    '2018-11-02'
    >>> addDaysToDate("2018-11-30", 30)
    '2018-12-30'
    >>> addDaysToDate("2018-11-30", 29)
    '2018-12-29'
    >>> addDaysToDate("2018-11-30", 1)
    '2018-12-01'
    >>> addDaysToDate("2018-11-29", 1)
    '2019-11-30'
    >>> addDaysToDate("2018-11-29", 722)
    '2020-12-01'
    >>> addDaysToDate("2018-04-30", 0)
    '2018-04-30'
    >>> addDaysToDate("2018-10-30", 60)
    '2018-12-30'
    """
    year, month, day = getDateFromString(date_string)

    year_in_days = year * C.MONTHS_PER_YEAR * C.DAYS_PER_MONTH
    month_in_days = month * C.DAYS_PER_MONTH

    accumulated_days = day + month_in_days + year_in_days + number_of_days_to_add

    updated_year = accumulated_days // (C.DAYS_PER_MONTH * C.MONTHS_PER_YEAR)
    updated_month = (accumulated_days % (C.DAYS_PER_MONTH * C.MONTHS_PER_YEAR)) // (C.DAYS_PER_MONTH)
    updated_day = (accumulated_days % (C.DAYS_PER_MONTH * C.MONTHS_PER_YEAR)) % (C.DAYS_PER_MONTH)

    if updated_day == 0 and updated_month == 0:
        updated_day = C.DAYS_PER_MONTH
        updated_month = C.MONTHS_PER_YEAR - 1
    else:
        if updated_day == 0:
            updated_day = C.DAYS_PER_MONTH
            updated_month = updated_month - 1

        if updated_month == 0:
            updated_month = C.MONTHS_PER_YEAR
            updated_year = updated_year - 1

    date_tuple = (updated_year, updated_month, updated_day)

    return dateToString(date_tuple)


def intDateTimeToString(int_value):
    """
    Receives an integer value and converts it into string.
        REQUIRES: int_value > 0 corresponding to a date or a time number.

        ENSURES: a st with the given number. If 0 <= int_value <= 9,
                 returns a str that results of the concatenation of 0 (zero) and the number.
        """

    str_value = str(int_value)
    if 0 <= int_value <= 9:
        str_value = "0" + str_value

    return str_value


def selectMostRecentDateTime(date1, time1, date2, time2):
    """
    Compares two date/time pairs and retrieves the most recent pair.
        REQUIRES: two pairs of date-time, date1-time1 and date2-time2.
                  date1 and date2, each a str representing date in the format "yyyy-mm-dd".
                  time1 and time2, each a str representing time in the format "hh:mm"

        ENSURES: the date-time pair, each a str, that represents the most recent date and time.

    >>> selectMostRecentDateTime("2018-10-03", "08:00", "2018-10-03", "08:01")
    ('2018-10-03', '08:01')

    >>> selectMostRecentDateTime("2018-10-03", "08:00", "2018-10-02", "08:00")
    ('2018-10-03', '08:00')
    """

    year1, month1, day1 = getDateFromString(date1)
    year2, month2, day2 = getDateFromString(date2)

    if (year1 == year2 and month1 == month2 and day1 == day2):
        # since the date is equal, we could also return date2
        return date1, selectMostRecentTime(time1, time2)

    elif (year1 > year2):
        return date1, time1

    elif (year1 < year2):
        return date2, time2

    elif (year1 == year2 and month1 > month2):
        return date1, time1

    elif (year1 == year2 and month1 < month2):
        return date2, time2

    elif (year1 == year2 and month1 == month2 and day1 > day2):
        return date1, time1

    elif (year1 == year2 and month1 == month2 and day1 < day2):
        return date2, time2


def selectMostRecentTime(time1, time2):
    """
    Compare two times and retrieves the most recent.
        REQUIRES: time1 and time2, each a str in the format "hh:mm"

        ENSURES: the most recent time in the format "hh:mm"
        """

    hour1, minute1 = getTimeFromString(time1)
    hour2, minute2 = getTimeFromString(time2)

    if (hour1 == hour2 and minute1 == minute2):
        return time1  # since they are equal, it could be time2 too.

    elif (hour1 > hour2):
        return time1

    elif (hour1 < hour2):
        return time2

    elif (hour1 == hour2 and minute1 > minute2):
        return time1
    else:
        return time2


def updateDateTime(date_str, time_str, period_in_hour, period_in_minute, delimiter=":"):
    """
    Adds period_in_hour and period_in_minutes to time_str and updates the date_str if necessary.
        REQUIRES: date_str, a str representing a date in the format "yyyy-mm-dd"
                  time_str, a str representing a time in the format "hh:mm"
                  period_in_hour, an int >= 0
                  period_in_minute, an int >= 0
                  delimiter that separates hours from minutes in the time_str

        ENSURES: the return of updated date and time str in the format "yyyy-mm-dd" and "hh:mm", respectively.
        """

    updated_time, number_of_days_to_add = addPeriodToTime(time_str, period_in_hour, period_in_minute, delimiter)

    updated_date = addDaysToDate(date_str, number_of_days_to_add)

    return updated_date, updated_time


if __name__ == "__main__":
    import doctest
    doctest.testmod()
