def power(x,n):
    x = int(x)
    n = int(n)
    if n == 1:
        return x
    elif n == 0:
        return 1
    else:
        new_x = x * power(x, n-1)
    return new_x
    
user_input = input("Enter a base and power (separated by a space): ")
x,n = user_input.split()
print(power(x,n))