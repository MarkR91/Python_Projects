#Functions

def triangle(arr):
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

f = open("input.txt","r")

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
