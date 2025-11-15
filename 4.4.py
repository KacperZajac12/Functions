###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    s = 0
    for cyfra in str(number):
        s+= int(cyfra)
    return s

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')