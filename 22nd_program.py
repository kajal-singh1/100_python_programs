#Pyhton Program to find GCD Or HCF

#int(input("Enter the value:"))

def calcHCF ( x , y):
  if x > y:
    small = y
  else:
    small = x

  for i in range(1 , small+1):
    if ((x % i == 0) and (y %  i== 0)):
      hcf = i
  return hcf

x = 12
y = 30

print(calcHCF(12 , 30))