number = input("Input credit card number: ")

for char in number:
    count +=1
    if count > 2 and count < 12:
        char.replace(char,"*")
    