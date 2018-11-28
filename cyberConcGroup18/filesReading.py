# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém
# 31955 Inês de Carvalho Fernandes Martins da Silva

import constants

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

    inFile = open ( fileName , 'r' )

    outputList.append(readHeader(fileName))

    fileIn = open(fileName, 'r')

    expertsList = []
    counter = 0
    for line in fileIn.readlines ():
        if counter >= 7:
            line.replace ("\n", "")
            expertsList.append (line.split (","))
        counter += 1



    fileIn.close()

    return (expertsList)



def readClientsFile(fileName):
    """"
    Converts a given file listing clients into a collection
        Requires: a fileName is str, the name of a .txt file listing experts, following the format specified
        in the project.
        Ensures: list whose first element is the name of the client,
                  second element is the

        ## COMPLETEEEE! """



    outputList = []

    inFile = open ( fileName , 'r' )

    outputList.append(readHeader(fileName))

#    print(outputList)

    inFile = open(fileName, 'r')

    for i in range(constants.header_number_lines):        ## redudante -  como fazer para evitar estar a abrir o ficheiro e a ler
        inFile.readline()


    for line in inFile.readlines():

        processed_line = line.replace ( "\n" , "" )

        outputList.append(processed_line.split(","))

    inFile.close()

    return outputList

# test:
print(readClientsFile("/Users/ClaudiaBelem/Google Drive (belem@campus.ul.pt)/FCUL - Informática/1º semestre/Fundamentos de programacao/Projeto/iCageDoree/tests/example1/2019y01m12experts09h00.txt"))
