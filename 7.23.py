def checker(text):
    if len(text) == len(set(text)) and len(text) >= 6:
        return True
    else:
        return False

user_text = input("Enter your password to check: ")
print(checker(user_text))