#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém

# Import project modules
import constants as C
import dateTime as DT

directory = "../debug/"

def createFileName(header_tuple):
    """
    Creates a file name based on the information contained in a tuple.
        REQUIRES: a tuple, header_tuple, with 4 elements.
                            The 1st element is date, str in the date format ("yyyy-mm-dd").
                            The 2nd element is time, str in the time format ("hh:mm").
                            The 3rd element is the application company.
                            The 4th element is the scope of the file , str (either "Experts", "Clients" or "Schedule").

        ENSURES: a file name containing the information present in the header_tuple in the following format:
                "AAAAyBBmCCscopeEEhFF.txt", where AAAAyBBmCC and EEhFF represent the date and time in the tuple,
                respectively.
        """

    date, time, _, scope = header_tuple

    year, month, day = DT.getDateFromString(date)
    hour, minute = DT.getTimeFromString(time, )

    processed_scope = scope.strip(":")

    file_name = DT.intDateTimeToString(year) + "y" \
                + DT.intDateTimeToString(month) + "m" \
                + DT.intDateTimeToString(day) \
                + processed_scope.lower() \
                + DT.intDateTimeToString(hour) + "h" \
                + DT.intDateTimeToString(minute) \
                + ".txt"

    return file_name


def updateHeader(header_tuple, scope):
    """
    Updates the header information present in a header_tuple.
        REQUIRES: a tuple,  header.
        Ensures: a tuple with updated time and date."""

    date, time, company, _ = header_tuple  # tuple unpacking   todo is it better to ignore the scope here and give it as a parameter? Or to make a if else statement to control whether we write experts or schedule

    # update time - adding 30 minutes to the current time
    updated_date, updated_time = DT.updateDateTime(date, time, 0, 30, ":")

    return (updated_date, updated_time, company, scope)



def writeHeader(file_out, header_tuple):
    """
    Creates a header containing the day, time, company and scope of a file.
        Requires: param day: is date in the format yyyy-mm-dd,
                  time: is time in the format hh:mm
                  company: is str
                  scope: is string

        Returns: creates a header with each parameter in different lines and preceded (in the line before) with the
                 type of parameter
    """

    day, time, company, scope = header_tuple  # tuple unpacking

    file_out.write("Day:\n")
    file_out.write(day)
    file_out.write("\nTime:\n")
    file_out.write(time)
    file_out.write("\nCompany:\n")
    file_out.write(company)
    file_out.write("\n")
    file_out.write(scope + ":")
    file_out.write("\n")



def writeExpertsFile(file_name, experts_list):
    """
    Creates a file and write the experts in it.
        REQUIRES: file_name, a str that corresponds to the name of the file that will be created.
                  experts_list, a list containing a tuple in the first position (HEADER_INDEX) and dictionaries
                in the remaining positions of the list. The tuple contains the information regarding the header.
                Dictionaries contain the information regarding each expert.

        ENSURES: a file named file_name with the header and the experts updated, both organized as in the
        examples provided (omitted here for the sake of readibility).
    """

    output_file = open(directory + file_name, "w")

    writeHeader(output_file, experts_list[C.HEADER_INDEX])



    for iterator in range(1, len(experts_list)):

        expert = experts_list[iterator]

        expert_str = convertExpertsDictToString(expert)

        output_file.write(expert_str + "\n")

    output_file.close()


def convertExpertsDictToString(experts_dict):
    """
    Converts an expert dictionary into string.
        REQUIRES: a dictionary of experts, containing all the keys mentioned in the module Constants (Name, Location,
            Specialities_list, review, key_cost, date, time and total_money.

        ENSURES: a str as a result of the concatenation of the values from the dictionary, in the same format as in
            the input files.
    """

    experts_str = experts_dict.get(C.E_KEY_NAME) + ", " + \
                    experts_dict.get(C.E_KEY_LOCATION) + ", " + \
                    experts_dict.get(C.E_KEY_SPECIALITIES_LIST) + ", " + \
                    experts_dict.get(C.E_KEY_REVIEW) + ", " + \
                    str(experts_dict.get(C.E_KEY_COST)) + ", " + \
                    experts_dict.get(C.E_KEY_DATE) + ", " + \
                    experts_dict.get(C.E_KEY_TIME) + ", " + \
                    str(experts_dict.get(C.E_KEY_TOTAL_MONEY))

    return experts_str




def writeSchedule(file_name, schedule_list):
    """
    Creates a file and write the schedule for each client in it.
        REQUIRES: file_name, a str that corresponds to the name of the file that will be created.
                  schedule_list, a list containing a tuple in the first position (HEADER_INDEX) and dictionaries
                in the remaining positions of the list. The tuple contains the information regarding the header.
                Dictionaries contain the information regarding each schedule - date, time, client and expert.

        ENSURES: a file named file_name with the header and the schedule updated, both organized as in the
        examples provided (omitted here for the sake of readibility.
    """

    fileOut = open(directory + file_name, "w")

    writeHeader(fileOut, schedule_list[C.HEADER_INDEX])

    for iterator in range(1, len(schedule_list)):

        schedule = schedule_list[iterator]

        schedule_str = convertScheduleDictToString(schedule)

        fileOut.write(schedule_str + "\n")


    fileOut.close()


def convertScheduleDictToString(schedule_dict):
    """
    Converts an expert dictionary into string.
        REQUIRES: a dictionary of schedules, containing all the keys mentioned in the module Constants (begin date, begin
            hour, client_name and expert_name (or "declined", if a client is not assigned with an expert)).

        ENSURES: a str as a result of the concatenation of the values from the dictionary, in the same format as in
            the input files.
        """

    schedule_string = schedule_dict.get(C.S_KEY_DATE) + ", " + \
                      schedule_dict.get(C.S_KEY_TIME) + ", " + \
                      schedule_dict.get(C.S_KEY_CLIENT_NAME) + ", " +\
                      schedule_dict.get(C.S_KEY_EXPERT_NAME)

    return schedule_string