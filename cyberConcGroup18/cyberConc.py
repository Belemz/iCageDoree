#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém
# 31955 Inês de Carvalho Fernandes Martins da Silva

import sys

import constants as C
import filesReading as FR
import filesWriting as FW
import scheduling as S


def assign(file_name_experts, file_name_clients):
    """
    Assign given experts given to given clients.
    Requires: fileNameExperts, fileNameClients are str, with the names
    of the files representing the list of experts and clients, respectively,
    following the format indicated in the project.
    Ensures: Two output files, respectively, with the listing of schedules
    tasks and the updated listing of experts, following the format
    and naming convention indicated in the project.
    """
        #to be completed


    # opens the file, removes and update the header from the list(for both clients and experts)

    clients_content = FR.readClientsFile(file_name_clients)
    clients_header = clients_content.pop(C.HEADER_INDEX)
    updated_schedule_header = FW.updateHeader(clients_header, "Schedule")
    new_schedule_file_name = FW.createFileName(updated_schedule_header)

    experts_content = FR.readExpertsFile(file_name_experts)
    experts_header = experts_content.pop(C.HEADER_INDEX)
    updated_experts_header = FW.updateHeader(experts_header, "Experts")
    new_experts_file_name = FW.createFileName(updated_experts_header)


    scheduled_content, updated_experts_content = S.schedule(clients_content, experts_content)

    scheduled_content.insert(C.HEADER_INDEX, updated_schedule_header)
    updated_experts_content.insert(C.HEADER_INDEX, updated_experts_header)


    FW.writeSchedule(new_schedule_file_name, scheduled_content)
    FW.writeExpertsFile(new_experts_file_name, updated_experts_content)


inputFileName1, inputFileName2 = sys.argv[1:]
assign(inputFileName1, inputFileName2)
print("terminou assign")
# assign("./../tests_v2/example1/2019y01m12experts09h00.txt", "./../tests_v2/example1/2019y01m12clients09h00.txt")


