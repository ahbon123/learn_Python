#http://www.cnblogs.com/fengmk2/archive/2008/04/21/1163766.html

def foo(*args, **kwargs):
    print ('args = ', args)
    print ('kwargs = ', kwargs)
    print ('---------------------------------------')

if __name__ == '__main__':
    foo(1, 2, 3, 4)
    foo(a = 1, b = 2, c = 3)
    foo(1, 2, 3, 4, a = 1, b = 2, c = 3)
    foo('a', 1, None, a = 1, b = '2', c = 3)
