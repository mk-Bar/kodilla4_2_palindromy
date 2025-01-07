def check_if_palindrom(word):
    letter_check=True
    for i in range(len(word)//2):
        following_end_letter=word[-(i+1)]
        following_front_letter=word[i]

        if following_front_letter!= following_end_letter:
            letter_check=False
            break
    return letter_check
        
print(check_if_palindrom("kajak"))