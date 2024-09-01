#python program to find the factorial of a number
num = int(input("Enter the number:"))
fact = 1
if num < 0:
  print("factorial doesnot exist")
if num == 0:
  print("factorial of number is :" , 1)
if num > 0:
  for i in range(1 , num+1):
    fact = fact * i

    print("the factorial of the given number" , fact)


#using recursion(calling the own function)
def fact(a):
  if a == 0:
    return 1
  else:
    return((a) * fact(a-1))

num = int(input("enter the number:"))
result = fact(num)
print(result)