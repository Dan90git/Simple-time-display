
import time

from datetime import datetime

import pytz

from tzlocal import get_localzone


def display_current_time_and_date_information():
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
    converted_time = datetime.now(time_zone_name).strftime('%H:%M:%S')
    return converted_time

def countdown(t, output):
    # while loop that iterates till "t"(amount of seconds) is true
    while t:
        # gets from t variables days, hours and minutes to print
        days, remainder_days = divmod(t, 86400)
        hours, remainder_hours = divmod(remainder_days, 3600)
        mins, secs = divmod(remainder_hours,60)
        # if-elif statement that displays the countdown in the requested format
        if output == 'days':
            timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days,hours,mins,secs)
            # prints the variable with the output with a carriage return to simulate a clock
            print(timer, end='\r')
            # time.spleep(1) stops cycle for a second than 1 went substract to "t"
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
    # ending message
    print('Time\'s up! ')

def stopwatch():
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
    return f'{round(stop_time - start_time, 2)} secs'

def world_clock_display(number_of_clocks_to_display):
    clocks_string = ''
    for clocks in range(1,number_of_clocks_to_display + 1):
        time_zone_clocks = pytz.timezone(input(f'Wich timezone for clock {clocks} ? '))
        clocks_string += f"{time_zone_clocks} - {datetime.now(time_zone_clocks).strftime('%H:%M:%S')} "
    return clocks_string

   

def main():
    # creates a list to store results from display_current_time()
    current_time_and_date_information= display_current_time_and_date_information()

    # prints a string with result from display_current_time()
    print(f'Time zone: {current_time_and_date_information[0]}\nCurrent time: {current_time_and_date_information[1]}\nCurrent date: {current_time_and_date_information[7]} {current_time_and_date_information[2]}\nWeek number: {current_time_and_date_information[6]}\nDay of the year: {day_number_from_date(current_time_and_date_information[3],current_time_and_date_information[4],current_time_and_date_information[5])}')

    # asks to user if wants the current hour in another time zone
    start_conversion = input('Press enter to convert current hour in another time zone, or press another button then enter to skip ')

    # performs the conversion
    if  start_conversion == '':
        tz_name = pytz.timezone(input('Enter a timezone: '))
        print(f'The current hour in {tz_name} time zone is {time_zone_conversion(tz_name)}')

    # asks to user if wants to start a countdown
    start_countdown = input('Press enter to start a countdown or another button then enter to skip: ')

    # asks to user the amount of time in hours, minutes and seconds for the countdown
    if start_countdown == '':
        hours, minutes, seconds = input('Enter hours, minutes, and seconds separated by whitespace to set the countdown: ').split()
        output_format = input('Choose the output (days, hours, minutes or seconds): ')

    # converts amount of time in seconds    
        time_user = int(hours) * 3600 + int(minutes) * 60 + int(seconds)

        countdown(time_user, output_format)

    # asks to user if start a stopwatch
    start_stopwatch = input('Press enter to start a stopwatch or another button then enter to skip: ')

    if start_stopwatch == '':
        print(stopwatch())

    # asks to user if wants to displays some clocks with the current hour in different time zone
    user_input = input('Press enter to display one or more clocks in different time zones, or another button then enter to skip: ')

    if user_input == '':
        number_of_clocks = int(input('how many clocks? '))
        print(world_clock_display(number_of_clocks))


if __name__ == '__main__':
    main()



