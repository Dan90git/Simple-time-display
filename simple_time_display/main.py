import pytz

from simple_time import display_current_time_and_date_information, day_number_from_date, time_zone_conversion, countdown, stopwatch, world_clock_display


def main():
    '''
    The program first starts creating from display_current_time() function a list with the current time and date informations, prints a string with the datas needed then asks to user if wants to convert current hour in another time zone. If so program performs conversion and display the result. Second, asks user if wants to start a countdown, if so asks format and amount of second then displays it. Third ask for stopwatch and if so displays it with stop and reset command. Last, asks to user if want to display multiple clocks in differents time zones and if so print a string with data requested.
    '''
    current_time_and_date_information= display_current_time_and_date_information()

    print(f'Time zone: {current_time_and_date_information[0]}\nCurrent time: {current_time_and_date_information[1]}\nCurrent date: {current_time_and_date_information[7]} {current_time_and_date_information[2]}\nWeek number: {current_time_and_date_information[6]}\nDay of the year: {day_number_from_date(current_time_and_date_information[3],current_time_and_date_information[4],current_time_and_date_information[5])}')

    start_conversion = input('Press enter to convert current hour in another time zone, or press another button then enter to skip ')

    if  start_conversion == '':
        tz_name = pytz.timezone(input('Enter a timezone: '))
        print(f'The current hour in {tz_name} time zone is {time_zone_conversion(tz_name)}')

    start_countdown = input('Press enter to start a countdown or another button then enter to skip: ')

    if start_countdown == '':
        hours, minutes, seconds = input('Enter hours, minutes, and seconds separated by whitespace to set the countdown: ').split()
        output_format = input('Choose the output (days, hours, minutes or seconds): ')
  
        time_user = int(hours) * 3600 + int(minutes) * 60 + int(seconds)

        countdown(time_user, output_format)

    start_stopwatch = input('Press enter to start a stopwatch or another button then enter to skip: ')

    if start_stopwatch == '':
        print(stopwatch())

    user_input = input('Press enter to display one or more clocks in different time zones, or another button then enter to skip: ')

    if user_input == '':
        number_of_clocks = int(input('how many clocks? '))
        print(world_clock_display(number_of_clocks))


if __name__ == '__main__':
    main()



