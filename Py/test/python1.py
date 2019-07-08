print("""
Python 3.x                                              
1 Data type                                             
    1.1 Integer                                             
    1.2 Floating Point                                      
    1.3 Complex number                                      
    1.4 String                                              
    1.5 Operators                                           
    1.6 List                                                
    1.7 Tuple                                               
    1.8 Dict                                                
2 Control Structure                                     
    2.1 Selective Structure                                 
    2.2 Loop Structure                                      
3 Function                                              
    3.1 Definition                                          
    3.2 Lambda Function                                     
4 Class                                                 
    4.1 Definition                                          
    4.2 Inheritance and derive         
5 Exception
    5.1 Syntax
    5.2 Built-in Exception                     
""")
index = float(input())
print(index)

if index == 1.1:
    print('\n******************1.1 Integer\n')
    binval = 0b10101
    oval = 0o3721
    xval = 0xffffa
    dval = 999
    print(binval, oval, xval, dval)

if index == 1.2:
    print('\n******************1.2 Floating Point\n')
    dfloat = 9.999
    sfloat = 3.14e5
    print(dfloat, sfloat)

if index == 1.3:
    print('\n******************1.3 Complex number\n')    
    cval0 = 3+2j
    cval2 = complex(3, -2)
    print(cval0, cval2)

if index == 1.4:
    print('\n******************1.4 String\n')
    strval1 = 'It is Python 3.x'
    strval2 = "It is Python 3.x"
    strval3 = "It's Python 3.x"
    strval4 = 'It\'s Python 3.x'
    print(strval1, '\n', strval2, '\n', strval3, '\n', strval4, '\n')
    # append
    print('It is '+'Python '+str(3)+'.x')
    print(r'That\'s a escape character : \n')
    # Bytes String and casting
    bstr = b'abc'
    print(type(bstr))
    print('abc'.encode())
    print(bytes('abd', 'UTF-8'))
    print(type(bstr.decode("UTF-8")))
    # Formatting
    s = 'the sum of %f and %f is '
    print(s % (1.6, 1.4), 3)
    print("the sum of {0} and {1} is {2}".format("1.6", "1.4", "3"))
    dict0 = {"language": "python", "id": 3.7}
    print("the version of {language} is {id}".format(language="python", id=3.7))
    # Use dict
    print("the version of {language} is {id}".format(**dict0))
    # number format
    print("{:.2f}".format(3.1415926))
    print("{:b}".format(11))
    print("{:o}".format(11))
    print("{:x}".format(11))
    print("{:#x}".format(11))
    # str method
    dir(str)
    # related functions
    print(len("abc"))
    print("an" in "acana")
    print(max("abc"))
    print(min("abc"))

