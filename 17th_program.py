#16 Python Program to find the sum of natural numbers
num = int(input("Enter the Number"))

if num < 0:
  print("please enter positive number")

else:
  sum = 0
  while num>0:
    sum += num
    num -= 1
print(sum)
