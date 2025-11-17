def sum_of_repeat(number):

    s = str(number)
    max_digit = None
    max_count = 0

    # Szukamy cyfry z najwieksza liczba powtorzen

    for digit in set(s): # Tworzymy unikalną liste bez powtorzeń
        count = s.count(digit) # sprawdzamy ilosc powtorzen danej cyfry
        if count > max_count: # sprawdzamy czy te powtorzenia sa wieksze od poprzednich powtorzen, jezeli tak to przypisujemy jako obecny rekord powtorzen
            max_count = count
            max_digit = digit


    if max_count <= 1: # jezeli kazda cyfra wystepuje raz albo i mniej to zwraca 0 
        return 0
    
    return int(max_digit) * max_count # obliczamy  wynik mnożąc ilosc potworzen razy ta cyfra

user_number = input("Enter your number: ")
print(f"Sum of repeated numbers is: {sum_of_repeat(user_number)}")
