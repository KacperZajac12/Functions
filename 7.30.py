def sum_natural(n):
    n = int(n)
    if n == 1:
        return 1
    else:
        return n + sum_natural(n-1)


user_number = input("Enter a number: ")
print(sum_natural(user_number))

