name = input('name:->')
nameArr = []

nameArr.append(name)

if nameArr:
	print (name)
elif len(nameArr) == 2:
	print ('{}hahaha'.format(name))
else:
	print ('end')
