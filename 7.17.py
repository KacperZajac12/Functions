def palindrome_checker(text):
    # Sprawdza czy oryginalny tekst jest taki sam jak jego odwrotnosc, w zapisie [::-1], pierwszy : oznacza start, drugi stop a trzeci krok, czyli idzie od końca do początku
    if text == text[::-1]:
        return True
    else:
        return False

user_text = input("What word you want to check?: ")
print(palindrome_checker(user_text))