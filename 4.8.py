def time_string(hour, minutes,time_format):
    if time_format == "12":
        time= f"{hour}:{minutes}am"
    else:
        time= f"{hour}:{minutes}"
    return time

h = input("Wpisz godzine: ")
m = input("Wpisz minuty: ")
t = input("Wybierz format daty, 24 albo 12: ")

print(f"Wynik: {time_string(h,m,t)}")

