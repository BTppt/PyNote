# function
def foo1(i0, i1=0):
    """
    :param i0: integral number
    :param i1: integral number
    :return: max value
    """
    if i0 > i1:
        return i0
    else:
        return i1


print(foo1(-4))
print(foo1(i1=3, i0=4))


# recursive function
def foo2(i):
    """
    :param i: positive integral number
    :return: accumulation
    """
    if i > 1:
        return i + foo2(i - 1)
    else:
        return 1


print(foo2(5))


# packing & unpacking
def foo3(i0, i1, i2):
    print("i0=%f, i1=%f, i2=%f" % (i0, i1, i2))


t0 = (1, 2, 3)
d0 = {'i0': 1, 'i2': 3, 'i1': 2}
foo3(*t0)
foo3(**d0)


def foo4(i0, *i1, i2):
    print('i0={}, i2={}'.format(i0, i2))
    for ele in i1:
        print(ele)


foo4(0, 1, 2, 3, i2=4)


def foo5(i0, i1):
    return i0 // i1, i0 % i1


v = foo5(6, 4)
print(v)

# global variables
gv = 6


def foo6():
    gv = 4
    globals()['gv'] = 7
    print(globals()['gv'])
    print(gv)


foo6()


def foo7():
    global gv
    gv = 9
    print(gv)


foo7()

# function variable
foo8 = foo1
print(foo8(1, 3))


def foo9(i0, i1, foo):
    return foo(i0, i1)


print(foo9(3, 4, foo1))


# lambda expression
def foo10(b):
    if b:
        return lambda n: n * n
    else:
        return lambda n, m: n ** m


foo = foo10(True)
print(foo(4))
foo = foo10(False)
print(foo(3, 2))


# function decorator
def foo11(foo):
    print('foo11')
    return foo


@foo11
def foo12(i0, i1):
    return i0 + i1


print(foo12(3, 4))


def decorator(foot):

    def fo(*k, **d):
        if type(k[0]) == str:
            foot()
        else:
            print('error type')

    return fo


@decorator
def foo(flag='train', vector='word2vector', graph=True):
    print(flag, vector, graph)
    return 1


# generator
def foo13(i0):
    cur = 0
    for num in range(0, i0):
        cur += num
        yield cur


ct = foo13(10)
print(next(ct))
print(next(ct))
