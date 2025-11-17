def coder_checker(code):

    if len(code) != 4 or not code.isdigit():
        return False
    
    total = int(code[0]) + int(code[1]) + int(code[2])

    control_digit = total % 7

    return int(code[3]) == control_digit

user_input = input("Enter a product code: ")
print(coder_checker(user_input))