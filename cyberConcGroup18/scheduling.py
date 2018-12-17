#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém


# Import project modules
import constants as C
import dateTime as DT
import filesReading as FR


def schedule(clients_list, experts_list, current_date, current_time):
    """
    Matches the clients in a clients_list with the experts in an experts_list.
    Requires
    :param clients_list:
    :param experts_list:
    :param current_date:
    :param current_time:
    :return:
    """

    schedule_list = []

    # clientSorting(clients_list) # if we wanted to sort the clients by the date and time of the requests.
    expertSorting(experts_list)

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

            expertSorting(experts_list)

        else:
            scheduled_line = declineClient(client.get(C.C_KEY_NAME), current_date, current_time)
            number_of_declined_clients += 1

        schedule_list.append(scheduled_line)

    finalSorting(schedule_list, experts_list, number_of_declined_clients)


    return schedule_list, experts_list


# def clientSorting(clients_list):
# """
# Sorts the client_list according to the date, time and name.
#       REQUIRES: a list of dictionaries, each corresponding to a client.
#
#       ENSURES: the list sorted by the client date, time and name, in an ascending way.
# """
#     clients_list.sort(key=lambda client: (client.get(C.C_KEY_DATE), \
#                                           client.get(C.C_KEY_TIME), \
#                                           client.get(C.C_KEY_NAME)))

def expertSorting(experts_list):
    """
    Sorts the experts_list according to the date, time and name.
        REQUIRES: a list of dictionaries, each corresponding to an expert.

        ENSURES: the list sorted by the expert date, time, cost, total money and name, in an ascending way.
    """

    experts_list.sort(key=lambda expert: (expert.get(C.E_KEY_DATE), \
                                          expert.get(C.E_KEY_TIME), \
                                          expert.get(C.E_KEY_COST), \
                                          expert.get(C.E_KEY_TOTAL_MONEY), \
                                          expert.get(C.E_KEY_NAME)))




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



def assignClient(client, expert):
    """
    Assigns an expert to a client.
        REQUIRES: a client dictionary and an expert dictionary.

        ENSURES: dictionary, schedule_dict, with the scheduled request. The dictionary keys are DATE, TIME, CLIENT_NAME,
            EXPERT_NAME and IS_DECLINED.
    """

    schedule_dict = {}

    client_date = client.get(C.C_KEY_DATE)
    client_time = client.get(C.C_KEY_TIME)

    expert[C.E_KEY_DATE], expert[C.E_KEY_TIME] = addExpertTravelTime(expert.get(C.E_KEY_DATE), expert.get(C.E_KEY_TIME))

    predicted_start_hour, _ = DT.getTimeFromString(expert[C.E_KEY_TIME], ":")

    if predicted_start_hour >= C.WORK_END_HOUR or predicted_start_hour < C.WORK_START_HOUR:

        expert[C.E_KEY_TIME] = DT.intDateTimeToString(C.WORK_START_HOUR) \
                               + ":" \
                               + DT.intDateTimeToString(0)

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



def addExpertTravelTime(expert_date_str, expert_time_str):
    """
    Add the 1h travel time to the expert availability time.
        REQUIRES: expert_date_str is str and represents the date at which the expert ends his last request.
                    expert_time_str is str and represents the time at which the expert ends his last request.

        ENSURES: updated date and time str that correspond to the real availability of the expert, i.e., at which time
            the expert could start working (with the travel time included).
    """

    # addition of 1 hour and 0 minutes to the expert time.
    return DT.updateDateTime(expert_date_str, expert_time_str, 1, 0, ":")



def declineClient(client_name, current_date, current_time):
    """
    Converts the request to declined.
        REQUIRES: client_name is str corresponding to the name of the client with out an assigned expert.
                  current_date is str and represents the date in the format "yyyy-mm-dd".
                  current_time is str and represents the time in the format "hh:mm".

        ENSURES: a schedule_dictionary containing the updated date and time str (equal to the header date and time),
            the client_name str, "declined" and True.
    """

    schedule_dict = {}

    schedule_dict[C.S_KEY_DATE] = current_date

    schedule_dict[C.S_KEY_TIME] = current_time

    schedule_dict[C.S_KEY_CLIENT_NAME] = client_name

    schedule_dict[C.S_KEY_EXPERT_NAME] = "declined"

    schedule_dict[C.S_KEY_IS_DECLINED] = True

    return schedule_dict



