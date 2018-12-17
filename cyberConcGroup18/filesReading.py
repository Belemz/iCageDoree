#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém

# Import project modules
import constants as C


def readHeader(file_name):
    """
    Reads the header of a file and stores the information in a tuple.
        REQUIRES: file_name is str and in the format specified in this program.

        ENSURES: a tuple with the header information where the first element is a date str in the format "yyyy-mm-dd"
                                                                second element is a time str in the format "hh:mm",
                                                                third element is company str,
                                                                fourth element is scope str.
    """

    fileIn = open(file_name, 'r')

    fileIn.readline()
    day = fileIn.readline().strip().replace("\n", "")

    fileIn.readline()
    time = fileIn.readline().strip().replace("\n", "")

    fileIn.readline()
    company = fileIn.readline().strip().replace("\n", "")

    scope = fileIn.readline().strip().replace("\n", "")

    fileIn.close()

    return (day, time, company, scope)  # returns a tuple


def readExpertsFile(file_name):
    """
   Converts a given file listing experts into a collection.
        REQUIRES: file_name is str, the name of a .txt file listing expert,
            following the format specified in the project.

        ENSURES: list whose first element is a tuple that corresponds to the header (date, time, company and scope),
                            the following elements correspond to dictionaries containing experts, where the
                            first element is the name of the expert,
                            second is their geographic area of work,
                            third is a tuple with their specialities,
                            fourth is their review rate,
                            fifth is their cost per hour,
                            sixth is the end date of their last order,
                            seventh is the time at which they become available,
                            eighth is the accumulated amount of money(in €) for the completed work.
        """

    output_list = []

    output_list.append(readHeader(file_name))

    file_content = open(file_name, 'r')

    for line in file_content.readlines()[C.EXPERT_START_LINE:]:
        striped_line = line.strip("\n")
        processed_line = striped_line.split(",")

        expert = convertExpertToDictionary(processed_line)

        output_list.append(expert)

    file_content.close()

    return output_list


def convertExpertToDictionary(expert_line_list):
    """
    Convert a string that corresponds to an expert into a dictionary.
        REQUIRES: expert_line_list is str and corresponds to a line in a file that is specified as in the project.

        ENSURES: a dictionary that corresponds to one expert containing keys associated with each of the
            str elements separated by "," in the line.
    """

    dictionary = {}

    dictionary[C.E_KEY_NAME] = expert_line_list[0].strip(" ")
    dictionary[C.E_KEY_LOCATION] = expert_line_list[1].strip(" ")
    dictionary[C.E_KEY_SPECIALITIES_LIST] = expert_line_list[2].strip(" ")
    dictionary[C.E_KEY_REVIEW] = expert_line_list[3].strip(" ")
    dictionary[C.E_KEY_COST] = int(expert_line_list[4].strip(" "))
    dictionary[C.E_KEY_DATE] = expert_line_list[5].strip(" ")
    dictionary[C.E_KEY_TIME] = expert_line_list[6].strip(" ")
    dictionary[C.E_KEY_TOTAL_MONEY] = float(expert_line_list[7].strip(" "))
    return dictionary


def extractExpertsSpecialities(speciality_string_tuple):
    """
    Converts a speciality_string_tuple tuple into a tuple of strings.
        REQUIRES: a string_tuple that is a str of a tuple containing specialities of the expert separated by a ";".

        ENSURES: a tuple with str elements, corresponding to the different specialities.
    """

    removal_of_parentheses = speciality_string_tuple.replace("(", "").replace(")", "")
    list_of_speciality = []
    processed_string = removal_of_parentheses.split(";")
    for word in processed_string:
        striped_word = word.strip(" ")
        list_of_speciality.append(striped_word)

    return list_of_speciality


def readClientsFile(file_name):
    """
    Converts a given file listing clients into a collection.
        REQUIRES: file_name is str, the name of a .txt file listing clients,
    following the format specified in the project.

        ENSURES: list whose first element is a tuple that corresponds to the header (date, time, company and scope),
                            the following elements correspond to dictionaries containing clients' requests, where the
                            first element is the name of the client,
                            second is their geographic area of work,
                            third is the date from which the request must be executed,
                            fourth is the time from which the request must be executed,
                            fifth is the maximum amount of money the client accepts to pay per hour,
                            sixth is the minimum review rate of the expert to be hired,
                            seventh is the desired service,
                            eighth is the period of hours they intend to hire the expert.
    """

    clients_list = []

    clients_list.append(readHeader(file_name))

    file_content = open(file_name, 'r')

    for line in file_content.readlines()[C.CLIENT_START_LINE:]:
        striped_line = line.strip("\n")
        processed_line = striped_line.split(",")

        client = convertClientToDictionary(processed_line)
        clients_list.append(client)

    file_content.close()

    return clients_list


def convertClientToDictionary(client_line_list):
    """
    Convert a string that corresponds to a client into a dictionary.
        REQUIRES: client_line_list is str and corresponds to a client line in a file that is specified as in the project.

        ENSURES: a dictionary that corresponds to one client containing keys associated with each of the
            str elements separated by "," in the line.
    """

    dictionary = {}

    dictionary[C.C_KEY_NAME] = client_line_list[0].strip(" ")
    dictionary[C.C_KEY_LOCATION] = client_line_list[1].strip(" ")
    dictionary[C.C_KEY_DATE] = client_line_list[2].strip(" ")
    dictionary[C.C_KEY_TIME] = client_line_list[3].strip(" ")
    dictionary[C.C_KEY_PAYMENT] = int(client_line_list[4].strip(" "))
    dictionary[C.C_KEY_REVIEW] = client_line_list[5].strip(" ")
    dictionary[C.C_KEY_SPECIALITY] = client_line_list[6].strip(" ")
    dictionary[C.C_KEY_PERIOD] = client_line_list[7].strip(" ")

    return dictionary

