from datetime import datetime, timedelta
import re
import math

# Global format for input times
timeFormat = "%H:%M"

# Here is how I have it formatted so far:
# start and end times are split into separate indices (Schedules[i][0] is 7:00, Schedules[i][1] is 8:30, etc)
# Schedule[0] is a list of the times the first person is busy (e.g. 7:00-8:30)
# Schedule[1] is the time they're logged in all day (e.g. their work day, we can't go past these values)
# Schedule[2] is a list of times the second person is busy
# Schedule[3] is the second person's login time
# Schedule[4] is the minimum time we need to find a meeting for
# Schedule[5] is just the newline separating the inputs in input.txt for readability

def findSchedule(schedule1, login1, schedule2, login2, minTime):
    #Convert meeting time to TimeDelta
    minTime = timedelta(minutes=(int(float(minTime[0]))))

    print("Person 1's schedule: " + str(schedule1).replace('\', \'', '-'))
    print("Person 1's login time: " + str(login1).replace('\', \'', '-'))
    print("Person 2's schedule: " + str(schedule2).replace('\', \'', '-'))
    print("Person 2's login time: " + str(login2).replace('\', \'', '-'))
    print("Minimum meeting length: " + str(int(minTime.seconds/60)) + " minutes.")

    #Append login times to schedules
    schedule1.insert(0, [login1[0][0], login1[0][0]])
    schedule1.append([login1[0][1], login1[0][1]])

    schedule2.insert(0, [login2[0][0], login2[0][0]])
    schedule2.append([login2[0][1], login2[0][1]])

    compatibleTimes = []

    timeFound = False

    for i in range((len(schedule1)-1)):
        #print("\nAvailable time " + str(i+1) + ": ")
        time1Start = datetime.strptime(schedule1[i][1], timeFormat)
        time1End = datetime.strptime(schedule1[i+1][0], timeFormat)
        time1span = time1End - time1Start
        #print(str(time1Start.time()) + "-" + str(time1End.time()))
        #print("Time1span: " + str(time1span))
        #print("=====")
        for j in range(len(schedule2)-1):
            time2Start = datetime.strptime(schedule2[j][1], timeFormat)
            time2End = datetime.strptime(schedule2[j+1][0], timeFormat)
            #print(str(time2Start.time()) + "-" + str(time2End.time()))
            time2span = time2End - time2Start
            #print("Time2span: " + str(time2span))
            
            if time1Start < time2End and time1End >= time2Start and time1span >= minTime and time2span >= minTime:

                startTime = max(time1Start, time2Start)
                endTime = min(time1End, time2End)

                if endTime - startTime < minTime:
                    continue

                meetingTime = startTime.strftime("%H:%M") + "-" + endTime.strftime("%H:%M")

                #print("=========")
                #print("Possible meeting time: " + meetingTime)
                #print("=========")

                compatibleTimes.append(meetingTime)
                #print("Compatible times: " + str(compatibleTimes))

                timeFound = True

    if not timeFound:
        print("\n[Notice] No compatible times found.\n")
    else:
        print("\n+------------------+")
        print("| Compatible Times | ", end="")
        for i in range(len(compatibleTimes)):
            print(compatibleTimes[i], end="")
            if i != len(compatibleTimes)-1:
                print(", ", end="")

        print()
        print("+------------------+\n")
        
            


def parseSchedule(schedule):
    for i in range(len(schedule)):
        schedule[i] = re.sub("[^0-9,-:]", "", schedule[i]) # Remove all characters except numbers, commas, dashes and colons
        schedule[i] = schedule[i].strip()
        schedule[i] = schedule[i].split(",") # Separate busy times

        if i != 4:
            for j in range(len(schedule[i])):
                schedule[i][j] = schedule[i][j].split("-") # Separate busy start time and busy end time
    
    #for L in range(len(schedule)):
    #    print("Schedule[" + str(L) + "]: " + str(schedule[L]))
    findSchedule(schedule[0], schedule[1], schedule[2], schedule[3], schedule[4])

# Run the program once for each section of input (5 lines per input in input.txt)
def parseFile(rawinput):

    schedule = []

    for i in range(len(rawinput)):
        #print("I: " + str(i))
        #print("Appending: " + rawinput[i])
        schedule.append(rawinput[i])
        if (rawinput[i] == '\n'):
            print("=================================")
            print("Starting algorithm for example " + str(int(i/5)))
            print("=================================\n")
            parseSchedule(schedule)
            schedule.clear()

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

runTestCases()
