def mathing(text):
    return eval(text)

user_text = input('Enter an expression with operators for adding and subtracting and single-digit numbers: ')

print(mathing(user_text))