def day_name(day_number):
    if day_number == 1:
        return 'Monday'
    if day_number == 2:
        return 'Tuesday'
    if day_number == 3:
        return 'Wednesday'
    if day_number == 4:
        return 'Thursday'
    if day_number == 5:
        return 'Friday'
    if day_number == 6:
        return 'Saturday'
    if day_number == 7:
        return 'Sunday'
    
number = 3
day = day_name(number)
print(f'The name of day {number} in the week is {day}')