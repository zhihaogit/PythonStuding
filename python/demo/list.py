classmates = ['1', '2', '3']

length = len(classmates)

item0 = classmates[0]

classmates.append('4')

classmates.insert(length - 2, '12')

classmates.pop(3)

classmates[1] = '121'

itemLast = classmates[-1]

print (length, item0, itemLast, classmates)
