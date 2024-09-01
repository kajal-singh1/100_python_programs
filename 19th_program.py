#python program to find numbers divisible by another number

#1st sol
for i in range(1 , 100):
  if i % 13 == 0:
    print(i)

#2nd sol
l = [13 , 26 , 39 , 50 , 130]

result =list(filter (lambda x : x %13 == 0 , l))

print('the numbers divisible by 13 are' , result)
