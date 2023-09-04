#Finding The odd numbers upto the n value'

num=int(input("Enter the number :"))
i=0
print("The odd numbers upto the given number are")
for x in range(i,num+1):
    if(x%2!=0):
        print(x,end="  ")