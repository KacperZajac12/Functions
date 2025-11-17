def separater(text):
    text = text.replace(" ", "")
    new_list = list(text)
    separator = "-"
    result = separator.join(new_list)

    return result

user_text = input("Enter your text: ")
print(separater(user_text))