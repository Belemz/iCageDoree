#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém


# Import project modules
import constants as C
import dateTime as DT
import filesReading as FR


def expertIsEligible(client, expert):
    """
    Receives a client and an expert and verifies is the expert is eligible to perform the requested work by the client.
        REQUIRES: client and expert dictionaries, containing client and expert sets of key-values, respectively.

        ENSURES: True if an expert is eligible for that work. False if it is not eligible.
    """

    # checks if the expert speciality corresponds to the requested by the client.
    same_speciality = client.get(C.C_KEY_SPECIALITY) in FR.extractExpertsSpecialities(expert.get(C.E_KEY_SPECIALITIES_LIST))

    # checks if the expert has the minimum review rate desired by the client.
    enough_review = client.get(C.C_KEY_REVIEW) <= expert.get(C.E_KEY_REVIEW)

    # checks if the price of the expert is within the value specified by the client.
    cost_is_lower = client.get(C.C_KEY_PAYMENT) >= expert.get(C.E_KEY_COST)

    # checks if the location between the client and the expert match.
    same_location = client.get(C.C_KEY_LOCATION) == expert.get(C.E_KEY_LOCATION)


    return (same_speciality and enough_review and cost_is_lower and same_location)


def addExpertTravelTime(expert_date_str, expert_time_str):
    """
    Add the travel time to the expert availability time.
        REQUIRES: expert_date_str is str and represents the date at which the expert ends his last request.
                    expert_time_str is str and represents the time at which the expert ends his last request.

        ENSURES: updated date and time str that correspond to the real availability of the expert, i.e., at which time
            the expert could start working (with the travel time included).
    """

    # return DT.addPeriodToTime(expert_time_str, 1, 0, ":")  # add 01 hour and 00 minutes

    # addition of 1 hour and 0 minutes to the expert time.
    return DT.updateDateTime(expert_date_str, expert_time_str, 1, 0, ":")

def assignClient(client, expert):
    """ #todo"""

    schedule_dict = {}

    client_date = client.get(C.C_KEY_DATE)
    client_time = client.get(C.C_KEY_TIME)

    expert[C.E_KEY_DATE], expert[C.E_KEY_TIME] = addExpertTravelTime(expert.get(C.E_KEY_DATE), expert.get(C.E_KEY_TIME))

    predicted_arrival_hour, predicted_arrival_minutes = DT.getTimeFromString(expert[C.E_KEY_TIME], ":")

    if predicted_arrival_hour >= C.WORK_END_HOUR or predicted_arrival_hour < C.WORK_START_HOUR:

        expert[C.E_KEY_TIME] = DT.intDateTimeToString(C.WORK_START_HOUR) + ":" + DT.intDateTimeToString(0)
        expert[C.E_KEY_DATE] = DT.addDaysToDate(expert.get(C.E_KEY_DATE), 1)

    start_date, start_time = DT.selectMostRecentDateTime(client_date, \
                                                         client_time, \
                                                         expert[C.E_KEY_DATE], \
                                                         expert[C.E_KEY_TIME])

    schedule_dict[C.S_KEY_DATE] = start_date

    schedule_dict[C.S_KEY_TIME] = start_time

    schedule_dict[C.S_KEY_CLIENT_NAME] = client.get(C.C_KEY_NAME)

    schedule_dict[C.S_KEY_EXPERT_NAME] = expert.get(C.E_KEY_NAME)

    schedule_dict[C.S_KEY_IS_DECLINED] = False

    return schedule_dict


def declineClient(client, current_date, current_time):  # TODO Podia simplifcar e passar apenas o nome do client em vez do client todo.
    """ #todo"""

    schedule_dict = {}

    schedule_dict[C.S_KEY_DATE] = current_date

    schedule_dict[C.S_KEY_TIME] = current_time

    schedule_dict[C.S_KEY_CLIENT_NAME] = client.get(C.C_KEY_NAME)

    schedule_dict[C.S_KEY_EXPERT_NAME] = "declined"

    schedule_dict[C.S_KEY_IS_DECLINED] = True

    return schedule_dict


def calculateExpertTotalMoney(expert_initial_money, expert_cost_per_hour, number_of_hours_worked):
    """#TODO"""

    initial_money = float(expert_initial_money)
    expert_cost = int(expert_cost_per_hour)
    number_of_hours, number_of_minutes = DT.getTimeFromString(number_of_hours_worked, "h")

    total_number_of_hours_worked = int(number_of_hours) + float(number_of_minutes / C.MINUTES_PER_HOUR)
    earned_money = initial_money + (expert_cost * total_number_of_hours_worked)

    return str(earned_money)



