s = "dhbfke,hedevd,bbbhdd"
for char in s:
    if char=="i":
        print("there is a i in ")
print("no i")
'''for is not limited to numbers'''


'''guess and check'''
t=0
for alice in range(11):
    for done in range(11):
        for dog in range(11):
            total=alice+done+dog
            if total == 11:
                print(f'({alice}  {done}  {dog})')
                t+=1
print(t)
                