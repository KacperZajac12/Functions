def acronymer(text):
    new_text = text.split()
    result = ""
    for n in new_text:
        result += n[0]

    return result

user_text = input("Enter your text: ")
print(f"Acronym from your text is: {acronymer(user_text)}")
