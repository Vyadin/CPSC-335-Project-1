import re

def parseText(rawinput):

    print("Raw input:")
    print(rawinput)
    print()

    newInput = []

    for i in range(len(rawinput)):
        newInput.append(rawinput[i].strip('\n').strip("\""))

    newInput[:] = [x for x in newInput if x != '']

    print("\nSTRIPPING\n")

    for i in range(len(newInput)):
        newInput[i] = re.sub('[^0-9:,]', '', newInput[i])
        print(newInput[i])

    print("\nFINAL RESULT\n")

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
    runtype = input("Would you like to run the 10 test cases or enter your own input? [Type TEST or ENTER]: ")
    if runtype != "TEST" and runtype != "ENTER":
        print("Please enter either TEST or ENTER below.")
        startProgram()
    elif runtype == "TEST":
        runTestCases()
    elif runtype == "ENTER":
        runFromInput()

startProgram()