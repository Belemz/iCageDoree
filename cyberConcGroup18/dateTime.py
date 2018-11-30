# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém
# 31955 Inês de Carvalho Fernandes Martins da Silva

# import constants

def getTimeFromString(timeEntry):
    """
    # todo: contract    """
    time = timeEntry.split(":")

    hour = int(time[0])
    min = int(time[1])

    return (hour, min)

def timeToString(timeTuple):
    """#todo: contract"""

    hour =(timeTuple[0])
    min = (timeTuple [1])

    if 0 <= hour <= 9 and 0 <= min <= 9:
        hour = "0"+ str(hour)
        min = "0"+ str(min)

    elif 0 <= hour <= 9:
        hour = "0" + str(hour)

    elif 0 <= min <=9:
        min = "0" + str(min)



    timeString = str(hour) + ":" + str(min)

    return timeString


def getDateFromString(string):
    """
    # todo: contract

    """


def dateToString():
    """#todo: contract"""


print(getTimeFromString(timeEntry="00:00"))
print(timeToString(getTimeFromString(timeEntry="00:00")))