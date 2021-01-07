from ics import Calendar
import re
import arrow
from ics.event import Event

def main():
    year = "2021"
    inputFileName = input("Please input the path of the input file: ")
    fp = None
    re_date = re.compile(r'[0-9]{1,2}\/[0-9]{1,2}')
    re_courseID = re.compile(r'([A-Z]{4}) ([0-9]{4})')
    re_type = re.compile(r'\( .{4} \)')
    courseID = ""
    courseName = ""
    courseType = ""
    courseDate = [[]]
    courseTime = [[]]
    courseLoc = [[]]
    weekDay = []
    c = Calendar()
    e = None
    jump = False
    try:
        fp = open(inputFileName, 'r')
        for line in fp:
            #print(line)
            if (re.match(re_courseID, line)):
                if e is not None or True:
                    #c.events.add(e)
                    e = None
                    courseDate.clear()
                    courseName = ""
                    courseID = ""
                    courseType = ""
                    weekDay = []
                    courseLoc.clear()
                    courseTime.clear()
                courseID = line[0:4] + line[5:9]
                courseName = line[10:-1]
                #print(courseID)
                #print(courseName)
            if (re.match(re_type, line)):
                courseType = line[-4:-1]
                courseDate.clear()
                courseTime.clear()
                courseLoc.clear()
                weekDay.clear()
                #print(courseType)
            if (re.match(re_date, line)):
                dates = re.findall(re_date,line)
                courseDate.append(dates)
                #print(formattedDates)
            if (re.match(r'Days:', line)):
                weekDay.append(line[6:-1])
                for i in range(len(courseDate)):
                    timeStr = fp.readline()
                    startTime = ""
                    endTime = ""
                    #print(timeStr)
                    if (re.search(r'\d{2}:\d{2}', timeStr)):
                        splittedStr = timeStr.split()
                        startTime = splittedStr[1]
                        endTime = splittedStr[3]
                    courseTime.append([startTime, endTime])
                    if i < len(courseDate) - 1: 
                        tempLine = fp.readline()
                        weekDay.append(tempLine[6:-1])
                for i in range(len(courseDate)):
                    locStr = fp.readline()[0:-1]
                    courseLoc.append(locStr)
                    fp.readline()
                #print(courseDate)
                #print(courseTime)
                #print(courseLoc)
                eventName = courseID + " - " + courseType
                eventDesc = courseID + " - " + courseName + " - " + courseType

                if jump is False:
                    print("The information of", courseID, "has been loaded:")
                    print("1. EVENT TITLE: ", eventName)
                    print("2. EVENT DESCRIPTION: ", eventDesc)
                    choice = input("You can enter the index to change the information ,enter 0 to continue or enter 3 to jump over all selections: ")
                    while choice != "0":
                        if choice == "1":
                            eventName = input("Please provide the event title: ")
                            choice = input("You can enter the index to change the information or enter 0 to continue: ")
                        elif choice == "2":
                            eventDesc = input("Please provide the event Description: ")
                            choice = input("You can enter the index to change the information or enter 0 to continue: ")
                        elif choice == "3":
                            jump = True
                            break
                        else:
                            choice = input("Please enter a valid input: ")

                for i in range(len(courseDate)):
                    #print(weekDay[i])
                    for j in range(len(courseDate[i])):
                        startStr = year + '/' + courseDate[i][j] + ' ' + courseTime[i][0]
                        endStr = year + '/' + courseDate[i][j] + ' ' + courseTime[i][1]
                        startArrow = arrow.get(startStr, 'YYYY/M/D HH:mm', tzinfo="+08:00")
                        endArrow = arrow.get(endStr, 'YYYY/M/D HH:mm', tzinfo="+08:00")
                        e = Event(name=eventName, begin=startArrow, end=endArrow, location=courseLoc[i], description=eventDesc)
                        c.events.add(e)
        print("All events have been added to calendar.")
        outputFileName = input("Please input the name of the output file(Without format): ")
        with open(outputFileName + ".ics", 'w') as f:
            f.write(str(c))          
                    

    except FileNotFoundError:
        print("File not found")
    finally:
        if fp:
            fp.close()

    re.match(re_date,"1/11, 1/18, 1/25, 2/1, 2/8, 2/22, 3/1, 3/8, 3/15, 3/22, 4/12, 4/19")

if __name__ == '__main__':
    main()