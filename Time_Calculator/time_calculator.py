def add_time(start, duration):
    #hour
    #min
    #meridiem
    #colonpos
    #d_hour
    #d_min
    count = 0
    dayslater = None

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
    
    if (dayslater == None):
        new_time = str(hour) + ":" + str(min) + " " + meridiem
    else:
        new_time = str(hour) + ":" + str(min) + " " + meridiem + " " + dayslater

    return new_time

"""
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
"""

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