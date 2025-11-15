def name_day(day_number):
    day = ''
    if day_number == 1:
        day = "Monday"
    elif day_number == 2:
        day = "Tuesday"
    elif day_number == 3:
        day = "Wednesday"
    elif day_number == 4:
        day = "Thursday"
    elif day_number == 5:
        day = "Friday"
    elif day_number == 6:
        day = "Saturday"
    elif day_number == 7:
        day = "Sunday"
    return day
    
# dzien_tygodnia = input("Wprowadz jakąś cyfre: ")
print('The name of day 7 in the week is', name_day(7))
print('The name of day 3 in the week is', name_day(3))
print('The name of day 5 in the week is', name_day(5))

