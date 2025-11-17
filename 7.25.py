def sum_in_range(x,y):
    x = int(x)
    y = int(y)
    sum = 0
    for i in range(x,y+1):
        if i % 6 == 0 and not i % 4 == 0:
            sum +=i
    return sum

user_range= input("Enter a range(separated by space): ")
x,y = user_range.split()
print(sum_in_range(x,y))