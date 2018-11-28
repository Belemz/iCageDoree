# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém
# 31955 Inês de Carvalho Fernandes Martins da Silva



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




print(numberClient("/Users/ClaudiaBelem/Google Drive (belem@campus.ul.pt)/FCUL - Informática/1º semestre/Fundamentos de programacao/Projeto/iCageDoree/tests/example1/2019y01m12clients09h00.txt"))