def updateExpert(expert, client, assigned_schedule):
    """
    Updates the expert date and time of last request and the total_money gathered.
        REQUIRES: expert is dictionary.
                  client is dictionary.
                  assigned_schedule is dictionary that corresponds to the scheduled request between the
            given expert and client.

        ENSURES: expert dictionary updated. The E_KEY_DATE, E_KEY_TIME and E_KEY_TOTAL_MONEY are updated
            according to the scheduled request. The E_KEY_DATE and E_KEY_TIME are calculated based on the
            previously established working interval (from 08:00 to 20:00).
    """

    predicted_start_date = assigned_schedule.get(C.S_KEY_DATE)
    predicted_start_time = assigned_schedule.get(C.S_KEY_TIME)
    hiring_period = client.get(C.C_KEY_PERIOD)

    hours_to_add, minutes_to_add = DT.getTimeFromString(hiring_period, "h")

   # verifies if the working period respects the interval established in the project and makes the necessary alterations
    predicted_end_date, predicted_end_time = DT.updateDateTime(predicted_start_date, \
                                                               predicted_start_time, \
                                                               hours_to_add, \
                                                               minutes_to_add)

    predicted_end_hour, predicted_end_minutes = DT.getTimeFromString(predicted_end_time)

    if (predicted_end_hour == C.WORK_END_HOUR and predicted_end_minutes != 0) \
            or (predicted_end_hour > C.WORK_END_HOUR) \
            or (predicted_end_hour < C.WORK_START_HOUR):


        expert[C.E_KEY_DATE] = DT.addDaysToDate(predicted_end_date, 1) #adds one day to the request date.

        hours_to_add = predicted_end_hour - C.WORK_END_HOUR

        end_hour = C.WORK_START_HOUR + hours_to_add

        expert[C.E_KEY_TIME] = DT.intDateTimeToString(end_hour) + ":" + DT.intDateTimeToString(predicted_end_minutes)


    else:
        expert[C.E_KEY_DATE] = predicted_end_date
        expert[C.E_KEY_TIME] = predicted_end_time


    # calculates the total money after carrying on the service.
    accumulated_money = calculateExpertTotalMoney(expert.get(C.E_KEY_TOTAL_MONEY), \
                                                            expert.get(C.E_KEY_COST), \
                                                            hiring_period)
    expert[C.E_KEY_TOTAL_MONEY] = accumulated_money

    return expert


def calculateExpertTotalMoney(expert_initial_money, expert_cost_per_hour, time_worked):
    """
    Calculates the expert total money after completing a service / fulfilling a client request.
        REQUIRES: expert_initial_money is str
                  expert_cost_per_hour is str
                  time_worked is str

        ENSURES: str of total_money_gathered by the expert upon completing the request.
    """

    initial_money = float(expert_initial_money)
    expert_cost = int(expert_cost_per_hour)
    number_of_hours, number_of_minutes = DT.getTimeFromString(time_worked, "h")

    total_number_of_hours_worked = int(number_of_hours) + float(number_of_minutes / C.MINUTES_PER_HOUR)

    total_money_gathered = initial_money + (expert_cost * total_number_of_hours_worked)

    return str(total_money_gathered)


# TODO VERIFICAR SE É PARA DEIXAR COMO MUTÁVEL OU SE É PARA RETORNAR AS LISTAS?

def finalSorting(schedule_list, experts_list, number_of_declined_clients):
    """
    Sorts the schedule_list and experts_list according to date, time and name of client and expert, respectively.
        REQUIRES: schedule_list is a list with dictionaries, each corresponding to a scheduled request of a client.
                  experts_list is a list with dictionaries, each corresponding to a expert.
                  number_of_declined_clients is an int >= 0 corresponding to the number of declined requests.
        ENSURES: experts_list re-ordered according to the expert date and time of last request, and alphabetic order of
            the expert name.
                 schedule_list re-ordered by the ascending schedule date, time and client name. If there are two or more
            requests declined, they appear before the other schedules. Else, the order is the same as described
            before.
    """


    schedule_list.sort(key=lambda schedule: (schedule.get(C.S_KEY_DATE),\
                                             schedule.get(C.S_KEY_TIME),\
                                             schedule.get(C.S_KEY_CLIENT_NAME)))

    experts_list.sort(key=lambda expert: (expert.get(C.E_KEY_DATE),
                                          expert.get(C.E_KEY_TIME),
                                          expert.get(C.E_KEY_NAME)))

    if number_of_declined_clients >= 2:
        schedule_list.sort(key=lambda schedule: (schedule.get(C.S_KEY_IS_DECLINED)), reverse = True)
