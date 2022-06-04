def tester(someparameter):
    return items.append(someparameter)


items =['cake','napkins']
tester('ice')
print("Parameter input in main program "+str(items))



def items2(someparameter):
    return someparameter.append('ice')

items1 = ['cake','napkin']
items2(items1)

print("Parameter coded in function "+str(items1))


