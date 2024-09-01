#python program to find armstrong number in an interval
a = int(input("enter the number:"))
b = int(input("enter the number:"))


for i in range(a , b+1):
  order = len(str(i))
  sum = 0
  svd = i
  while svd > 0:
    digit = svd % 10
    sum  += digit ** order
    svd //= 10

if i == sum:
  print(i)