from datetime import datetime, timedelta
import re

# Global format for input times
timeFormat = "%H:%M"

def parseSchedule(schedule):
    for i in range(len(schedule)):
        schedule[i] = re.sub("[^0-9,-:]", "", schedule[i])
        schedule[i] = schedule[i].strip()
        schedule[i] = schedule[i].split(",")

        if i != 4:
            for j in range(len(schedule[i])):
                schedule[i][j] = schedule[i][j].split("-")

        print("Schedules[" + str(i) + "]: " + str(schedule[i]))

def parseFile(rawinput):

    schedule = []

    for i in range(len(rawinput)):
        schedule.append(rawinput[i])
        if i%5 == 0 and i != 0:
            print("5 lines passed")
            parseSchedule(schedule)
            schedule = []

    #for i in range(len(schedule)-1):
    #    time1 = datetime.strptime(schedule[i][1], timeFormat)
    #    print("Time 1: " + str(time1))
    #    time2 = datetime.strptime(schedule[i+1][0], timeFormat)
    #    print("Time 2: " + str(time2))
    #
    #   timeDelta = time2-time1
    #    print(timeDelta.seconds/60)
    #    i += 2

def runTestCases():
    file = open("input.txt", 'r')
    rawinput = file.readlines()
    parseFile(rawinput)


def runFromInput():
    person1_schedule = input("Enter Person 2's Schedule: ")
    person1_active = input("Enter Person 1's Active Time: ")

    print()

    person2_schedule = input("Enter Person 2's Schedule: ")
    person2_active = input("Enter Person 2's Active Time: ")

    print()

    meeting_duration = input("Enter meeting duration: ")

    rawinput = [person1_schedule, person1_active, person2_schedule, person2_active, meeting_duration]
    parseFile(rawinput)

def startProgram():
    runtype = input("Would you like to run the 10 test cases or enter your own input? [Type Test or Enter]: ")
    runtype = runtype.lower()

    match runtype:
        case "test":
            runTestCases()
        case "enter":
            runFromInput()
        case _:
            print("Please enter either Test or Enter.")
            startProgram()

startProgram()