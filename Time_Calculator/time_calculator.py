def add_time(start, duration, day=None):
    #hour
    #min
    #meridiem
    #colonpos
    #d_hour
    #d_min
    count = 0
    dayslater = None

    if (day != None):
        day = Day_of_Week(day = day.lower())
        print (day)

    colonpos = start.find(':')
    hour = int(start[0:colonpos].strip())
    min = int(start[colonpos + 1:colonpos + 3].strip())
    meridiem = start[colonpos + 3:].strip()

    print ("Start Time:")
    print (hour)
    print (min)
    print (meridiem)


    colonpos = duration.find(':')
    d_hour = int(duration[0:colonpos].strip())
    d_min = int(duration[colonpos + 1:].strip())

    print ("Duration Time:")
    print (d_hour)
    print (d_min)
 

    if (meridiem == "PM"):
        count += 1

    min = min + d_min
    if (min >= 60):
        min -= 60
        hour += 1

    hour = hour + d_hour
    print (hour)
    if (hour > 12):
        while hour > 12:
            hour -= 12
            count += 1
    
    if (hour == 12):
        count += 1

    if (count % 2 == 0):
        meridiem = "AM"
    else:
        meridiem = "PM"
    
    if (count >= 4):
        dayslater = "(" + str(count//2) + " days later)"
    elif (count >= 2):
        dayslater = "(next day)"

    min = str(min)
    if (len(min) < 2):
        min = "0" + min

    if (day != None):
        if ((day + ((count // 2) % 7)) > 7):
            day = day + ((count // 2) % 7) - 7
        else:
            day = day + ((count // 2) % 7)
        day = Day_of_Week(num = day)
    
    if ((day != None) and (dayslater != None)):
        new_time = str(hour) + ":" + str(min) + " " + meridiem + ", " + day + " " + dayslater
    elif (day != None):
        new_time = str(hour) + ":" + str(min) + " " + meridiem + ", " + day
    elif (dayslater != None):
        new_time = str(hour) + ":" + str(min) + " " + meridiem + " " + dayslater
    else:
        new_time = str(hour) + ":" + str(min) + " " + meridiem 

    return new_time

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