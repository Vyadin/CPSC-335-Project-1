from datetime import datetime, timedelta
import re

# Global format for input times
timeFormat = "%H:%M"

# Here is how I have it formatted so far:
# start and end times are split into separate indices (Schedules[i][0] is 7:00, Schedules[i][1] is 8:30, etc)
# Schedules[0] is a list of the times the first person is busy (e.g. 7:00-8:30)
# Schedules[1] is the time they're logged in all day (e.g. their work day, we can't go past these values)
# Schedules[2] is a list of times the second person is busy
# Schedules[3] is the second person's login time
# Schedules[4] is the minimum time we need to find a meeting for
# Schedules[5] is just the newline separating the inputs in input.txt for readability

def parseSchedule(schedule):
    for i in range(len(schedule)):
        schedule[i] = re.sub("[^0-9,-:]", "", schedule[i]) # Remove all characters except numbers, commas, dashes and colons
        schedule[i] = schedule[i].strip()
        schedule[i] = schedule[i].split(",") # Separate busy times

        if i != 4:
            for j in range(len(schedule[i])):
                schedule[i][j] = schedule[i][j].split("-") # Separate busy start time and busy end time

        print("Schedules[" + str(i) + "]: " + str(schedule[i]))

# Run the program once for each section of input (5 lines per input in input.txt)
def parseFile(rawinput):

    schedule = []

    for i in range(len(rawinput)):
        schedule.append(rawinput[i])
        if i%5 == 0 and i != 0:
            parseSchedule(schedule)
            schedule = []

    # Old code showing an example of how to find the timespans
    #for i in range(len(schedule)-1):
    #    time1 = datetime.strptime(schedule[i][1], timeFormat)
    #    print("Time 1: " + str(time1))
    #    time2 = datetime.strptime(schedule[i+1][0], timeFormat)
    #    print("Time 2: " + str(time2))
    #
    #   timeDelta = time2-time1
    #    print(timeDelta.seconds/60)
    #    i += 2

# Take input from file
def runTestCases():
    file = open("input.txt", 'r')
    rawinput = file.readlines()
    parseFile(rawinput)

# Take input from user
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
