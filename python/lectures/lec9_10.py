(lambda x: x%2==0)(8)


'''tuples'''
'''indexable ordered sequence,obj can be of
any type ,cannot change obj value'''
ts=()
t=(2,"hello",3)
print(t[0])





seq =(2,"a",4,(1,2))
print(len(seq))
print(seq[3])
print(seq[3][0])


'''swaping with help of tupels'''
g=1
h=2
(g,h)=(2,1)


'''can be used to return more than one value from a function'''
'''return(sum,ans)'''

'''while making a function'''
'''deaf mean(*args       take parameter automatically as tuples)'''





'''LIST'''
'''[]'''
'''we can change values'''
'''can increase lenghth'''
l =[1,2,3]
l[0]=8
l.append(5)


'''string to list'''
y="hello cow"
k= list(y)
'''each charcter will be a element'''
k1=y.split('h')
k1.sort()
k1.reverse()
k1_new=sorted(k1)
'''remove h'''
'''list to string'''
c=''.join(k1)






'''decimal in binary'''

# Get the decimal number from the user
num = float(input("Enter a decimal number between 0 and 1 (e.g., 0.3, 0.5): "))

# Make sure it's between 0 and 1
if num >= 1 or num <= 0:
    print("Please enter a number between 0 and 1 (exclusive).")
else:
    binary = "0."
    count = 0  # to prevent infinite loop on non-terminating binary fractions

    while num > 0 and count < 30:  # limit digits to avoid infinite loop
        num = num * 2
        if num >= 1:
            binary += "1"
            num -= 1
        else:
            binary += "0"
        count += 1

    print("Binary representation is:", binary)





