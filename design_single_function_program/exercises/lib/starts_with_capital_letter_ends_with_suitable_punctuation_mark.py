def starts_with_capital_letter_ends_with_suitable_punctuation(text):
    for i in text:
        if i[0].upper() and i[-1] == ".":
            return True
        elif i[0] and i[-1] in ":!?:.":
            return False

    
    
