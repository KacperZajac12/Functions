def counter(amount_to_pay):

    amount_to_pay = int(amount_to_pay)
    coins = 0

    # Sprawdzamy ile 5 zlotowek sie miesci w kwocie
    coins += amount_to_pay // 5
    amount_to_pay %= 5

    # Sprawdzamy ile 2 zlotowek sie miesci w kwocie
    coins += amount_to_pay // 2
    amount_to_pay %= 2

    # a reszta to złotówki
    coins += amount_to_pay

    return coins

user_amount = input("Enter your amount: ")
print(counter(user_amount))
    