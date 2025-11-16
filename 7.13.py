def funny_numbers(number):
    integer = int(number)
    text = ""
    for i in range(1, integer +1, +1):
        text += str(i)
    return text

start_point = input("Enter an ending point:  ")

print(funny_numbers(start_point))