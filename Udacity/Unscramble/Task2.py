"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv ,operator
with open("texts.csv", 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("C:\\Users\\Usuario\\OneDrive\\Desktop\\calls.csv", 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def trackCallDuration(dictionary, phoneNumber, callDuration):
    if(dictionary.get(phoneNumber) == None):
        dictionary[phoneNumber] = callDuration
    else:
        dictionary[phoneNumber] = int(
            dictionary.get(phoneNumber)) + int(callDuration)
    return dictionary

dictionary = {}

for rows in calls:
    callers = rows[0]
    callRecievers = rows[1]
    timestamp = rows[2]
    callDuration = rows[3]

    dictionary = trackCallDuration(dictionary, callers, callDuration)
    dictionary = trackCallDuration(dictionary, callRecievers, callDuration)

longestCall = max(dictionary.items(), key = lambda x: int(x[1]))
print (f"{longestCall[0]} spent the longest time, {longestCall[1]} seconds, on the phone during September 2016.")
