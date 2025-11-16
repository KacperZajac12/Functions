def numbers(number, even):
        count = 0
        sum = 0

        even = even.lower() == "true"
        for num in number:
            count +=1
            digit = int(num)
            if even and count % 2 == 0:
                sum += digit
            elif not even and count % 2 == 1:
                sum += digit
                
        return sum 

user_input = input("Enter an number: ")
user_even= input("Decide if your number is even (true or false): ")

print(f"Sum is: {numbers(user_input, user_even)}")