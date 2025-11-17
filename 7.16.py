def fibonacci(n):
    count = 1
    n = int(n)
    if n == 2 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    
value = input("Which value of the Fibonacci sequence you want to see?: ")
print(fibonacci(value))
