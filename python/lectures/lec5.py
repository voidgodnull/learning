'''to get binary of a number'''
number=int(input("provide the number: "))
binary=''
while number>=1:
    if number%2==0:
        binary=binary+"0"
        number=number/2
    else:
        binary=binary+"1"
        number=int(number/2)
print(binary)



''''a decimal number into binary'''
num=float(input("with all due respect please provide the number: "))
decimal_places=0
while  num!=int:
    num=num*2
    decimal_places+=1
bry=''
while num>=1:
    if num%2==0:
        bry=bry+"0"
        num=number/2
    else:
        bry=bry+"1"
        num=int(num/2)
brny=int(bry)
i=0
for g in decimal_places:
    brny[-decimal_places]=brny[-decimal_places + 1]
brny[decimal_places]="."
print(brny)



