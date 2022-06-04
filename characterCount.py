wordlist1 = "Enter a name to look for in birthday list"

# wordlist2 =["Enter a name to look for in birthday list"]
# print(list(wordlist1))
# print(wordlist2)
"""
count=0
for char in wordlist1:
    if char != ' ':
      count+=1
print(count)
"""
count = {}
x = '/'
count.setdefault(x, 0)
print(count.items())
for char in wordlist1:
    count.setdefault(char, 0)
    count[char] = count[char]+1
print(count.values())
print(count)
