#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém


import copy
# Import python built-in modules
import sys

# Import project modules
import constants as C
import filesReading as FR
import filesWriting as FW
import scheduling as S


def checkConsistencyHeaderFileName(header, file_path):
    """
    Checks if the file_path corresponds to the file header.
        REQUIRES: header is a tuple of str. The str's in the tuple represent (date, time, company, scope) in this order.
                  file_path is str.
        ENSURES: raise a ValueError Exception if the content in the file_path and header are not the same.
    """
    file_name = file_path.split("/")[-1]

    # an alternative to the try-catch, would be using the assert condition in the "guard" condition of an if statement.
    # the raise would then be raised in the else statement.
    try:
        assert FW.createFileName(header) == file_name
    except AssertionError:
        raise ValueError("Error in input file: inconsistent name and header in file " + file_name + ".")



def checkConsistencyBetweenFiles(file_path1, header1, file_path2, header2):
    """
    Checks if there are no inconsistencies between the date, time and company of two headers.
        REQUIRES: header1 and header2 is a tuple of str. The str's in the tuple represent (date, time, company, scope) in this order.
                  file_path is str.

        ENSURES: raise a IOError Exception if the content between the two headers does not match.
    """
    file_name1 = file_path1.split("/")[-1]
    file_name2 = file_path2.split("/")[-1]

    # an alternative to the try-catch, would be using the assert condition in the "guard" condition of an if statement.
    # the raise would then be raised in the else statement.
    try:
        for iterator in range(len(header1) - 1):
            assert header1[iterator] == header2[iterator]
    except AssertionError:
        raise IOError(
            "Error in input files: inconsistent files " + file_name1 + " and " + file_name2 + ".")



def assign(file_path_experts, file_path_clients):
    """
    Assign given experts given to given clients.
        REQUIRES: fileNameExperts, fileNameClients are str, with the paths of the files representing the
        list of experts and clients, respectively, following the format indicated in the project.

        ENSURES: Two output files, respectively, with the listing of schedules tasks and the updated
        listing of experts, following the format and naming convention indicated in the project.
    """

    clients_content = FR.readClientsFile(file_path_clients)
    experts_content = FR.readExpertsFile(file_path_experts)

    copy_clients_content = copy.deepcopy(clients_content)
    copy_experts_content = copy.deepcopy(experts_content)

    clients_header = copy_clients_content.pop(C.HEADER_INDEX)
    experts_header = copy_experts_content.pop(C.HEADER_INDEX)

    #exception treatment
    checkConsistencyHeaderFileName(clients_header, file_path_clients)
    checkConsistencyHeaderFileName(experts_header, file_path_experts)

    checkConsistencyBetweenFiles(file_path_clients, clients_header, file_path_experts, experts_header)


    updated_schedule_header = FW.updateHeader(clients_header, "Schedule")
    new_schedule_file_name = FW.createFileName(updated_schedule_header)

    updated_experts_header = FW.updateHeader(experts_header, "Experts")
    new_experts_file_name = FW.createFileName(updated_experts_header)

    current_date = updated_schedule_header[C.HEADER_DATE_INDEX]
    current_time = updated_schedule_header[C.HEADER_TIME_INDEX]

    scheduled_content, updated_experts_content = S.schedule(copy_clients_content, copy_experts_content, current_date,
                                                            current_time)

    scheduled_content.insert(C.HEADER_INDEX, updated_schedule_header)
    updated_experts_content.insert(C.HEADER_INDEX, updated_experts_header)

    # one could also put file_path_clients (assuming they are in the same folder).
    output_directory = FW.createDirectory(file_path_experts)

    FW.writeSchedule(new_schedule_file_name, scheduled_content, output_directory)
    FW.writeExpertsFile(new_experts_file_name, updated_experts_content, output_directory)


input_expert_file, input_client_file = sys.argv[1:]
# assign(input_expert_file, input_client_file)


assign("./../debug/exemplo1/2019y01m12experts09h00.txt", "./../debug/exemplo1/2019y01m12clients09h00.txt")
assign("./../debug/exemplo2/2019y02m15experts10h30.txt", "./../debug/exemplo2/2019y02m15clients10h30.txt")
assign("./../debug/exemplo3/2019y03m20experts12h30.txt", "./../debug/exemplo3/2019y03m20clients12h30.txt")
