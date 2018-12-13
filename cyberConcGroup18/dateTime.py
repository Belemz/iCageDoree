# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém
# 31955 Inês de Carvalho Fernandes Martins da Silva

import constants as C

def getTimeFromString(time_entry, delimiter = ":"):
    """
    # todo: contract
    :param delimiter: """

    time = time_entry.split(delimiter)

    hour = int(time[0])
    min = int(time[1])

    return (hour, min)

def timeToString(time_tuple):
    """#todo: contract"""

    hour =(time_tuple[0])
    min = (time_tuple [1])

    if 0 <= hour <= 9 and 0 <= min <= 9:
        hour = "0"+ str(hour)
        min = "0"+ str(min)

    elif 0 <= hour <= 9:
        hour = "0" + str(hour)

    elif 0 <= min <=9:
        min = "0" + str(min)



    time_string = str(hour) + ":" + str(min)

    return time_string


def addPeriodToTime(time, period_in_hours, period_in_minutes, time_delimiter = ":"):
    """ # todo: contract
    :param time_delimiter:
    :param period_in_hours:
    """

    hour, minute = getTimeFromString(time, time_delimiter)

    summed_hours = hour + period_in_hours
    hour_to_minutes = summed_hours * C.MIN_PER_HOUR
    new_time = hour_to_minutes + minute + period_in_minutes
    minutes_to_hour = new_time // C.MIN_PER_HOUR
    minutes = new_time % C.MIN_PER_HOUR

    if minutes_to_hour >= 24:
        raise ValueError("Essa hora ultrapassa a meia-noite!!")
        # todo remove this RAISE AND SOLVE THE PROBLEM OF HOURS > 24 h

    time_tuple = (minutes_to_hour, minutes)
    return timeToString(time_tuple)



def addPeriodStringToTime(time, period_string, time_delimiter = ":"):
    """ # todo: contract
    :param time_delimiter:
    :param period_in_hours:
    """
    period_in_hours, period_in_minutes = getTimeFromString(period_string, time_delimiter)

    return addPeriodToTime(time, period_in_hours, period_in_minutes, ":")


def getDateFromString(date_entry):
    """
    # todo: contract

    """
    date_entry = date_entry.split("-")

    year = int(date_entry[0])
    month = int(date_entry[1])
    day = int(date_entry[2])

    return (year, month, day)

def dateToString(date_tuple):
    """#todo: contract"""

    year = date_tuple[0]

    month = date_tuple[1]

    day = date_tuple[2]

    if month < 10 and day < 10:
        month = "0" + str(month)
        day = "0" + str(day)
    elif month < 10:
        month = "0" + str(month)
    elif day < 10:
        day = "0" + str(day)

    return str(year) + "-" + str(month) + "-" + str(day)


def addDaysToDate(date_string, number_of_days_to_add):    # todo RETHINK
    """
    #todo
    """

    year, month, day = getDateFromString(date_string)

    accumulated_day = day + number_of_days_to_add
    accumulated_month = month + (accumulated_day // C.DAYS_PER_MONTH)

    if accumulated_day % C.DAYS_PER_MONTH == 0:
        updated_day = C.DAYS_PER_MONTH
        updated_month = (month % C.DAYS_PER_MONTH) + 1
        accumulated_month = updated_month
    else:
        updated_day = accumulated_day % C.DAYS_PER_MONTH
        updated_month = accumulated_month % C.MONTHS_PER_YEAR
        accumulated_month = updated_month


    if accumulated_month % C.MONTHS_PER_YEAR == 0:
        updated_month = C.MONTHS_PER_YEAR
        updated_year = year
    else:
        updated_year = year + (accumulated_month // C.MONTHS_PER_YEAR)

    date_tuple = (updated_year, updated_month, updated_day)
    return dateToString(date_tuple)


def intDateTimeToString (int_value):
    """ #todo """
    str_value = str(int_value)
    if 0 <= int_value <= 9:
        str_value = "0"+ str_value

    return str_value



def selectMostRecentDateTime (date1, time1, date2, time2):
    """#TODO"""
    year1, month1, day1 = getDateFromString(date1)
    hour1, minute1 = getTimeFromString(time1, )

    year2, month2, day2 = getDateFromString(date2)
    hour2, minute2 = getTimeFromString(time2, )


    if (year1 == year2 and month1 == month2 and day1 == day2):
        return date1, selectMostRecentTime(time1, time2) # since the date is equal, we could also return date2

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
    """Compare two times and retrieves the most recent.
        Requires: one_time, other_time are int
        Ensures: the most recent time"""
    hour1, minute1 = getTimeFromString(time1, )
    hour2, minute2 = getTimeFromString(time2, )


    if (hour1 == hour2 and  minute1 == minute2):
        return time1    # since they are equal, it could be time2 too.

    elif (hour1 > hour2):
        return time1

    elif (hour1 < hour2):
        return time2

    elif (hour1 == hour2 and minute1 > minute2):
        return time1
    else:
        return time2


# def isAfter(one_date, other_date):
#    """Verifies if a certain date occurs after another date."""




#print(getTimeFromString(time_entry="00:00"))
#print(timeToString(getTimeFromString(time_entry="00:00")))

#print(getDateFromString("2018-10-20"))
#print(dateToString(getDateFromString("2018-10-20")))
