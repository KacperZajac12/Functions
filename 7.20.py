def prime_letters(number):
    primes = []
    num = 2 # zaczynamy od 2 bo 2 to liczba pierwsza
    is_prime = True
    number = int(number)
    while len(primes) < number:
            # sprawdzamy czy num nie dzieli sie przez żadną znalezioną juz liczbe pierwszą
            for p in primes:
                  if num % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
            num +=1
    return primes[-1] # zwracamy ostatni wynik czyli najwieksza liczbe pierwsza

user_input = input("Którą liczbę pierwszą z kolei chcesz sprawdzić?: ")
print(f"{user_input} liczba pierwsza z kolei to {prime_letters(user_input)}")
