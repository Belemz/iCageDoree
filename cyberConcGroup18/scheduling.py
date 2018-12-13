# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém
# 31955 Inês de Carvalho Fernandes Martins da Silva

import constants as C
import dateTime as DT

def extractExpertsSpecialities(string):
    """#TODO
    """

    removal_of_parentheses = string.replace("(","").replace(")","")
    list_of_speciality = []
    processed_string = removal_of_parentheses.split(";")
    for word in processed_string:
        striped_word = word.strip(" ")
        list_of_speciality.append(striped_word)

    return list_of_speciality


def expertIsEligible(client, expert):
    """
    todo finish the contract
    :param client:
    :param expert:
    :return:
    """

    same_specialty = client.get(C.C_KEY_SPECIALITY) in extractExpertsSpecialities(expert.get(C.E_KEY_SPECIALITIES_LIST))
    enough_review = client.get(C.C_KEY_REVIEW) <= expert.get(C.E_KEY_REVIEW)
    cost_is_lower = client.get(C.C_KEY_PAYMENT) >= expert.get(C.E_KEY_COST)
    same_location = client.get(C.C_KEY_LOCATION) == expert.get(C.E_KEY_LOCATION)


    return (same_specialty and enough_review and cost_is_lower and same_location)


def addExpertTravelTime(expert_time_str):
    """todo"""

    return DT.addPeriodToTime(expert_time_str, 1, 0, ":")  # add 01 hour and 00 minutes


def assignClient(client, expert):
    """ #todo"""


    schedule_dict = {}

    start_date, start_time = DT.selectMostRecentDateTime(client.get(C.C_KEY_DATE),
                                                         client.get(C.C_KEY_TIME),
                                                         expert.get(C.E_KEY_DATE),
                                                         addExpertTravelTime(expert.get(C.E_KEY_TIME)))

    schedule_dict[C.S_KEY_DATE] = start_date

    schedule_dict[C.S_KEY_TIME] = start_time

    schedule_dict[C.S_KEY_CLIENT_NAME] = client.get(C.C_KEY_NAME)

    schedule_dict[C.S_KEY_EXPERT_NAME] = expert.get(C.E_KEY_NAME)

    schedule_dict[C.S_KEY_IS_DECLINED] = False

    return schedule_dict



def declineClient(client):
    """ #todo"""


    schedule_dict = {}

    schedule_dict[C.S_KEY_DATE] = client.get(C.C_KEY_DATE)

    schedule_dict[C.S_KEY_TIME] = client.get(C.C_KEY_TIME)

    schedule_dict[C.S_KEY_CLIENT_NAME] = client.get(C.C_KEY_NAME)

    schedule_dict[C.S_KEY_EXPERT_NAME] = "declined"

    schedule_dict[C.S_KEY_IS_DECLINED] = True


    return schedule_dict


def updateExpert(expert, client, assigned_schedule):
    """#TODO"""

    expert_start_time = assigned_schedule.get(C.S_KEY_TIME)
    period = client.get(C.C_KEY_PERIOD)
    expert[C.E_KEY_TIME] = DT.addPeriodStringToTime(expert_start_time, period,"h" )  #TODO: CHECK 08:00 - 20:00 SCHEDULE



    return expert



def schedule(clients_list, experts_list):
    """#todo"""

    schedule_list = []

    clients_list.sort(key = lambda client: (client.get(C.C_KEY_DATE), \
                                            client.get(C.C_KEY_TIME)))


    experts_list.sort(key = lambda expert: (expert.get(C.E_KEY_DATE), \
                                            expert.get(C.E_KEY_TIME), \
                                            expert.get(C.E_KEY_TOTAL_MONEY), \
                                            expert.get(C.E_KEY_NAME)))


    for client in clients_list:

        has_been_assigned = False
        index = 0

        while (index < len(experts_list) and not has_been_assigned): #todo confirmar negação do has_been_assigned

            expert = experts_list[index]

            if expertIsEligible(client, expert):
                scheduled_line = assignClient(client, expert)
                schedule_list.append(scheduled_line)
                has_been_assigned = True

            index += 1

        if has_been_assigned:
            assigned_expert = experts_list.pop(index-1)
            updated_expert = updateExpert(assigned_expert, client, scheduled_line)
            experts_list.append(updated_expert)

            experts_list.sort(key=lambda expert: (expert.get(C.E_KEY_DATE), \
                                                  expert.get(C.E_KEY_TIME), \
                                                  expert.get(C.E_KEY_TOTAL_MONEY), \
                                                  expert.get(C.E_KEY_NAME)))



        else:
            scheduled_line = declineClient(client)
            schedule_list.append(scheduled_line)

    return schedule_list, experts_list


    # 1) Se houver só um decline, deve ficar no topo do ficheiro à mesma? Ordem natural (local onde está)

    # 2) Se um cliente pretender arranjar um frigorífico a partir da data 31-10-2010 das 10:00, caso não haja melhor
    # alternativa, um especialista que esteja livre na data 1/11/2010, poderá fazê-lo, certo ?
