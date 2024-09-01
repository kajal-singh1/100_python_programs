#12 python program for printing the multiplication of a table
#using for loop
num = int(input("Enter the number:"))
for i in range(1 , 11):
    table = num * 1
    print(num , "X" , i , "=" , table)


#using while loop
num = int(input("Enter the number:"))
i = 1
while i <= 10:
    table = num * 1
    print(num , "X" , i , "=" , table)
    i = i+1