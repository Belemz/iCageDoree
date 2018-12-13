import dateTime as DT

#
# print(DT.addPeriodToTime(00, 00, 30))
# print(DT.addPeriodToTime(23, 29, 10))
# print(DT.addPeriodToTime(23, 29, 30))
# print(DT.addTime(23,29,50))
# print(DT.addPeriodToTime(23, 29, 1))


#
# print(DT.updateDate(2018, 11, 1, 1))
#
# print(DT.updateDate(2018, 11, 30, 30))
#
# print(DT.updateDate(2018, 11, 30, 1))
#
# print(DT.updateDate(2018, 11, 29, 1))
#
# print(DT.updateDate(2018, 11, 29, 720))

# test schedule writing
# FW.writeSchedule(FR.readClientsFile("./../tests_v2/example1/2019y01m12clients09h00.txt"))
# FW.writeExpertsFile(FR.readExpertsFile("./../tests_v2/example1/2019y01m12experts09h00.txt"))

# testto read clients File
# print(FR.readClientsFile("./../tests/example1/2019y01m12clients09h00.txt"))


# test to read expert file
# print(FR.readExpertsFile("./../tests/example1/2019y01m12experts09h00.txt"))


print("the most recent time is: ", DT.selectMostRecentTime("00:10", "00:10"))
print("the most recent time is: ", DT.selectMostRecentTime("00:05", "00:10"))
print("the most recent time is: ", DT.selectMostRecentTime("23:59", "12:10"))
print("the most recent time is: ", DT.selectMostRecentTime("05:10", "06:10"))
print("the most recent time is: ", DT.selectMostRecentTime("06:10", "05:10"))
print("the most recent time is: ", DT.selectMostRecentTime("00:10", "00:05"))
print("the most recent time is: ", DT.selectMostRecentTime("00:01", "23:59"))