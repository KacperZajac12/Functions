number = input("Input credit card number: ")

def invisible_number(number):
    count = 0
    new_number = "  "
    for char in number:
        count +=1
        if count > 2 and count < len(number)-3:
            new_number += "*"
        else:
            new_number += char
    return new_number

print(invisible_number(number))
    