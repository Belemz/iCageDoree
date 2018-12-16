#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém


# Import python built-in modules
import sys

# Import project modules
import constants as C
import filesReading as FR
import filesWriting as FW
import scheduling as S


def assign(file_name_experts, file_name_clients):
    """
    Assign given experts given to given clients.
        REQUIRES: fileNameExperts, fileNameClients are str, with the names of the files representing the
        list of experts and clients, respectively, following the format indicated in the project.

        ENSURES: Two output files, respectively, with the listing of schedules tasks and the updated
        listing of experts, following the format and naming convention indicated in the project.
    """

    clients_content = FR.readClientsFile(file_name_clients)
    clients_header = clients_content.pop(C.HEADER_INDEX)
    updated_schedule_header = FW.updateHeader(clients_header, "Schedule")
    new_schedule_file_name = FW.createFileName(updated_schedule_header)

    experts_content = FR.readExpertsFile(file_name_experts)
    experts_header = experts_content.pop(C.HEADER_INDEX)
    updated_experts_header = FW.updateHeader(experts_header, "Experts")
    new_experts_file_name = FW.createFileName(updated_experts_header)


    current_date = updated_schedule_header[C.HEADER_DATE_INDEX]
    current_time = updated_schedule_header[C.HEADER_TIME_INDEX]

    scheduled_content, updated_experts_content = S.schedule(clients_content, experts_content, current_date, current_time)

    scheduled_content.insert(C.HEADER_INDEX, updated_schedule_header)
    updated_experts_content.insert(C.HEADER_INDEX, updated_experts_header)


    FW.writeSchedule(new_schedule_file_name, scheduled_content)
    FW.writeExpertsFile(new_experts_file_name, updated_experts_content)


inputFileName1, inputFileName2 = sys.argv[1:]
#assign(inputFileName1, inputFileName2)

#inputFileName1 = experts file
#inputFileName2 = clients file

assign("./../tests_v4/example1/2019y01m12experts09h00.txt", "./../tests_v4/example1/2019y01m12clients09h00.txt")
print("terminou assign")
assign("./../tests_v4/example2/2019y02m15experts10h30.txt", "./../tests_v4/example2/2019y02m15clients10h30.txt")
print("terminou assign")
assign("./../tests_v4/example3/2019y03m20experts12h30.txt", "./../tests_v4/example3/2019y03m20clients12h30.txt")
print("terminou assign")

