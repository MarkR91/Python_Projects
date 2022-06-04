#spam = ['apple','bananas','tofu','cat']

def commacode(list):

   length = len(list)

   print("Your list of "+str(length)+" items is")
   if length == 2:
      print(list[0]+" and "+list[1])
   else:
       list.insert(length - 1, 'and')
       for i in range(len(list)-2):
          print(list[i]+", ",end='')
       print("and "+list[length])

#Start of main
list = []

while True:
     word = input("Enter a word or nothing to finish your list: ")
     if word =='':
         break
     list = list+ [word] #Alternative method to populate list?

commacode(list)


