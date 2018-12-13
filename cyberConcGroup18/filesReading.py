# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém
# 31955 Inês de Carvalho Fernandes Martins da Silva

import constants as C

def readHeader(fileName):
    # ... <to complete>

    fileIn = open(fileName, 'r')

    fileIn.readline()
    day = fileIn.readline().strip().replace("\n", "")

    fileIn.readline()
    time = fileIn.readline().strip().replace("\n", "")

    fileIn.readline()
    company = fileIn.readline().strip().replace("\n", "")


    scope = fileIn.readline().strip().replace("\n", "")

    fileIn.close()

    return (day, time, company, scope)     # returns a tuple

    ## teste:  print("o dia é ", day)
    # print("o tempo é ", time)
    # print("a companhia é ", company)
    # print("o scope é ", scope)

def readExpertsFile(fileName):
    """
    Converts a given file listing experts into a collection
    Requires: fileName is str, the name of a .txt file listing experts,
    following the format specified in the project.
    Ensures: list whose first element is the name of the expert,
        second is their geographic area of work,
        third is their specialty,
        fourth is their review rate,
        fifth is their hourly pay,
        sixth is the end date of their last order,
        seventh is starting time of next available slot,
        eighth is the accumulated amount (in €) for the completed work
    """

    outputList = []

    outputList.append(readHeader(fileName))

    fileIn = open(fileName, 'r')


    counter = 0
    for line in fileIn.readlines():   ## todo o professor sugeriu fazer slicing do readlines
        if counter >= 7:
            striped_line = line.strip("\n")

            processed_line = striped_line.split(",")

            expert = expertToDictionary(processed_line)

            # print("esta é o cliente:", expert)

            outputList.append (expert)


        counter += 1

    fileIn.close()

    return outputList


def expertToDictionary(expertLineList):           # TODO: CONFIRMAR TIPOS QUE SÃO GUARDADOS NO DICIONÁRIO
    """ #todo
    """

    dictionary = {}

    dictionary[C.E_KEY_NAME] = expertLineList[0].strip(" ")
    dictionary[C.E_KEY_LOCATION] = expertLineList[1].strip(" ")
    dictionary[C.E_KEY_SPECIALITIES_LIST] = expertLineList[2].strip(" ")
    dictionary[C.E_KEY_REVIEW] = expertLineList[3].strip(" ")
    dictionary[C.E_KEY_COST] = int(expertLineList[4].strip(" "))
    dictionary[C.E_KEY_DATE] = expertLineList[5].strip(" ")
    dictionary[C.E_KEY_TIME] = expertLineList[6].strip(" ")
    dictionary[C.E_KEY_TOTAL_MONEY] = float(expertLineList[7].strip(" "))
    return dictionary


def readClientsFile(fileName):
    """"
    Converts a given file listing clients into a collection
        Requires: a fileName is str, the name of a .txt file listing experts, following the format specified
        in the project.
        Ensures: list whose first element is the name of the client,
                  second element is the

        ##TODO COMPLETEEEE! """

    outputList = []

    outputList.append(readHeader(fileName))

#    print(outputList)

    fileIn = open(fileName, 'r')

    for _ in range(C.header_number_lines):        ## todo redudante -  como fazer para evitar estar a abrir o ficheiro e a ler
        fileIn.readline()


    for line in fileIn.readlines():
        striped_line = line.strip ( "\n" )
        processed_line = striped_line.split ( "," )
        client = clientsToDictionary(processed_line)
        outputList.append(client)

    fileIn.close()

    return outputList


def clientsToDictionary(clientLineList):   # TODO: CONFIRMAR TIPOS QUE SÃO GUARDADOS NO DICIONÁRIO
    """ #todo
    """

    dictionary = {}

    dictionary[C.C_KEY_NAME] = clientLineList[0].strip(" ")
    dictionary[C.C_KEY_LOCATION] = clientLineList[1].strip(" ")
    dictionary[C.C_KEY_DATE] = clientLineList[2].strip(" ")
    dictionary[C.C_KEY_TIME] = clientLineList[3].strip(" ")
    dictionary[C.C_KEY_PAYMENT] = int(clientLineList[4].strip(" "))
    dictionary[C.C_KEY_REVIEW] = clientLineList[5].strip(" ")
    dictionary[C.C_KEY_SPECIALITY] = clientLineList[6].strip(" ")
    dictionary[C.C_KEY_PERIOD] = clientLineList[7].strip(" ")

    return dictionary
