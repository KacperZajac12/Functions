from range_check import is_in_range

x = 2
y = 15
number = int(input("What number you want to check?: "))

print(f"Number {number} is in range <{x}, {y}>: {is_in_range(number,x,y)}")