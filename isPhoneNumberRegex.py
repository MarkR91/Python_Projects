import re #regex module

def isPhoneNumberRegex(chunk):
   phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
   match_object = phoneNumRegex.search(chunk)
   print("The phone number is ",match_object.group())

chunk = "...reach me at 456-331-4567"
isPhoneNumberRegex(chunk)