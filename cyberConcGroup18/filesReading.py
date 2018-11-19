# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém
# 31955 Inês de Carvalho Fernandes Martins da Silva


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

    return outputList



def readHeader(fileName):
    
    # ... <to complete>

    fileIn.readline()
    day = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    time = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    company = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    scope = fileIn.readline().strip().replace("\n", "")
    
    return (day, time, company, scope)
