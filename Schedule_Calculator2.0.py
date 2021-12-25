#Daily_Calculator

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

def gates_func(time_string):
    '''(str) -> [int, int]

    Returns the position of the ':' and the 'A', 'a', 'P', or 'p' in a time string.
    For these examples, we will have to use print to show the results, otherwise
    we would not see the results on screen.

    >>> gates_func('1:30 PM')
    [1,5]
    >>> gates_func('12:45PM')
    [2,5]
    >>> gates_func('3:07AM')
    [1,4]
    '''
    start_gate = time_string.find(':')
    am_pm = 'aApP'
    end_gate = 0
    for char in time_string:
        if char in am_pm:
            end_gate = time_string.find(char)
    return [start_gate, end_gate]
        
def start_time_func():
    '''' (none) -> [float, str]

    Returns a decimal time after the user inputs a time.
    Must give 'AM' or 'PM' with time to specify, otherwise
    the program gives an error.    
    '''
    start_time = input('What time did you start your shift?: ')
    start_gate = 0
    end_gate = 0
    while True:
        if start_time.find('a') != -1:
            start_gate = gates_func(start_time)[0]
            end_gate = gates_func(start_time)[1]
            break
        elif start_time.find('A') != -1:
            start_gate = gates_func(start_time)[0]
            end_gate = gates_func(start_time)[1]
            break
        elif start_time.find('p') != -1:
            start_gate = gates_func(start_time)[0]
            end_gate = gates_func(start_time)[1]
            break
        elif start_time.find('P') != -1:
            start_gate = gates_func(start_time)[0]
            end_gate = gates_func(start_time)[1]
            break
        else:
            print('Please specify AM or PM')
            start_time = input('What time did you start your shift?: ')
            
    hours = int(start_time[:start_gate]) % 12
    minutes = round(int(start_time[start_gate+1:end_gate]),2)
    if start_time.find('p') != -1 or start_time.find('P') != -1:
        hours = hours + 12    
    final_time = hours + round(minutes/60,2) 
    return [final_time, start_time]

def meal_time_func(start_time):
    ''' ([float, str]) -> [float, str]

    Will ask for starting and ending times of break and returns
    a float that is the decimal equivalent for how much time
    the user was gone. Also returns the end time (will be
    used to check against any inaccuracies for time outside of this
    function).
    '''
#    start_shift = start_time[1]
    start_meal = input('What time did you start your break? Hit enter if not on break: ')
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
            start_meal = input('What time did you start your break? Hit enter if not on break: ')
            if start_meal == '':
                skip_break = input('Did you skip break today?: ')
                if skip_break.find('n' or 'N') != -1:       #if you skipped break, your meal should be 0
                    total_time = 0.0
                    hours = datetime.datetime.now().time().hour
                    minutes = datetime.datetime.now().time().minute
                    if hours > 12:
                        end_meal = str(hours + ':' + minutes + 'PM')
                    else:
                        end_meal = str(hours + ':' + minutes + 'AM')
                    return [total_time,end_meal]
                else:                                       #if you did not skip break, but you did not start it (not on meal yet)
                    hours = datetime.datetime.now().time().hour
                    minutes = datetime.datetime.now().time().minute
                    minutes_decimal = round(datetime.datetime.now().time().minute/60,2)
                    total_time = hours + minutes_decimal
                    if hours > 12:
                        end_meal = str(hours%12 + ':' + minutes + 'PM')
                    else:
                        end_meal = str(hours + ':' + minutes + 'AM')
                    return [total_time,end_meal]
    else:



def end_time_func():
    ''' (none) -> [float, string]

    Takes in the user's input for their clock out punch and
    returns the decimal hour format of that time and the string containing
    the user's input.    
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

    if end_time == meal_time_func.end_meal:
        total = 0
    else:
        total = hour + minutes
    return total,end_time


start = start_time_func()
meal = meal_time_func()
end = end_time_func()

if meal > end - start:
    total = round(end - start - meal,2)

print('You worked ' + str(total) + ' hours today. You had a ' + str(meal) + ' hour long meal.')
    
