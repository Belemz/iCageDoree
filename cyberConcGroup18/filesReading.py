# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém
# 31955 Inês de Carvalho Fernandes Martins da Silva


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
    Ensures: list whose first element is ... <to complete>
    """
    outputList = []
    
    outputList.append(readHeader(fileName))
    
    fileIn = open(fileName, 'r')

    # ... <to complete>

    return (outputList)


def readClientsFile(fileName):
    """"
    Converts a given file listing clients into a collection
        Requires: a fileName is str, the name of a .txt file listing experts, following the format specified
        in the project.
        Ensures: list whose first element is the name of the client,
                  second element is the

        ## COMPLETEEEE! """

    outputList = []

    outputList.append(readHeader(fileName))

    print(outputList)

    inFile = open(fileName, 'r')

    count = 0
    clientsList = []

    for line in inFile.readlines():

        processed_line = line.replace ( "\n" , "" )

        if count >= 7:

            clientList = processed_line.split(",")

            outputList.append(clientList)

        count = count + 1

    inFile.close()

    return outputList

# test :
print(readClientsFile("/Users/ClaudiaBelem/PycharmProjects/iCageDoree/tests/example1/2019y01m12clients09h00.txt"))
