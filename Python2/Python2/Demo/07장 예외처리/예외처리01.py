# def divide(a, b):
#     return a / b

# try:
#     c = divide(5, 'string')
# except ZeroDivisionError:
#     print('두 번째 인자는 0이여서는 안됩니다.')
# except TypeError:
#     print('모든 인자는 숫자여야 합니다.')
# except:
#     print('음 무슨 에러인지 모르겠음')

    


def divide(a,b):
    return a/b

try:
    result = divide(5,3)
    print('result : {}'.format(result))
except ZeroDivisionError:
    print('no 0')
except TypeError:
    print('all number')
else:
    print('wtf')
finally:
    print('ok')


# try:
#     c = divide(5, 'string')
# except ZeroDivisionError:
#     print('no 0')
# except TypeError:
#     print('all number')
# except:
#     print('wtf')
