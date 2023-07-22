#Functions:

def triangle(list):

  n=0
  m=1
  i=2

  for x in list:
    print(list[n:m])
    n=m
    m=m+i
    i=i+1
    if(list[n:m]==[]):
      break

# Beginning of program
f = open("input.txt","r") #Open text file

list =[] #Declare list variable as Python technically dosen't use arrays

for x in f:
   ln = x.split(" ")
   list.append(ln)

list.sort()
triangle(list)

f.close()
