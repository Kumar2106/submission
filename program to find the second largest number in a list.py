x = [1,2,3,4,8]
maxnumber = max(x)
index = x.index(maxnumber)
x.pop(index)
print(x)
print("The largest of the number in the given list is: ",max(x))