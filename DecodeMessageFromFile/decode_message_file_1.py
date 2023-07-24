# Start of function
def decode(message_file):
  
  # Function for use in sort
  def sortfirst(ln):
    return int(ln[0]) #The numbers in text file are in a string type we need to convert to the integer type so that Python's sort function can properly sort the numbers.

  list =[] #Declare as list variable as Python technically dosen't use arrays

  for x in message_file:
    ln = x.split(" ")  #Call the Python split function for each line (x) in the text file by space character. ln is a list of a list containing numbers and text in string data type.
    list.append(ln)
  
  # Call Python sort function
  list.sort(key=sortfirst) #Need to create a sortfirst function as a control parameter to sort the list by numbers - accessed by ln[0]
  
  #print(list)
  '''Example: list= [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14]'''
  
  #The following indices prints out the numbers in list in the triangular pattern below.
  #print(list[0:1]) -> 1
  #print(list[1:3]) -> 2 3
  #print(list[3:6]) -> 4 5 6
  #print(list[6:10])-> 7 8 9 10
  
  #Initalize indices before entering for loop
  n=0 
  m=1
  i=2

  str="" #initialize string variable for code on line 36.

  for x in list:
    #print(list[n:m])
    #print(list[m-1][1])
    #print(type(list[m-1][1]))
    str = str +" "+list[m-1][1].rstrip('\n') #The strings/words associated with each of the ending numbers are concatenated by this line of code 
                                             #Applying the rstrip() method will ignore the newline character in building the list. 
                                             #This allows printing of strings on a single line.
    n=m
    m=m+i
    i=i+1  

    if(list[n:m]==[]): #break out of loop if no other elements while transversing then list
      break

  return str.lstrip() #Need to apply lstrip() Python string method to remove whitespace at the beginning of the concatenated string in str variable. 
# end of decode function

#Beginning of program

message_file= open("input.txt","r") #Opens text file assuming its in the same folder as the Python program file.

print(decode(message_file)) #Call decode function with file input parameter i.e message_file and print out the decoded string

message_file.close() #Closes our opened text file.


