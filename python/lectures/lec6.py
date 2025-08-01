

x=int(input("provide the number: "))
epslion = 0.01
num_guess=0
guess=0.0
increment=0.001

while abs(guess*guess-x)>=epslion:
    guess+=increment
    num_guess+=1

print(num_guess)
print(guess)









s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = int(input("Provide the number to find: "))
low = 0
high = len(s) - 1

while low <= high:
    mid = (low + high) // 2
    if s[mid] == f:
        print("Number is at index", mid)
        break
    elif s[mid] < f:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Number not found in the list.")
