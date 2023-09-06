"""*****************************************************Exception Handling and User defined exception**********************************************************"""

#Write a python program to catch following exception Value Error,Index Error,Name Error,Type Error,DivideZero Error""" 

try:
   Name=input("Enter your name :")
   age=int(input("Enter your age :"))
   num1,num2=int(input("Enter num1 :")),int(input("Enter num2 :"))
   result=num1/num2
   print(result)
   li=["BMW","Audi","Ferrari","Ford"]
   S=int(input("Enter index of the element from the list :"))
   print(li[S])
   option=input("Enter y to create a variable")
   if option=="Y":
      value=20
      print(value)
   else:
      print(value) 
except ValueError:
   print(" Value error has occured,please try again..!")
except IndexError:
   print(" IndexError has occured,please try again..!")
except NameError:
   print(" NameError has occured,please try again..!")
except TypeError:
   print(" TypeError has occured,please try again..!")
except ZeroDivisionError:
   print(" ZeroDivisionError has occured,please try again..!")

#Write a python program to create user defined exception.

li=["CSE","CSM","CSD"]
branch=input("Enter your branch name :")
assert branch in li,"You don't belong to cse department"
print("you belong to CSE department")

#Write a python program to understand the use of else and finally block with try block."""

try:
  num1,num2=int(input("Enter num1 :")),int(input("Enter num2 :"))
  result=num1/num2
except ZeroDivisionError:
   print("Zero division Error please try again..!")
else:
   print("The division of given two numbers are : %d"%result)
finally:
   print("End of the code..!")
  
     

#Write a python program that uses raise and exception class to throw an exception"""


class error(Exception):
   pass
try:
   li=["BMW","Audi","Ferrari","Ford","Vovlo"]
   Re=input("Enter the Required company to buy:")
   if Re not in li:
      raise error 
   else:
      print("you can buy the car in your region")
except error:
    print("Error The company car is not avaliable for right now..!")