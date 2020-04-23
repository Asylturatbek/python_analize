my_list = ['some', 'another', 'mine', 'okay']
print(my_list)
print(enumerate(my_list))
enumerateList = enumerate(my_list)


# very interesting here, ... 
# if I uncomment the code below the next blocl doesn't get executed
# I think that is because enumerate object disappers immediately after first call


# print(list(enumerateList))
print('enumerate in for loop ======')

for index, element in enumerateList:
	print('index is '+str(index))
	print('element is '+ element)