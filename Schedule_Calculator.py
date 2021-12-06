# Schedule calculator

def remaining_time(num):
    ''' (number) -> float
    Returns the amount of time in hours (and decimal)
    left in a 40 hour week.

    >>> remaining_time(24)
    16.00
    >>> remaining_time(25.99)
    14.01
    >>> remaining_time(15.3)
    24.70
    '''
    return round(40-num,2)

def get_hours(num):
    '''(number) -> int
    
    Return the hour portion given the time
    in hours (can be a decimal).

    >>> get_hours(.99)
    0
    >>> get_hours(15.9)
    15
    '''
    return int(num)

def get_minutes(num):
    '''(number) -> int

    Return the amount of minutes given the
    number of hours (can be a decimal).

    >>> get_minutes(15.5)
    30
    >>> get_minutes(29)
    0
    >>> get_minutes(45.15)
    9
    '''
    minutes = num - get_hours(num)
    return int(minutes*60)

my_time = round(float(input('How much have you worked so far?: ')),2)
num_days_worked = int(input('How many days have you worked so far?: '))

def work_per_day(work_time, days):
    '''' (number, integer) -> string

    Returns a message based upon how much time has been worked
    and in how many days (work time per day).

    >>> work_per_day(8.00, 2)
    'You are under on time this week.'
    >>> work_per_day(24.59,3)
    'You are up on time this week.'
    >>> work_per_day(16.00,2)
    'You are on time for this week.'
    '''
    if work_time/days > 8: 
       return print('\nYou are up on time this week.\n')
    elif work_time/days < 8:
        return print('\nYou are under on time this week.\n')
    else:
       return print('\nYou are on time for this week.\n')

hours = get_hours(remaining_time(my_time))
minutes = get_minutes(remaining_time(my_time))

work_per_day(my_time,num_days_worked)
print('You have ' + str(hours) + ' hours and ' + str(minutes) + ' minutes left for the week.')
