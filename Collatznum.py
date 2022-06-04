def collatznum(number):

    if number % 2 == 0:
        return number//2
    else:
        return 3*number+1


number =int(input("Enter a number: "))
ans = number
while ans != 1:
     ans= collatznum(ans)
     print(ans)
