def negative_in_range(x,y):
    sum = 0
    first_number = int(x)
    second_number = int(y)
    second_number +=1
    for i in range(first_number, second_number):
        if i % 2 == 0 and i < 0:
            sum +=1
    return sum

print("======ENTERING A RANGE======")
user_input = input("Enter a first number: ")
user_input2 = input("Enter a second number: ")

print(f"Sum is: {negative_in_range(user_input,user_input2)}")