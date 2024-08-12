immutable_var = (1,2,3,4,5)
print(immutable_var)
mutable_list = [1,2,3,True,'list']
mutable_list[1]= 9
mutable_list[3]= False
mutable_list[4]= mutable_list[4][::-1]
print(mutable_list)