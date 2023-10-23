import re
from datetime import datetime, timedelta

def parseText(rawinput):

    print("Raw input:")
    print(rawinput)
    print()

    newInput = []

    for i in range(len(rawinput)):
        newInput.append(rawinput[i].strip("\n\'[],").split(" | "))

    print("NEWINPUT:")
    print(newInput)

    #print("\nSPLIT AGAIN")

    #for i in range(len(newInput)):
    #    print("i: " + str(newInput[i]))
    #    for j in range(len(newInput[i])):
    #        newInput[i][j].split("]")
    #        print("new j: " + str(newInput[i][j]))
    #        newInput[i][j].split("]")
    #        print("FINAL j:" + str(newInput[i][j]))

    print(newInput)

    #!newInput[:] = [x for x in newInput if x != '']

    print("\nFormatting numbers...\n")

    for i in range(len(newInput)):
        print("Test " + str(i+1) + ":")
        for j in range(len(newInput[i])):
            newInput[i][j] = re.sub('[^0-9:,]', '', newInput[i][j])
            print(newInput[i][j])
        print()

    print("\nFinal results:\n")

    for i in range(len(newInput)):
        print(newInput[i])

#! =========================================

def runTestCases():
    file = open("input.txt", 'r')
    rawinput = file.readlines()
    parseText(rawinput)


def runFromInput():
    person1_schedule = input("Enter Person 2's Schedule: ")
    person1_active = input("Enter Person 1's Active Time: ")

    print()

    person2_schedule = input("Enter Person 2's Schedule: ")
    person2_active = input("Enter Person 2's Active Time: ")

    print()

    meeting_duration = input("Enter meeting duration: ")

    rawinput = [person1_schedule, person1_active, person2_schedule, person2_active, meeting_duration]
    parseText(rawinput)

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