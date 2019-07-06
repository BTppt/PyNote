print('''
Python 3.x                                              \n
1 Data type                                             \n
1.1 Integer                                             \n
1.2 Floating Point                                      \n
1.3 Complex number                                      \n
1.4 String                                              \n
1.5 Operators                                           \n
1.6 List                                                \n
1.7 Tuple                                               \n
1.8 Dict                                                \n
2 Control Structure                                     \n
2.1 Selective Structure                                 \n
2.2 Loop Structure                                      \n
3 Function                                              \n
3.1 Definition                                          \n
3.2 Lambda Function                                     \n
4 Class                                                 \n
4.1 Definition                                          \n
4.2 Inheritance and derive                              \n
''')
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

if index == 1.7:
    print('\n******************1.7 Tuple\n')

if index == 1.8:
    print('\n******************1.8 Dict\n')
