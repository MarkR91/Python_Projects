"""
picnicItems = {'apples': 5, 'cups': 2}
item = str(input("Enter an item in picnic basket "))
print("There are "+str(picnicItems.get(item, 'no'))+" "+str(item)+" in the picnic basket")
"""
""
birthday_names = {'Frances': 'Apr 23rd 1991', 'Laura': 'Sep 17th 1990', 'Kim': 'July 20th 1997'}


while True:

    name = str(input("Enter a name to look for in birthday list or blank to finish: "))
    name = name.capitalize()
    if name == '':
        break

    if birthday_names.get(name, 0) == 0:
        print("There is no " + str(name) + " in the birthday list ")
        print("What is their birthday?")
        birth = str(input())
        birthday_names.setdefault(name, birth)
    else:
        print("There is a " + str(name) + " in the birthday list")


print(birthday_names.items())
""
"""
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
   print('Enter a name: (blank to quit)')
   name = input()
   if name == '':
     break
   if name in birthdays:
      print(birthdays[name] + ' is the birthday of ' + name)
   else:
      print('I do not have birthday information for ' + name)
      print('What is their birthday?')
      bday = input()
      birthdays[name] = bday
print('Birthday database updated.')
print(birthdays.items())
"""