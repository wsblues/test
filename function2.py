# function2

from re import X


x = 2

def func(a):
    return a+x
    


print(func(1))



def func2(a):
    x=5
    return a+x
    

print(func2(1))



def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))



def conU(ser, port):
    url = ser + port 
    return url


print(conU(port = '80', ser="www"))

