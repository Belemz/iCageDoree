# 2018-2019 Fundamentos de Programação
# Grupo 18
# 44605 Cláudia Garcia Belém
# 31955 Inês de Carvalho Fernandes Martins da Silva


import constants

def createHeader(fileOut , tuple):
    """
    Creates a header containing the day, time, company and scope of a file.
    Requires: param day: is date in the format yyyy-mm-dd,
              time: is time in the format hh:mm
              company: is str
              scope: is string
    Returns: creates a header with each parameter in different lines and preceded (in the line before) with the
     type of parameter
    """

    day, time, company, scope = tuple     # tuple unpacking

    fileOut.write( "Day:\n" )
    fileOut.write( day )
    fileOut.write( "\nTime:\n" )
    fileOut.write( time )
    fileOut.write( "\nCompany:\n" )
    fileOut.write( company )
    fileOut.write( "\n" )
    fileOut.write( scope )
    fileOut.write( "\n" )




def writeExpertsFile(content):
    """

    #

    # todo
    """
    print(content)

    fileOut = open ( "../debug/ficheiroqualquer.txt" , "w" )

    createHeader(fileOut, content[0])    # todo colocar nas constantes

    for iterator in range (1, len(content)):

        element = content[iterator]        # each element of the list received from content

        # print("este é o elemento:", element)

        elementStr = convertExpertsDictToString(element)    # dictionary values transformed to Str per expert

        print("elemento em String", elementStr)

        fileOut.write(elementStr + "\n")



    fileOut.close()





def convertExpertsDictToString (expertsDict):
    """

    # todo
    """

    expertsString =  expertsDict.get(constants.expertsDictKeyName) + "," +\
                     expertsDict.get(constants.expertsDictKeyLocation) + "," + \
                     expertsDict.get(constants.expertsDictKeySpecialty) + "," +\
                     expertsDict.get(constants.expertsDictKeyReview) + "," + \
                     expertsDict.get(constants.expertsDictKeyCost) + "," + \
                     expertsDict.get(constants.expertsDictKeyService) + "," + \
                     expertsDict.get(constants.expertsDictKeyAvailability) + "," + \
                     expertsDict.get(constants.expertsDictKeyMoney)

    return expertsString

def writeSchedule():
    """
    Write a file with the scheduling


    #todo contract

    """


    # newFile = open("./../tests/example1/2018y10m22schedule21h00.txt", "w")

    # FALTA DEFINIR: DAY, TIME, COMPANY, SCOPE - INCOMPLETE!

   # createHeader(newFile, day,time,company,scope)   # Header is created!




    # newFile.write(date, ",", time, ",", client_name, ",", expert_name)                            #
    # newFile.write ()

    # newFile.close()


# print(writeSchedule())


# writeExpertsFile()