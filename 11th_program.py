#program to print all the prime numbers in an interval
lower  = int(input("Enter the values :"))
upper  = int(input("Enter the values :"))
for num in range(lower , upper+1):
  if num > 1:
    for i in range(2 , num):
      if num%i == 0 :
        break
    else:
      print(num)