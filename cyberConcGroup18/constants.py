#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém


# This module records the constants used throughout this application.


# Header related constants:
# Number of the line where the first expert appears.
EXPERT_START_LINE = 7

# Number of the line where the first client appears.
CLIENT_START_LINE = 7


# Lists constants:
# Position of the header in a list containing the experts, clients or
# schedules.
HEADER_INDEX = 0


# HEADER INDEXES:
# Index of the header date in the header tuple.
HEADER_DATE_INDEX = 0

# Index of the header time in the header tuple.
HEADER_TIME_INDEX = 1

# Index of the header company in the header tuple.
HEADER_COMPANY_INDEX = 2

# Index of the header scope in the header tuple.
HEADER_SCOPE_INDEX = 3


# Time related Constants:

# Number of months in a year.
MONTHS_PER_YEAR = 12

# number of days in a month.
DAYS_PER_MONTH = 30

# number of hours in a day.
HOUR_PER_DAY = 24

# number of minutes in a hour.
MINUTES_PER_HOUR = 60


# Interval of work hours
# hour at which experts start to work.
WORK_START_HOUR = 8

# hour at which experts stop working.
WORK_END_HOUR = 20


# Indexes in Time and Date tuples:

# index of hour in a time tuple
HOUR = 0

# index of minutes in a time tuple
MINUTE = 1

# index of year in a date tuple
YEAR = 0


# index of month in a date tuple
MONTH = 1

# index of days in a date tuple
DAY = 2

# Dictionary Keys - Experts

# Key for the expert name.
E_KEY_NAME = "name"

# Key for the expert work location.
E_KEY_LOCATION = "location"

# Key for the expert specialties domains.
E_KEY_SPECIALITIES_LIST = "specialty"

# Key for the reviews given to experts.
E_KEY_REVIEW = "review"

# Key for the price an expert charge per hour (expert cost/hour).
E_KEY_COST = "cost"

# Key for the date in which the expert finishes his last request.
E_KEY_DATE = "date"

# Key for the time at which the last request they attended finishes.
E_KEY_TIME = "time"

# Key for the accumulated money by the expert.
E_KEY_TOTAL_MONEY = "total money"


# Dictionary Keys - Clients

# Key for the client name
C_KEY_NAME = "name"

# Key for the location of the requested service (defined by the client)
C_KEY_LOCATION = "location"

# Key for the requested start date.
C_KEY_DATE = "date"

# Key for the requested start time.
C_KEY_TIME = "time"

# Key for how much the client wants to pay an expert.
C_KEY_PAYMENT = "max payment"

# Key for the minimum review rate an expert must have to be hired by the
# client.
C_KEY_REVIEW = "review"

# Key for the specialty desired by the client.
C_KEY_SPECIALITY = "specialty"

# Key for how long a client wants to hire an expert.
C_KEY_PERIOD = "period"


# Dictionary Keys - Schedule

# Key for the begin date of the request.
S_KEY_DATE = "begin date"

# Key for the begin time of the request.
S_KEY_TIME = "begin time"

# Key for the client who made the request.
S_KEY_CLIENT_NAME = "client name"

# Key for the expert that will answer the request.
S_KEY_EXPERT_NAME = "expert name"

# Key for the status of a request.
S_KEY_IS_DECLINED = "is declined"
