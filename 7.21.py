def differencer(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a > b and a > c and b > c:
        result = a - c

    elif a > b and a > a and c > b:
        result = a - b

    elif b > a and b > c and a > c:
        result = b - c

    elif b > a and b > c and c > a:
        result = b - a

    elif c > b and c > a and b > a:
        result = c - a

    elif c > b and c > a and a > b:
        result = c - b

    return result
user_numbers = []

user_numbers = input("Enter 3 numbers (separated by space): ")
x,y,z = user_numbers.split()
print(f"Difference between the largest and the smallest is: {differencer(x,y,z)}")
    