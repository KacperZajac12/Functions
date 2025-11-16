def binary_number(number):
    for char in number:
            if char not in "01":
                  return False
    return True 

number = input(f"Enter a number: ")

if binary_number(number):     
    print(f"{number} is binary number")
else:
      print("This is not a binary number")
    