def time_string(hour, minutes,time_format):
    if time_format == "12":
        if hour > 10:
            hour = int(hour) - 12   
            time= f"{hour}:{minutes}am"
    else:
        if hour == "24":
            hour = "00"
        time= f"{hour}:{minutes}"
    return time

h = input("Wpisz godzine: ")
m = input("Wpisz minuty: ")
t = input("Wybierz format daty, 24 albo 12: ")

print(f"Wynik: {time_string(h,m,t)}")

