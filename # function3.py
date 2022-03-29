# function3

from tkinter import Y
from unittest import result


def union(*arg):
    result=[]
    for item in arg:
        for x in item:
            if x not in result:
                result.append(x)
    return result


print(union('han', 'egg'))
print(union('ham', 'egg', 'spam'))



def usrURIBuilder(server, port, **user):
    strURL = "https://" + server + ":" + port +  "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
        return strURL

print(usrURIBuilder('credu.com', '80', id='kim', age='30'))


g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))

print((lambda x:x*x)(3))

