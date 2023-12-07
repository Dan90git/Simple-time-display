import time

from datetime import datetime

import pytz

from tzlocal import get_localzone


def display_current_time_and_date_information():
    '''
    Returns time zone, current hour, date, day number,month number, year, week number and day name.

            Parameters: 
                    no arguments needed

            Returns:
                time_zone(str): the name of time zone
                current_time(str): the current time (H/M/S), 24 hours format
                current_date(str): the current date (day name, D/M/Y)
                current_day_num(int): day number as integer
                current_month_num(int): current month number as integer
                current_year(int): current year as integer
                current_week_num(int): current week number as integer
                day_name(str):  the current day's name 
    '''
    time_zone = get_localzone()
    current_time =time.strftime('%X')
    current_date = time.strftime('%d/%m/%Y')
    current_day_num = int(time.strftime('%u'))
    current_month_num = int(time.strftime('%m'))
    current_year = int(time.strftime('%V'))
    current_week_num = int(time.strftime('%V'))
    day_name = time.strftime('%A')
    return time_zone,current_time,current_date,current_day_num,current_month_num,current_year,current_week_num,day_name


def day_number_from_date(day,month,year):
    '''
    Returns day number of the year from date D/M/Y.

        Parameters:
                day(int): decimal integer.
                month(int): decimal integer.
                year(int): decimal integer.

        Returns: 
                ordinal_date(int): day number as integer.
    '''
    if year % 400 == 0:
        leap_year = True
    elif year % 400 != 0 and year % 100 != 0 and year % 4 == 0:
        leap_year = True
    else:
        leap_year = False

    if (day > 28 and month == 2 and leap_year == False) or (day > 29 and month == 2 and leap_year == True) or (day > 31 and (1 <= month <= 7 and month % 2 != 0)) or (day > 31 and (7 < month <= 12 and month % 2 == 0)) or (day > 30 and (1 <= month <= 7 and month % 2 == 0)) or  (day > 30 and (7 < month <= 12 and month % 2 != 0)) or  month > 12 or month < 1 :
        return 'invalid date'
    else:    
        ordinal_day = 0
    
        if month == 1:
            ordinal_day = day
        else:
            for i in range(1, month):
                if i == 2 and leap_year == True: 
                    ordinal_day += 29
                elif i == 2 and leap_year == False:
                    ordinal_day += 28 
                elif 1 <= i <= 7 and i % 2 != 0:
                    ordinal_day += 31
                elif 7 < i <= 12 and i % 2 == 0:
                    ordinal_day += 31
                elif 1 <= i <= 7 and i % 2 == 0:
                    ordinal_day += 30
                elif 7 < i <= 12 and i % 2 != 0:
                    ordinal_day += 30
            ordinal_day += day

        return ordinal_day


def time_zone_conversion(time_zone_name):
    '''
    Returns the current hour from a given time zone.

            Parameters:
                    time_zone_name(str): A string with time zone's name.

            Returns: 
                    converted_time(str): A string with current hour(H:M:S) of the gived time zone
    '''
    converted_time = datetime.now(time_zone_name).strftime('%H:%M:%S')
    return converted_time

def countdown(t, output):
    '''
    Print a countdown with a string and carriage return.

            Parameters:
                    t(int): an amount of seconds
                    output(string): could be "days" to print countdown in the format DD:HH:MM:SS, "hours" to print countdown in the format HH:MM:SS, "minutes" to print countdown in the format MM:SS or "seconds" to print only seconds
      
            print a string with carriage return in the specific format choosed: DD:HH:MM:SS or HH:MM:SS or MM:SS or only seconds
    '''
    while t:
        
        days, remainder_days = divmod(t, 86400)
        hours, remainder_hours = divmod(remainder_days, 3600)
        mins, secs = divmod(remainder_hours,60)
        if output == 'days':
            timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days,hours,mins,secs)
            print(timer, end='\r')
            time.sleep(1)
            t -= 1
        elif output == 'hours':
            hours += days * 24
            timer = '{:02d}:{:02d}:{:02d}'.format(hours,mins,secs)
            print(timer, end='\r')
            time.sleep(1)
            t -= 1
        elif output == 'minutes':
            hours += days * 24
            mins += hours * 60
            timer = '{:02d}:{:02d}'.format(mins,secs)
            print(timer, end='\r')
            time.sleep(1)
            t -= 1
        elif output == 'seconds':
            hours += days * 24
            mins += hours * 60
            secs += mins * 60
            timer = '{:02d}'.format(secs)
            print(timer, end='\r')
            time.sleep(1)
            t -= 1
    print('Time\'s up! ')

def stopwatch():
    '''
    Simulates a stopwatch traking the time from the function's call, until user stops it, then return time elapsed (could be reset).

            Parameters:
                    no arguments
            
            Returns:
                    time_elapsed(str): string with the amounts of seconds elapsed from stopwatch starts.
            
    '''
    input_stopwatch = ''
    start_time = time.time()
    while input_stopwatch != 'q':
        if input_stopwatch == '':
            print('Started stopwatch')
            start_time = time.time()
            input_stopwatch = input('Press q and enter to stop, or r and enter to reset stopwatch: ')
        elif input_stopwatch == 'r':
            print('Stopwatch has been reset')
            start_time = time.time()
            input_stopwatch = ''
            input_stopwatch = input('Press q and enter to stop, or r and enter to reset stopwatch: ')
    stop_time = time.time()
    time_elapsed = f'{round(stop_time - start_time, 2)} secs'
    return time_elapsed

def world_clock_display(number_of_clocks_to_display):
    '''
    Returns a string with one or more clocks of differents time zone.

            Parameters: 
                    number_of_clock_to_display(int): number of "clocks" composing the return string

            Returns:
                clocks_string(str): a string         
    '''
    clocks_string = ''
    for clocks in range(1,number_of_clocks_to_display + 1):
        time_zone_clocks = pytz.timezone(input(f'Wich timezone for clock {clocks} ? '))
        clocks_string += f"{time_zone_clocks} - {datetime.now(time_zone_clocks).strftime('%H:%M:%S')} "
    return clocks_string