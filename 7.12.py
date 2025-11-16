def drawing():
    text = "*/*/*/*"
    length = len(text)
    new_text = ""
    # Przechodzi po kolei od 9 do 0 odejmując po 1 
    for i in range(length, 0, -1):
            # Dodaje po kolei znaki i dodaje znak nowej linii a [:i] oznacza  ilosc pierwszuch znakow
            new_text += text[:i] + "\n"
    return new_text

print(drawing())