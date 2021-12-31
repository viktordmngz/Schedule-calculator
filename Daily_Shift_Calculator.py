#Daily_Calculator2.02

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
from sys import exit

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
    num_hour = '012'
    if start_time.find(':') == -1 and len(start_time) >= 3:
        if start_time[0] == '1':
            if start_time[1] in num_hour:
                start_time = start_time[:2] + ':' + start_time[2:]
        else:
            start_time = start_time[0] + ':' + start_time[1:]
    if start_time.find(':') == -1:
        if start_time.lower().find('a') != -1 or start_time.lower().find('p') != -1:
            start_time = start_time.strip()[:gates_func(start_time)[1]] + ':00 ' + start_time[gates_func(start_time)[1]:]
        else:
            start_time = start_time + ':00'
    while start_time.lower().find('a') == -1 and start_time.lower().find('p') == -1:
        start_time = start_time + ' ' + input('Please specify AM or PM: ')
    hours = int(start_time[:gates_func(start_time)[0]])
    minutes = int(start_time[gates_func(start_time)[0]+1:gates_func(start_time)[1]])
    final_time = round(hours + minutes/60,2)
    return[final_time,start_time]

start_shift_vals = start_time_func()
start_shift = start_shift_vals[0]
start_shift_str = start_shift_vals[1]
def start_meal_func(start_time):
    '''(float) -> [flloat, string]

    Takes in user input to determine when the start of the meal has taken place.
    3 Scenarios: The user is not on break yet, the user started break but has not ended break yet, the user skipped break.    
    '''
    num_hour = '012'
    start_meal = input('\nWhat time did you start your break? Hit enter if you did not start one: ')
    if start_meal == '':
        skipped = input('Did you skip your break?: ')
    #### if the user did not skip break but has not entered a start meal time: user has not taken a break yet
        if skipped.lower().find('n') != -1:
            hours = datetime.datetime.now().time().hour
            minutes = datetime.datetime.now().time().minute
            final_time = round(hours + minutes/60 - start_time,2)
            print("\nYou are currently still on the clock. Your shift is currently at " + str(final_time) + ' hour(s) worked.')
            quit()
    #### if the user skipped break, start meal should return a 0 as should the end meal function
        else:
            final_time = 0.00
            return[final_time,start_meal]
    #### if the user entered a start meal time
    else:
        if start_meal.find(':') == -1 and len(start_meal) >= 3:
            if start_meal[0] == '1':
                if start_meal[1] in num_hour and len(start_meal) > 3:
                    start_meal = start_meal[:2] + ':' + start_meal[2:]
            else:
                start_meal = start_meal[:1] + ':' + start_meal[1:]
        if start_meal.find(':') == -1:
            if start_meal.lower().find('a') != -1 or start_meal.lower().find('p') != -1:
                start_meal = start_meal.strip()[:gates_func(start_meal)[1]] + ':00 ' + start_meal[gates_func(start_meal)[1]:]
            else:
                start_meal = start_meal + ':00'
        while start_meal.lower().find('a') == -1 and start_meal.lower().find('p') == -1:
            start_meal = start_meal + ' ' + input('Please specify AM or PM: ')
        hours = int(start_meal[:gates_func(start_meal)[0]])
        minutes = int(start_meal[gates_func(start_meal)[0] + 1: gates_func(start_meal)[1]])
        if start_meal.lower().find('p') != -1:
            hours = hours+12
        final_time = round(hours + minutes/60,2)
        return[final_time, start_meal]

#### Decimal starting time of break (will be 0 if skipped)
#### Should run once               
start_break_vals = start_meal_func(start_shift)
start_break = start_break_vals[0]
start_break_str = start_break_vals[1]

