def factorial(n):

    n = int(n)
# 0! = 1, 1! = 1
    if n==0 or n==1:
        return 1

    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n-1)

user_choice = input("Enter a number: ")
print(factorial(user_choice))