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
