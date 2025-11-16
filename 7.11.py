def checking_numbers(x,y,z):
    result = ""
    new_x = int(x)
    new_y = int(y)
    new_z = int(z)
    lista = [new_x, new_y, new_z]
    for char in lista:
        if char < 0:
            result = True
        else:
            result = False
    return result 

first = input("Enter first number: ")
second = input("Enter second number: ")
third = input("Enter third number: ")

print(checking_numbers(first, second, third))
    
