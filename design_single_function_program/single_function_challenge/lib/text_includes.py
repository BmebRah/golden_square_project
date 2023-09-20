
def text_includes(text):
    for i in text:
        return i in text.upper()
    if text == "":
        raise Exception('No Text Passed')
    elif text == None:
        raise Exception("'NoneType' object is not iterable")
    
