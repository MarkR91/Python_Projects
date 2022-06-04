grid =[['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]


i=j=0
overpass= 0

while overpass < 6: #How to get internal list length?
    while i < len(grid):
           print(grid[i][j],end='')
           i+=1
           if(i == len(grid)):
               print('\n')
               i=0
               j+=1
    overpass+=1
