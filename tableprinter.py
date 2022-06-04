"""
 -How to print a list with inner lists into a table with the first column representing the first items in the inner list
 -How to print a two by two matrix

"""


tableData = [['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]


def printTable(tableData):

       #colwidth= [0]*len(tableData)
       #rowitems= [0]*len(tableData[0])

       i = j = 0
       overpass = 0

       while overpass < 4:  # How to get internal list length?
           while i < len(tableData):
               print(tableData[i][j], end=' ') #Used end=''in the original code
               i += 1
               if (i == len(tableData)):
                   print('\n')
                   i = 0
                   j += 1
           overpass += 1


printTable(tableData)