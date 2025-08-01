def checker(a):
    for x in range(len(a)//2):
        if a[x] != a[-(x+1)]:
            print("no")
            break
    else:
        print("yes")

a = input("provide the word: ")
checker(a)







'''getting none'''

def checker(a):
   print(a)

a = input("provide the word: ")
print(checker(a))


'''enviroment global and local'''
def checker(a):
   h=1
   print(h)
   print(a)

h = input("provide the word: ")
print(checker(h))
'''accesing same code'''
hacker=checker
'''everything in python is a object'''