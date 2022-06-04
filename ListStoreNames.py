people = []

while True:
     name = input("Enter a name or nothing to finish your list: ")
     if name =='':
         break
     people = people+ [name]

print("Entered names using both simple print and a for loop: ")
print(people,len(people))
for i in range(len(people)-1):
    print(i,people[i])