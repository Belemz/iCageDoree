# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém
# 31955 Inês de Carvalho Fernandes Martins da Silva


import constants as C
import dateTime as DT

directory = "../debug/"

def createFileName(header_tuple):
    """
    #todo
    """
    date, time, _, scope = header_tuple

    year, month, day = DT.getDateFromString(date)
    hour, min = DT.getTimeFromString(time, )

    processed_scope = scope.strip(":")

    file_name = DT.intDateTimeToString(year) + "y" \
                + DT.intDateTimeToString(month) + "m" \
                + DT.intDateTimeToString(day) \
                + processed_scope \
                + DT.intDateTimeToString(hour) + "h" \
                + DT.intDateTimeToString(min) \
                + ".txt"

    return file_name

def updateHeader(headerTuple, scope):
    """Updates the date and time fields of a header.
        Requires: a tuple with the header.
        Ensures: a tuple with updated time and date."""

    date, time, company, _ = headerTuple  # tuple unpacking   todo is it better to ignore the scope here and give it as a parameter? Or to make a if else statement to control whether we write experts or schedule

    # update time
    updated_time = DT.addPeriodToTime(time, 0, 30, ":")  # adding 30 minutes to the current time


    #update date
    # todo add the conditional that allows you to know how many days to add.- ask if this is required

    # updated_date = DT.addDaysToDate(date, 0)
    # date_str = DT.dateToString(updated_date)
    updated_date = date   # todo REMOVER

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


def writeExpertsFile(file_name, content):
    """
    # todo
    """

    fileOut = open(directory + file_name, "w")

    writeHeader(fileOut, content[C.HEADER_INDEX])  # todo colocar nas constantes

    for iterator in range(1, len(content)):
        element = content[iterator]  # each element of the list received from content

        elementStr = convertExpertsDictToString(element)  # dictionary values transformed to Str per expert

        fileOut.write(elementStr + "\n")

    fileOut.close()


def convertExpertsDictToString(experts_dict):
    """

    # todo
    """

    expertsString = experts_dict.get(C.E_KEY_NAME) + ", " + \
                    experts_dict.get(C.E_KEY_LOCATION) + ", " + \
                    experts_dict.get(C.E_KEY_SPECIALITIES_LIST) + ", " + \
                    experts_dict.get(C.E_KEY_REVIEW) + ", " + \
                    str(experts_dict.get(C.E_KEY_COST)) + ", " + \
                    experts_dict.get(C.E_KEY_DATE) + ", " + \
                    experts_dict.get(C.E_KEY_TIME) + ", " + \
                    str(experts_dict.get(C.E_KEY_TOTAL_MONEY))

    return expertsString


def writeSchedule(file_name, content):
    """
    Write a file with the scheduling
    #todo contract """

    fileOut = open(directory + file_name, "w")

    writeHeader(fileOut, content[C.HEADER_INDEX])  # todo colocar nas constantes

    for iterator in range(1, len(content)):
        element = content[iterator]  # each element of the list received from content

        # print("este é o elemento:", element)

        elementStr = convertScheduleDictToString(element)  # dictionary values transformed to Str per expert

        fileOut.write(elementStr + "\n")

    fileOut.close()


def convertScheduleDictToString(schedule_dict):
    """
    # todo
    """

    schedule_string = schedule_dict.get(C.S_KEY_DATE) + ", " + \
                      schedule_dict.get(C.S_KEY_TIME) + ", " + \
                      schedule_dict.get(C.S_KEY_CLIENT_NAME) + ", " +\
                      schedule_dict.get(C.S_KEY_EXPERT_NAME)


    return schedule_string
