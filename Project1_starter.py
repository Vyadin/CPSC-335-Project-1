from datetime import datetime, timedelta
import re

# Global format for input times
timeFormat = "%H:%M"

# Input and output files
inputFile = open("input.txt", 'r')
rawinput = inputFile.readlines()

outputFile = open("Output.txt", 'w')
outputFile.flush()

def findSchedule(schedule1, login1, schedule2, login2, minTime):
    # Convert meeting time to TimeDelta
    minTime = timedelta(minutes=(int(float(minTime[0]))))

    outputFile.write("Person 1's schedule: " + str(schedule1).replace('\', \'', '-') + "\n")
    outputFile.write("Person 1's login time: " + str(login1).replace('\', \'', '-') + "\n")
    outputFile.write("Person 2's schedule: " + str(schedule2).replace('\', \'', '-') + "\n")
    outputFile.write("Person 2's login time: " + str(login2).replace('\', \'', '-') + "\n")
    outputFile.write("Minimum meeting length: " + str(int(minTime.seconds/60)) + " minutes."  + "\n\n")

    # Append login times to schedules
    schedule1.insert(0, [login1[0][0], login1[0][0]])
    schedule1.append([login1[0][1], login1[0][1]])

    schedule2.insert(0, [login2[0][0], login2[0][0]])
    schedule2.append([login2[0][1], login2[0][1]])

    compatibleTimes = []

    timeFound = False

    # Algorithm begins here
    for i in range((len(schedule1)-1)):
        time1Start = datetime.strptime(schedule1[i][1], timeFormat)
        time1End = datetime.strptime(schedule1[i+1][0], timeFormat)
        time1span = time1End - time1Start
        for j in range(len(schedule2)-1):
            time2Start = datetime.strptime(schedule2[j][1], timeFormat)
            time2End = datetime.strptime(schedule2[j+1][0], timeFormat)
            time2span = time2End - time2Start
            
            if time1Start < time2End and time1End >= time2Start and time1span >= minTime and time2span >= minTime:

                startTime = max(time1Start, time2Start)
                endTime = min(time1End, time2End)

                if endTime - startTime < minTime:
                    continue

                meetingTime = startTime.strftime("%H:%M") + "-" + endTime.strftime("%H:%M")
                compatibleTimes.append(meetingTime)

                timeFound = True

    if not timeFound:
        outputFile.write("[Notice] No compatible times found.\n")
    else:
        outputFile.write("+------------------+\n")
        outputFile.write("| Compatible Times | ")
        for i in range(len(compatibleTimes)):
            outputFile.write(compatibleTimes[i])
            if i != len(compatibleTimes)-1:
                outputFile.write(", ")
        outputFile.write("\n+------------------+\n")

    outputFile.write("\n")

# I kinda dug myself into a hole while parsing the files so here's how it's formatted
# start and end times are split into separate indices (Schedule[i][0] is 7:00, Schedules[i][1] is 8:30, etc)
# Schedule[0] is a list of the times the first person is busy (e.g. 7:00-8:30)
# Schedule[1] is the time they're logged in all day (e.g. their work day, we can't go past these values)
# Schedule[2] is a list of times the second person is busy
# Schedule[3] is the second person's login time
# Schedule[4] is the minimum time we need to find a meeting for
# Schedule[5] is just the newline separating the inputs in input.txt for readability

def parseSchedule(schedule):
    for i in range(len(schedule)):
        schedule[i] = re.sub("[^0-9,-:]", "", schedule[i]) # Remove all characters except numbers, commas, dashes and colons
        schedule[i] = schedule[i].strip()
        schedule[i] = schedule[i].split(",") # Separate busy times

        if i != 4:
            for j in range(len(schedule[i])):
                schedule[i][j] = schedule[i][j].split("-") # Separate busy start time and busy end time
    findSchedule(schedule[0], schedule[1], schedule[2], schedule[3], schedule[4])

# Run the program once for each section of input (Separated by newline)
def parseFile(rawinput):

    schedule = []

    runNumber = 1

    for i in range(len(rawinput)):

        schedule.append(rawinput[i])

        if (rawinput[i] == '\n' or rawinput[i] == ''):
            outputFile.write("=================================\n")
            outputFile.write("           Example " + str(runNumber) + "\n")
            outputFile.write("=================================\n\n")
            parseSchedule(schedule)
            schedule.clear()
            runNumber += 1

# Run program
parseFile(rawinput)
print("[Notice] Program completed.")