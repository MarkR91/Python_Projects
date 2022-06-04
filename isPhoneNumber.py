def isPhoneNumber(text):  # 1-800-553-4589
    x = len(text)
    if x != 14 and x != 12:  # Study this Interesting logic
        return False
    for i in range(0, 12):
        if not text[i].isdigit() and text[i] != '-':
            return False
    return True  # If the program execution manages to get past all the checks, it returns True


# text = "800-553-4589"
text = 'Call me at 800-553-4589 today. 415-555-9999 is my office.'

for i in range(len(text)):
    chunk = text[i:i + 12]  # loop slices text every 12 characters to the right
    if isPhoneNumber(chunk):
        print('Phone numbers found: ' + chunk)
print('Done')
