#Finding the data types for the given values

li,di,s=[],{"sampath":"CSD"},{"E","R","A"}
a,b,c,d,e=1,True,19.32,"hello world",2-1j
print(type(li),type(a),type(b),type(c),type(d),type(e),type(di),type(s))

#identifying wheather the given value is either even or odd number

num=int(input("Enter the number :"))
if(num%2==0):
    print("%d is an Even number"%num)
elif(num==0):
    print("number is Zero")
else:
    print("%d is an odd number"%num)

#smallest number among three values

num1,num2,num3=int(input("num1 : ")),int(input("num2 : ")),int(input("num3 : "))
if num1<num2 and num1<num3:
    print("%d is the smallest number"%num1)
elif num2<num1 and num2<num3:
    print("%d is the smallest number"%num2)
else:
    print("%d is the smallest number"%num3)

num,result=int(input("Enter the number :")),0
i=0
while i<=num:
    result+=i
    i+=1
print("The sum of the numbers is %d"%result)

#Finding The odd numbers upto the n value'

num=int(input("Enter the number :"))
i=0
print("The odd numbers upto the given number are")
for x in range(i,num+1):
    if(x%2!=0):
        print(x,end="  ")

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

