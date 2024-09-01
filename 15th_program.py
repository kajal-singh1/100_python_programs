#Python Program to check Armstrong Number
num = int(input("Enter the number:"))
order = len(str(num))

sum = 0
svd = num

while svd > 0:
  digit = svd % 10
  sum  += digit ** order
  svd //= 10

if sum == num:
  print("it is a armstrong number")
else:
  print("it is not an armstrong number")