def space_saver(text):
    new_text = text.replace(" ","")
    return new_text
    
user_text = input("Enter a text: ")
print(f'This is your text without spaces: \n {space_saver(user_text)}')