def updateExpert(expert, client, assigned_schedule):
    """#TODO"""
    predicted_start_date = assigned_schedule.get(C.S_KEY_DATE)
    predicted_start_time = assigned_schedule.get(C.S_KEY_TIME)
    period = client.get(C.C_KEY_PERIOD)

    hours_to_add, minutes_to_add = DT.getTimeFromString(period, "h")


    predicted_end_date, predicted_end_time = DT.updateDateTime(predicted_start_date, predicted_start_time, hours_to_add, minutes_to_add)
    predicted_end_hour, predicted_end_minutes = DT.getTimeFromString(predicted_end_time)

    if (predicted_end_hour == C.WORK_END_HOUR and predicted_end_minutes != 0) or (predicted_end_hour > C.WORK_END_HOUR) \
            or (predicted_end_hour < C.WORK_START_HOUR):

        expert[C.E_KEY_DATE] = DT.addDaysToDate(predicted_end_date, 1)   #TODO: Deveria colocar a possibilidade de adicionar mais do que um dia?

        hours_to_add = predicted_end_hour - C.WORK_END_HOUR
        end_hour = C.WORK_START_HOUR + hours_to_add
        expert[C.E_KEY_TIME] = DT.intDateTimeToString(end_hour) + ":" + DT.intDateTimeToString(predicted_end_minutes)

    else:
        expert[C.E_KEY_DATE] = predicted_end_date
        expert[C.E_KEY_TIME] = predicted_end_time



    expert[C.E_KEY_TOTAL_MONEY] = calculateExpertTotalMoney(expert.get(C.E_KEY_TOTAL_MONEY), \
                                                            expert.get(C.E_KEY_COST), \
                                                            client.get(C.C_KEY_PERIOD))

    return expert


# TODO VERIFICAR SE É PARA DEIXAR COMO MUTÁVEL OU SE É PARA RETORNAR AS LISTAS?

#def initialSorting(clients_list, experts_list):
    """TODO"""
    clients_list.sort(key=lambda client: (client.get(C.C_KEY_DATE), \
                                          client.get(C.C_KEY_TIME), \
                                          client.get(C.C_KEY_NAME)))

def initialSorting(experts_list):


    experts_list.sort(key=lambda expert: (expert.get(C.E_KEY_DATE), \
                                          expert.get(C.E_KEY_TIME), \
                                          expert.get(C.E_KEY_COST), \
                                          expert.get(C.E_KEY_TOTAL_MONEY), \
                                          expert.get(C.E_KEY_NAME)))

def reSortExpert(experts_list):
    """
    :param experts_list:
    :return:
    """
    experts_list.sort(key=lambda expert: (expert.get(C.E_KEY_DATE), \
                                          expert.get(C.E_KEY_TIME), \
                                          expert.get(C.E_KEY_TOTAL_MONEY), \
                                          expert.get(C.E_KEY_NAME)))


def finalSorting(schedule_list, experts_list, number_of_declined_clients):
    """ TODO"""


    schedule_list.sort(key=lambda schedule: (schedule.get(C.S_KEY_DATE),\
                                             schedule.get(C.S_KEY_TIME),\
                                             schedule.get(C.S_KEY_CLIENT_NAME)))

    experts_list.sort(key=lambda expert: (expert.get(C.E_KEY_DATE),
                                          expert.get(C.E_KEY_TIME),
                                          expert.get(C.E_KEY_NAME)))

    if number_of_declined_clients >= 2:
        schedule_list.sort(key=lambda schedule: (schedule.get(C.S_KEY_IS_DECLINED)), reverse = True)



def schedule(clients_list, experts_list, current_date, current_time):
    """#todo"""

    schedule_list = []

    # initialSorting(clients_list, experts_list)
    initialSorting(experts_list)

    number_of_declined_clients = 0


    for client in clients_list:

        has_been_assigned = False
        index = 0

        while (index < len(experts_list) and not has_been_assigned): #todo confirmar negação do has_been_assigned

            expert = experts_list[index]

            if expertIsEligible(client, expert):
                scheduled_line = assignClient(client, expert)
                has_been_assigned = True

            else:
                index += 1



        if has_been_assigned:
            assigned_expert = experts_list.pop(index)
            updated_expert = updateExpert(assigned_expert, client, scheduled_line)
            experts_list.append(updated_expert)

            reSortExpert(experts_list)

        else:
            scheduled_line = declineClient(client, current_date, current_time)
            number_of_declined_clients += 1

        schedule_list.append(scheduled_line)

    finalSorting(schedule_list, experts_list, number_of_declined_clients)


    return schedule_list, experts_list


    # 1) Se houver só um decline, deve ficar no topo do ficheiro à mesma? Ordem natural (local onde está)

    # 2) Se um cliente pretender arranjar um frigorífico a partir da data 31-10-2010 das 10:00, caso não haja melhor
    # alternativa, um especialista que esteja livre na data 1/11/2010, poderá fazê-lo, certo ?
