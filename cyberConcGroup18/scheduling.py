# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém
# 31955 Inês de Carvalho Fernandes Martins da Silva

import filesReading
import filesWriting

def numberClient(filename):
    """ Retrieves the number of clients that are waiting.
        REQUIRES: file name is str.
        ENSURES:  the number of clients in a client list. (Between 0 and )"""

    count = 0
    clientNumber = 0

    openFile = open(filename,"r")

    for line in openFile.readlines:
        count +=1

    clientNumber = count - 7

    return clientNumber




def test (fileNameToRead):
    """# todo"""


    content = filesReading.readExpertsFile (fileNameToRead)


    filesWriting.writeExpertsFile(content)


test("./../tests/example1/2019y01m12experts09h00.txt")


# print(numberClient("./../tests/example1/2019y01m12clients09h00.txt"))