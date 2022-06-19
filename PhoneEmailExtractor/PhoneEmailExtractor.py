#Phonebook number and email address extractor

import pyperclip #The pyperclip module has the copy() and paste() functions that can send/receive text from clipboard.
import re

print("To Run: Open example webpage at http://www.nostarch.com/contactus press ctrl-A to select all the text and copy to the clipboard")
print ("Press Enter when done")

input()

phoneRegex = re.compile(r'''(
            (\d{3}|\(\d{3}\))?  # area code
            (\s | - |\.)?       # separator
            (\d{3})             # first 3 digits
            (\s| - |\.)         # separator
            (\d{4})             # last 4 digits
            (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
            )''', re.VERBOSE)


emailRegex = re.compile(r'''(
                [a-zA-Z0-9.-]+    # username
                @                 # @ symbol
                [a-zA-Z0-9.-]+    # domain name
                (\.[a-zA-Z]{2,4}) # dot
                )''', re.VERBOSE)

# Function that find matches in clipboard text
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
           phoneNum = '-'.join([groups[1], groups[3], groups[5]])
           if groups[8] != '':
              phoneNum += ' x' + groups[8]
           matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
for groups in emailRegex.findall(text):
     matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('The following phone numbers and emails were copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