def end_meal_func(start_meal):
    '''(float) -> [float,string]

    Returns a list with the decimal end-time of meal and the string to represent it.
    3 cases:    end meal has not been entered in but start time is not 0 -> still on break, return the current time as end
                end meal has not been entered in and start time is 0 -> Skipped meal, end should also equal 0
                end meal is entered (must make sure it is >= 30minutes past start meal) -> end will be what user input.
    '''
    num_hour = '012'
    if start_meal == 0:
        final_time = 0
        return[final_time, None]
    end_meal = input('\nWhat time did you end your break? Hit enter if you did not end it: ')
    #### if user started meal but has not ended it, current time will be used as end
    if end_meal == '':
        hours = datetime.datetime.now().time().hour
        minutes = datetime.datetime.now().time().minute
        final_time = round(hours + minutes/60,2)
        print('\nYou are still on break. Your break currently is ' + str(final_time) + ' hours long.')
        if final_time < start_meal:
            print("\nYou have made an error entering in your times. Please try again.")
            quit()
        return[final_time, None]
    else:
        if end_meal.find(':') == -1 and len(end_meal) >= 3:
            if end_meal[0] == '1':
                if end_meal[1] in num_hour and len(end_meal) > 3:
                    end_meal = end_meal[:2] + ':' + end_meal[2:]
            else:
                end_meal = end_meal[:1] + ':' + end_meal[1:]
        if end_meal.find(':') == -1:        
            if end_meal.lower().find('a') != -1 or end_meal.lower().find('p') != -1:
                end_meal = end_meal.strip()[:gates_func(end_meal)[1]] + ':00 ' + end_meal[gates_func(end_meal)[1]:]
            else:
                end_meal = end_meal + ':00'
        while end_meal.lower().find('a') == -1 and end_meal.lower().find('p') == -1:
            end_meal = end_meal + ' ' + input('Please specify AM or PM: ')
        hours = int(end_meal[:gates_func(end_meal)[0]])
        minutes = int(end_meal[gates_func(end_meal)[0]+1: gates_func(end_meal)[1]])
        if end_meal.lower().find('p') != -1:
            hours = hours+12
        final_time = round(hours + minutes/60,2)
        if final_time - start_meal < .5:
            print('\nYou have made an error entering your time (breaks must be minumum of 30 minutes). Please try again.')
            quit()
    return[final_time, end_meal]
#### Decimal ending time of break (will be 0 if skipped)
#### If end meal is not entered but start meal was, set the end time to end meal

end_break_vals = end_meal_func(start_break)
end_break = end_break_vals[0]
end_break_str = end_break_vals[1]

if end_break > 0 and end_break_str == None:
    print('\nYour shift is currently ' + str(start_break - start_shift) + ' hours long.')
    quit()


def end_time_func(full_meal, start_meal, start_shift):
    '''(float, string, float) -> [float, string]

    Takes in the user's input for their clock out punch and
    returns the decimal hour format of that time and the string containing
    the user's input.    
    '''
    num_hour = '012'
    end_time = input('\nWhat time did you end your shift? Hit enter if you still are on the clock: ')
    #### if no end time is put in, the user must still be on the clock. The current time will be used as the end
    if end_time == '':
        hours = datetime.datetime.now().time().hour
        minutes = datetime.datetime.now().time().minute
        final_time = round(hours + minutes/60,2)
        if hours >=12:
            hours = hours % 12
            end_time_str = str(hours) + ':' + str(minutes) + ' PM'
        else:
            end_time_str = str(hours) + ':' + str(minutes) + ' AM'
    #### if full_meal = 0, meal was skipped. Subtract the start_time from the entered end time for the shift.
        if full_meal == 0:
            print('\nYour shift currently is this long: ' + str(final_time-start_shift))
            quit()
        else:
    #### need to test the case where a start meal time was entered but not an end meal
    #### need to skip the end shift function or pass through our end meal time as the end shift time.
            print('\nYour break is currently this long: ' + str(final_time))
            print('\nYour shift is currently this long: ' + str(start_meal - start_shift))
            quit()
    else:
        if end_time.find(':') == -1 and len(end_time) >= 3:
            if end_time[0] == '1':
                if end_time[1] in num_hour and len(end_time) > 3:
                    end_time = end_time[:2] + ':' + end_time[2:]
            else:
                end_time = end_time[:1] + ':' + end_time[1:]
        if end_time.find(':') == -1:
            if end_time.lower().find('a') != -1 or end_time.lower().find('p') != -1:
                end_time = end_time.strip()[:gates_func(end_time)[1]] + ':00 ' + end_time[gates_func(end_time)[1]:]
            else:
                end_time = end_time + ':00'
        while end_time.lower().find('a') == -1 and end_time.lower().find('p') == -1:
            end_time = end_time + ' ' + input('Please specify AM or PM: ')
        hours = int(end_time[:gates_func(end_time)[0]])
        minutes = int(end_time[gates_func(end_time)[0] + 1: gates_func(end_time)[1]])
        if end_time.lower().find('p') != -1:
            hours = hours + 12
        final_time = round(hours + minutes/60,2)
        return[final_time,end_time]

full_break_vals = [start_break, end_break]
full_break = end_break - start_break
full_break_str = [start_break_str, end_break_str]


end_shift_vals = end_time_func(full_break, start_break, start_shift)
end_shift = end_shift_vals[0]
end_shift_str = end_shift_vals[1]

full_shift = round((end_shift - end_break) + (start_break - start_shift),2)
print("\nYour shift was " + str(full_shift) + " hours long. Your meal was " + str(full_break) + " hours long.")
#### if meal is skipped, the program will exit before it gets to this step.
#### meal should not count toward shift length.
