#f = open("demofile.txt", "r")

def triangle(arr):

  '''arr= [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14]'''

  #print(arr[0:1])
  #print(arr[1:3])
  #print(arr[3:6])
  #print(arr[6:10])...
  n=0
  m=1
  i=2

  for x in arr:
    print(arr[n:m])
    n=m
    m=m+i
    i=i+1
    if(arr[n:m]==[]):
      break

f = open("D:\Downloads\cq_input.txt","r")

arr =[]
for x in f:
   #print(x)
   ln = x.split(" ")
   arr.append(ln[0])
   #print(ln[0])

arr.sort()
triangle(arr)
#print("arr=",arr[0:len(arr)])
#print(f.read(5))
f.close()
