#Create a list using different elements
li=[2,1.2,4+1j,"list",True]
print(li)

#find the length of the list
print("Length of the List is",len(li))

#perform slice operations & change some elements
MNC=["Apple","Microsoft","IBM","Amazon"]
print(MNC[1:3] ,MNC[:1],MNC[3],MNC[1:])
MNC.append("Facebook")
MNC.insert(2,"Google")
print(MNC)


#perform all other data structures

num1= [16,85,24,56]
num2= [12,54,32,15]
num1.extend(num2)
print('Numbers:', num1)
num1.reverse()
print(num1)
num1.pop(0)
print(num1)
num1.append(77)
print(num1)
num1.clear()
print(num1)
