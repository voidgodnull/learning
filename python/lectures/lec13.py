def sum_digits(s):
    total = 0
    for char in s:
        if char in '0123456789':
            val = int(char)
            total += val
    return total

s = "12345adfg"
d = sum_digits(s)
print(d)

'''using tru and except'''


def sum_digits(s):
    total =0
    for char in s:
        try:
           val=int(char)
           total+=val
        except:
            print("cannot convert",char)
        finally:
            print("done")
    return total
    
s = "12345adfg"
d = sum_digits(s)
print(d)





'''assert and error printing'''
def sum_digits(s):
    assert len(s) !=0,"s is empty"
    total =0
    for char in s:
        try:
           val=int(char)
           total+=val
        except:
            raise ValueError("string have charcter")
    return total
    
s = "12345adfg"
d = sum_digits(s)
print(d)



'''except zerodivisionerror'''

