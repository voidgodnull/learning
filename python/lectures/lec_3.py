number =4
if number < 6:
    print("good to go")
elif number>9:
    print("hello")
else:
    print("bye")


'''iteration'''
x =int(input("guess a number: "))
while x<100:
    if x==3: 
        '''3 to get out of this code'''
        break
    print("keep guessing")
    x=int(input("guess again: "))
    if x==49:
        print("welcome to the void")
        x=int(input("guess again: "))
print("finally u started thinking big")


"""to find factors"""
y=int(input("please provide the number: "))
i=1
while i<= y:
    if y==3:
        break
    if y%i ==0:
        print(i)
    i += 1


h=[1,2,3,8,9]
for n in range(1):
    for z_count in h:
     print(n)

max=h[0]
for number in h:
    if max<number:
        max=number
print(max)

for o in range(1,6,2):
    print(o)