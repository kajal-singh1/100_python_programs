#python program to make a simple calculator

inp1 = float(input("Enter the number:"))
inp2 = float(input("Enter the number:"))

print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 division ")

choice = int(input("Enter your choice:"))

if choice == 1:
  print("addition of numbers = " , inp1+inpt2)
elif choice == 2:
  print("subtraction of numbers = " , inp1-inp2)
elif choice == 3:
  print("multiplication of numbers = ", inp1*inp2)
else:
  print("division of numbers = " , inp1/inp2)
