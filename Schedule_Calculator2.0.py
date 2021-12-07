#Schedule_Calculator2.0

#-----------------------------------------------------------------------------------
# This code was written by Viktor Dominguez.
# Any questions can be answered at viktordmngz@yahoo.com
# Please include "CODING" in the subject line so I know it's not spam.
# This code is open for free use.
#
# This is an updated version of my original schedule calculator.
# This was written just for fun and for me and my coworkers, it is just for our
# overnight retail jobs. This code will take in times as inputs and return
# how much time was worked.
#------------------------------------------------------------------------------------

import datetime

def start_time_func():
    '''' (none) -> float

    Returns a decimal time after the user inputs a time.
    Must give 'AM' or 'PM' with time to specify, otherwise
    the program gives an error.    
    '''
    start_time = input('What time did you start your shift?: ')

    while True:
        if start_time.find('A') != -1:
            end_gate = start_time.find('A')
            break
        elif start_time.find('P') != -1:
            end_gate = start_time.find('P')
            break
        elif start_time.find('a') != -1:
            end_gate = start_time.find('a')
            break
        elif start_time.find('p') != -1:
            end_gate = start_time.find('p')
            break
        else:
            print('Please specify AM or PM.\n')
            start_time = input('What time did you start your shift?: ')
    # Need a way to loop back through these statements after this last line....
    # Use another function
    
   
    start_gate = start_time.find(':')
    hours = int(start_time[:start_gate]) % 12
    minutes = int(start_time[start_gate+1:end_gate])

    if start_time.find('p') != -1 or start_time.find('P') != -1:
        hours = hours + 12
    
    
    final_time = hours + round(minutes/60,2)
    
    return final_time

def meal_time_func():
    ''' (none) -> float

    Will ask for starting and ending times of break and returns
    a float that is the decimal equivalent for how much time
    the user was gone.    
    '''

    start_meal = input('What time did you start your break?: ')
    while True:
        if start_meal.find('A') != -1:
            end_gate = start_meal.find('A')
            break
        elif start_meal.find('P') != -1:
            end_gate = start_meal.find('P')
            break
        elif start_meal.find('a') != -1:
            end_gate = start_meal.find('a')
            break
        elif start_meal.find('p') != -1:
            end_gate = start_meal.find('p')
            break
        else:
            print('Please specify AM or PM.\n')
            start_meal = input('What time did you start your break?: ')
    
    end_meal = input("\nWhat time did you end your break?('N' for 'Not done'): ")
    if end_meal == 'N' or end_meal == 'n':
        print('You are still on break.')
        if datetime.datetime.now().time().hour >=12:
            end_meal = str(datetime.datetime.now().time().hour%12) + str(':') + str(datetime.datetime.now().time().minute) + str('PM')
        else:
            end_meal = str(datetime.datetime.now().time().hour%12) + str(':') + str(datetime.datetime.now().time().minute) + str('AM')
    
    

    while True:
        if end_meal.find('A') != -1:
            end_gate2 = end_meal.find('A')
            break
        elif end_meal.find('a') != -1:
            end_gate2 = end_meal.find('a')
            break
        elif end_meal.find('P') != -1:
            end_gate2 = end_meal.find('P')
            break
        elif end_meal.find('p') != -1:
            end_gate2 = end_meal.find('p')
            break
        else:
            print('Please specify AM or PM.\n')
            end_meal = input('What time did you end your break?: ')

    start_gate = start_meal.find(':')
    start_gate2 = end_meal.find(':')

    hour1 = int(start_meal[:start_gate]) % 12
    hour2 = int(end_meal[:start_gate2]) % 12

    if start_meal.find('p') != -1 or start_meal.find('P') != -1:
        hour1 = hour1 + 12

    if end_meal.find('p') != -1 or end_meal.find('P') != -1:
        hour2 = hour2 + 12


    minutes1 = round(int(start_meal[start_gate + 1: end_gate])/60,2)
    minutes2 = round(int(end_meal[start_gate2 + 1: end_gate2])/60,2)

    total_time = round((hour2 + minutes2) - (hour1 + minutes1),2)

    return total_time

def end_time_func():
    ''' (none) -> float

    Takes in the user's input for their clock out punch and
    returns the decimal hour format of that time.    
    '''
    end_time = input("When did you punch out? ('N' if not punched out yet): ")
    if end_time == 'N' or end_time == 'n':
        if datetime.datetime.now().time().hour >=12:
            end_meal = str(datetime.datetime.now().time().hour%12) + str(':') + str(datetime.datetime.now().time().minute) + str('PM')
        else:
            end_meal = str(datetime.datetime.now().time().hour%12) + str(':') + str(datetime.datetime.now().time().minute) + str('AM')
    

    while True:
        if end_time.find('a') != -1 or end_time.find('A') != -1:
            x = end_time.find('a')
            y = end_time.find('A')
            endgate = max(x,y)
            break
        elif end_time.find('p') != -1 or end_time.find('A') != -1:
            x = end_time.find('a')
            y = end_time.find('A')
            endgate = max(x,y)
            break
        else:
            print('Please specify AM or PM.\n')
            end_time = input("When did you punch out? ('N' if not punched out yet): ")
            
    startgate = end_time.find(':')
   
    hour = int(end_time[:startgate]) % 12
    if end_time.find('p') != -1 or end_time.find('P') != -1:
        hour = hour + 12

    minutes = round(int(end_time[startgate + 1: endgate])/60, 2)

    total = hour + minutes
    return total


start = start_time_func()
meal = meal_time_func()
end = end_time_func()

total = round(end - start - meal,2)

print('You worked ' + str(total) + ' hours today. You had a ' + str(meal) + ' hour long meal.')
    