if index == 1.5:
    print('\n******************1.5 Operators\n')
    # Arithmetic operators
    a = 5.0
    b = 2.0
    print(a/b, a//b, a % b, a*b, a+b, a-b, a**b)
    # Index operator
    c = "01234567"
    print(c[1:4])
    print(c[1:2:4])
    # Relational operators
    print(a >= b, a <= b, a != b)
    v1 = str(123)
    v2 = '123'
    print(v1 is v2)
    print(v1 == v2)
    # Logical operators
    print(True and False)
    print(True or False)
    print(not True)
    # Bitwise operators
    print(1 & 0)
    print(0b1010 | 0b1100)
    print(0b1010 ^ 0b1100)
    print(~0b1010)
    print(0b1010 << 1)
    print(~0b1010 >> 1)

if index == 1.6:
    print('\n******************1.6 List\n')
    # construct
    L = ["List ", "is ", "changeable", 1]
    print(L)
    print(L[-3:-1])
    # Unpacking
    a, b, c, d = L
    print(a, b, c, d)
    print(type(a))
    first, *rest = L
    print(first, rest)
    first, *rest, last = L
    print(first, rest, last)
    # Packing
    mypackage = a, b, c, d
    print(mypackage)
    print(type(mypackage))
    num1, num2, char1 = 1, 2, 'c'
    print(num1, num2, char1)
    # Method
    print(L.append('ex'))
    print(L.extend(L))
    print(L.insert(3, '3'))
    del L[0:2]
    print(L)
    
    dir(list)

if index == 1.7:
    print('\n******************1.7 Tuple\n')
    # construct
    T = ('Tuple ', 'is ', 'not ', 'changeable')
    print(T)
    T = ('Single',)
    print(type(T))
    # casting
    T = tuple(list(range(10)))
    L = list(tuple(range(10)))
    print(T, '\n', L)
    # List & Tuple
    L = ['1', '2', '3']
    print((L+L)*2)
    print(type(L))
    print(len(L))
    dir(tuple)

if index == 1.8:
    print('\n******************1.8 Dict\n')
    # construction > key-value >> unchangeable-changeable
    my_dict = {'math': 140, 'english': 120, 'Chinese': 103}
    my_dict = dict([('math', 140), ('english', 120), ('Chinese', 103)])
    print(my_dict)
    print(my_dict['math'])
    # append
    my_dict['physic'] = 100
    print(my_dict)
    # del
    del my_dict['physic']
    print(my_dict)
    # judgement
    print('math' in my_dict)
    # method
    my_dict.update([('math', 100), ('nature', 100)])
    print(my_dict)
    # traverse
    for key in my_dict.keys():
        print(key)
    for value in my_dict.values():
        print(value)
    for item in my_dict.items():
        print(item)
    for key, value in my_dict.items():
        print(key, value)
    # other method
    print(my_dict.popitem())
    print(my_dict.setdefault('math'))

if index == 2.1:
    print('\n******************2.1 Selective Structure\n')
    c = -1
    # if statement
    if c > 0:
        print('c > 0')
    elif c == 0:
        print('c == 0')
    else:
        print('c < 0')

if index == 2.2:
    print('\n******************2.2 Loop Structure\n')
    # while statement
    c = -5
    while c < 0:
        print(c)
        c += 1
    else:
        print(c)
    # for statement
    for k in range(4):
        print(k)

if index == 3.1:
    print('\n******************3.1 Definition\n')
    # positional and keyword-only argument

    def myfun(p1, p2=0):
        """
        param p1: the added number 1
        param p2: the added number 2
        return: the sum
        """
        p1 = p1 ** p2
        return p1
    print(myfun(2, 3))
    print(myfun(p2=4, p1=2))
    print(myfun(2))
    print(myfun.__doc__)
    # support packing and unpacking >> using Tuple

    def unpacking(p1, p2, p3):
        return [p1, p2, p3]

    def packing(p1, p2, p3):
        return p1, p2, p3

    return_para_tuple = packing(1, 2, 3)
    print(return_para_tuple)
    return_p1, return_p2, return_p3 = unpacking('p1', 'p2', 'p3')
    print(return_p1, return_p2, return_p3)
    # arguments collection

    def tsum(p1, *rp, p2):
        thesum = p1 + p2
        for num in rp:
            thesum += num
        return thesum

    # print(tsum(1, 2, 3, 4)) >> TypeError: tsum() missing 1 required keyword-only argument: 'p2'
    print(tsum(1, 2, 3, p2=4))
    print(tsum(1, p2=4))          # *rp can be empty

    def dictshow(number, *subjects, **table):
        print('the number of subjects is ', number)
        print('containing: ', subjects)
        print('scores: ', table)

    dictshow(3, 'Math', 'Chines', 'Nature', Math=100, Chinese=100, Nature=100)
    # reverse argument collection

    def acmu(mp1, mp2):
        return mp1*mp2

    mp = (3, 4)
    print(acmu(*mp))
    mp = {'mp1': 3, 'mp2': 4}
    print(acmu(**mp))

if index == 3.2:
    print('\n******************3.2 Lambda Function and Function modifier\n')
    # Lambda
    func = lambda n: n**n
    print(func(2))
    # modifier

    def funa(fn):
        print('A')
        fn()
        return 'fkit'

    @funa
    def funb():
        print('B')
    print(funb)

if index == 4.1:
    print('\n******************4.1 Definition\n')
    # class variables and instance variables
    class Polygon:
        xpos = 0
        ypos = 0
        def __init__(self, vertex, angles):
            self.__vertex__ = vertex
            self.__angles__ = angles
        def vertexnum(self):
            return self.__vertex__
        # static method
        @staticmethod
        def count(self):
            self.xpos += 1

    polygon1 = Polygon(3,[60, 60, 60])
    polygon2 = Polygon(4, (90, 90, 90, 90))
    polygon1.xpos= 4
    print(polygon2.xpos)
    Polygon.xpos = 8
    print(polygon1.xpos)
    print(polygon2.xpos)
    # invoking instance method using class name
    print(Polygon.vertexnum(polygon1))
    # invoking static method
    Polygon.count(polygon1)
    print(polygon1.xpos)
    del Polygon.xpos
    #print(Polygon.xpos) >>AttributeError: type object 'Polygon' has no attribute 'xpos'

if index == 4.2:
    print('\n******************4.2 Inheritance and derive\n')
    class Polygon:
        xpos = 0
        ypos = 0
        def __init__(self, vertex, angles):
            self.__vertex__ = vertex
            self.__angles__ = angles
        def vertexnum(self):
            return self.__vertex__
    class  Rect(Polygon):
        def __init__(self, vertex, angles):
            super(Rect, self).__init__(vertex, angles)
            self.xpos = 1
            self.ypos = 2

    rect1 = Rect(4, [90, 90, 90, 90])
    print(rect1.xpos)
    print(rect1.ypos)

if index == 5.1:
    print('\n******************5.1 Syntax\n')

if index == 5.22:
    print('\n******************5.2 Built-in Exception\n')