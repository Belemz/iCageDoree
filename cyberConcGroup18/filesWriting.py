# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém
# 31955 Inês de Carvalho Fernandes Martins da Silva



def createHeader(fileName, day, time, company, scope):
    """
    Creates a header containing the day, time, company and scope of a file.
    Requires: param day: is date in the format yyyy-mm-dd,
              time: is time in the format hh:mm
              company: is str
              scope: is string
    Returns: creates a header with each parameter in different lines and preceded (in the line before) with the
     type of parameter
    """


    fileName.write("Day:\n")
    fileName.write(day)
    fileName.write("\nTime:\n")
    fileName.write(time)
    fileName.write("\nCompany:\n")
    fileName.write(company)
    fileName.write("\n")
    fileName.write(scope)






def writeSchedule():
    """
    Write a file with the scheduling


    #to complete!

    """


    newFile = open("/Users/ClaudiaBelem/PycharmProjects/iCageDoree/tests/example1/2018y10m22schedule21h00.txt", "w")

    # FALTA DEFINIR: DAY, TIME, COMPANY, SCOPE - INCOMPLETE!

    createHeader(newFile, day,time,company,scope)   # Header is created!

    newFile.write("\n ")                            #
    newFile.write ( "\nA Carlota também!" )

    newFile.close()

    """
    Na calendarização do atendimento dos pedidos de contratação, a seguir ao cabeçalho, cada linha corresponde ao 
    atendimento de um pedido calendarizado (cujos elementos informativos estão separados por vírgulas) estando a
    listagem ordenada por ordem crescente do momento de atendimento.
    Cada atendimento calendarizado é caracterizado pela data (e.g. 2018-10- 30) e hora de início (e.g. 16:00), pelo
    nome do cliente que fez o pedido (e.g. Maria Schwartz), e pelo nome do especialista que vai responder a esse 
    pedido (e.g. Maciej Salawa), como ilustrado no seguinte exemplo:
    
                2018-10-30, 16:00, Maria Schwartz, Maciej Salawa
    """

print(writeSchedule())