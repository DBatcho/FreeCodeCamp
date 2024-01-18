"""
Takes 2 parameters with an optional 3rd:
-a start time in hours:minutes with AM/PM (meridiem)
-a duration of time elapsed from start time in hours:minutes
-OPTIONAL: a day of the week

function will take parameters and output the new_time given the start time and duration of time given
-if a day has passed since start time output will add "next day" to output
-if multiple days passed since start time output will add "n days later", with n being the amount of days passed
-if a day is provided output will include the day of the week after duration
"""
def add_time(start, duration, day=None):

    #seperates the data from start time
    colonpos = start.find(':')
    hour = int(start[0:colonpos].strip())
    min = int(start[colonpos + 1:colonpos + 3].strip())
    meridiem = start[colonpos + 3:].strip()

    #seperates the data from duration time
    colonpos = duration.find(':')
    d_hour = int(duration[0:colonpos].strip())
    d_min = int(duration[colonpos + 1:].strip())

    #if day is provided assigns day variable to a number of corresponding day of the week
    if (day != None):
        day = Day_of_Week(day = day.lower())

    """
    AM_PMcount is used to determine the meridiem and how many days passed
    if AM_PMcount is even it is AM, if odd it is PM
    every 2 in AM_PMcount is a day
    """
    if (meridiem == "AM"):
        AM_PMcount = 0
    else:
        AM_PMcount = 1

    """
    Calculates the minutes after duration is included
    if greater then 60 removes 60 from minutes and adds 1 to hour
    """
    min = min + d_min
    if (min >= 60):
        min -= 60
        hour += 1
    
    #if minutes are single digit, adds a "0" to the front
    min = str(min)
    if (len(min) < 2):
        min = "0" + min

    """
    Calculates the hours after duration is included
    if hour is greater than 12, loop through hour removing 12 until hour < 12
    each loop adds 1 to AM_PMcount because 12 hours went by
    after loop is hour equals 12 add 1 to AM_PMcount
    """
    hour = hour + d_hour
    if (hour >= 12):
        while hour > 12:
            hour -= 12
            AM_PMcount += 1
        if (hour == 12):
            AM_PMcount += 1

    #if AM_PMcount == even: meridiem = AM; odd: meridiem = PM
    if (AM_PMcount % 2 == 0):
        meridiem = "AM"
    else:
        meridiem = "PM"
    
    #every 2 in AM_PMcount is a day
    numdays = AM_PMcount // 2

    """
    to find how many days passed find the remainder of numdays
    if greater than 7, remove 7 from day number plus days passed
    else (if less than 7), add day to the remainder of days
    pass the number to the Day_Of_Week function to get the corresponding day
    """
    if (day != None):
        if ((day + (numdays % 7)) > 7):
            day = day + (numdays % 7) - 7
        else:
            day = day + (numdays % 7)
        day = Day_of_Week(num = day)

    """
    if numdays is more than 2, change to "(n days later)"
    if numdays is >=1, change numdays to "(next day)"
    else numdays is None
    """
    if (numdays >= 2):
        numdays = "(" + str(numdays) + " days later)"
    elif (numdays >= 1):
        numdays = "(next day)"
    else:
        numdays = None
    
    #combines all the data for the correct output. Determines what should be included based on data given
    if ((day != None) and (numdays != None)):
        new_time = str(hour) + ":" + str(min) + " " + meridiem + ", " + day + " " + numdays
    elif (day != None):
        new_time = str(hour) + ":" + str(min) + " " + meridiem + ", " + day
    elif (numdays != None):
        new_time = str(hour) + ":" + str(min) + " " + meridiem + " " + numdays
    else:
        new_time = str(hour) + ":" + str(min) + " " + meridiem 

    return new_time

"""
Given one of the optional parameters:
function will return either the number assigned to the day or the day assigned to the number
"""
def Day_of_Week(num = None, day = None):
    if (num == None):
        if (day == "monday"):
            return 1
        elif (day == "tuesday"):
            return 2
        elif (day == "wednesday"):
            return 3
        elif (day == "thursday"):
            return 4
        elif (day == "friday"):
            return 5
        elif (day == "saturday"):
            return 6
        elif (day == "sunday"):
            return 7
        else:
            return None
    else:
        if (num == 1):
            return "Monday"
        elif (num == 2):
            return "Tuesday"
        elif (num == 3):
            return "Wednesday"
        elif (num == 4):
            return "Thursday"
        elif (num == 5):
            return "Friday"
        elif (num == 6):
            return "Saturday"
        elif (num == 7):
            return "Sunday"
        else:
            return None



#PASS
actual = add_time("3:30 PM", "2:12")
expected = "5:42 PM"
if (actual == expected):
    print ("PASS")
    print(actual)
    print(expected)
else:
    print ("FAIL")
    print (actual)
    print (expected)

#PASS
actual = add_time("11:55 AM", "3:12")
expected = "3:07 PM"
if (actual == expected):
    print ("PASS")
    print(actual)
    print(expected)
else:
    print ("FAIL")
    print (actual)
    print (expected)

#PASS
actual = add_time("9:15 PM", "5:30")
expected = "2:45 AM (next day)"
if (actual == expected):
    print ("PASS")
    print(actual)
    print(expected)
else:
    print ("FAIL")
    print (actual)
    print (expected)

#PASS
actual = add_time("11:40 AM", "0:25")
expected = "12:05 PM"
if (actual == expected):
    print ("PASS")
    print(actual)
    print(expected)
else:
    print ("FAIL")
    print (actual)
    print (expected)

#PASS
actual = add_time("2:59 AM", "24:00")
expected = "2:59 AM (next day)"
if (actual == expected):
    print ("PASS")
    print(actual)
    print(expected)
else:
    print ("FAIL")
    print (actual)
    print (expected)

#PASS
actual = add_time("11:59 PM", "24:05")
expected = "12:04 AM (2 days later)"
if (actual == expected):
    print ("PASS")
    print(actual)
    print(expected)
else:
    print ("FAIL")
    print (actual)
    print (expected)

#PASS
actual = add_time("8:16 PM", "466:02")
expected = "6:18 AM (20 days later)"
if (actual == expected):
    print ("PASS")
    print(actual)
    print(expected)
else:
    print ("FAIL")
    print (actual)
    print (expected)

#PASS
actual = add_time("5:01 AM", "0:00")
expected = "5:01 AM"
if (actual == expected):
    print ("PASS")
    print(actual)
    print(expected)
else:
    print ("FAIL")
    print (actual)
    print (expected)

#PASS
actual = add_time("3:30 PM", "2:12", "Monday")
expected = "5:42 PM, Monday"
if (actual == expected):
    print ("PASS")
    print(actual)
    print(expected)
else:
    print ("FAIL")
    print (actual)
    print (expected)

#PASS
actual = add_time("2:59 AM", "24:00", "saturDay")
expected = "2:59 AM, Sunday (next day)"
if (actual == expected):
    print ("PASS")
    print(actual)
    print(expected)
else:
    print ("FAIL")
    print (actual)
    print (expected)

#PASS
actual = add_time("11:59 PM", "24:05", "Wednesday")
expected = "12:04 AM, Friday (2 days later)"
if (actual == expected):
    print ("PASS")
    print(actual)
    print(expected)
else:
    print ("FAIL")
    print (actual)
    print (expected)

#PASS
actual = add_time("8:16 PM", "466:02", "tuesday")
expected = "6:18 AM, Monday (20 days later)"
if (actual == expected):
    print ("PASS")
    print(actual)
    print(expected)
else:
    print ("FAIL")
    print (actual)
    print (expected)