def solving(number1, number2, operator):
    number1 = int(number1)
    number2 = int(number2)
    if operator == "+":
        sum = number1 + number2
    elif operator == "%":
        sum = number1 % number2
    elif operator == "**":
        sum = number1 ** number2
    elif operator == "*":
        sum = number1 * number2
    elif operator == "-":
        sum = number1- number2
    return sum

user_input = input("Podaj dwie liczby i operator, wszystko oddzielone spacją: ")
user_number1, user_number2, user_operator = user_input.split()
print(solving(user_number1,user_number2,user_operator))
