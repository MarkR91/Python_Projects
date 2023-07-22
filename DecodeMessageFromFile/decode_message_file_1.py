#Functions:
def decode(message_file):

  list =[] #Declare list variable as Python technically dosen't use arrays.

  for x in message_file:
    ln = x.split(" ")
    list.append(ln)

  list.sort()
  output(list)


def output(list):
  
  n=0
  m=1
  i=2

  for x in list:
    print(list[n:m])
    print(list[m-1][1])
    n=m
    m=m+i
    i=i+1  
    if(list[n:m]==[]):
      break
   
#Beginning of program

message_file= open("file.txt","r") #Opens text file assuming its in the same folder as the Python program file.
decode(message_file)

message_file.close()



