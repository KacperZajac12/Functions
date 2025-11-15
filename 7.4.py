text = "You never get a second chance to make a first impression"

def finding_a_letter(letter):
    text = "You never get a second chance to make a first impression"
    count = 0
    for char in text:
        if char.lower() == letter.lower():
            count +=1
    return count


letter_to_find = input("What letter do you want to find?: ")
print(f"Letter {letter_to_find} appeared in \n '{text}' \n {finding_a_letter(letter_to_find)} times.")



