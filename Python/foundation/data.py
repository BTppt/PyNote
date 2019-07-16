# Built-in Data Type
## Integer
binval = 0b10101
oval = 0o3721
xval = 0xffffa
dval = 999
print(binval, oval, xval, dval)

## Floating Point
dfloat = 9.999
sfloat = 3.14e5
print(dfloat, sfloat)

## Complex number
cval0 = 3 + 2j
cval2 = complex(3, -2)
print(cval0, cval2)

## String
strval1 = 'It is Python 3.x'
strval2 = "It is Python 3.x"
strval3 = "It's Python 3.x"
strval4 = 'It\'s Python 3.x'
print(strval1, '\n', strval2, '\n', strval3, '\n', strval4, '\n')
### append
print('It is ' + 'Python ' + str(3) + '.x')
print(r'That\'s a escape character : \n')
### Bytes String and casting
bstr = b'abc'
print(type(bstr))
print('abc'.encode())
print(bytes('abd', 'UTF-8'))
print(type(bstr.decode("UTF-8")))
### Formatting
s = 'the sum of %f and %f is '
print(s % (1.6, 1.4), 3)
print("the sum of {0} and {1} is {2}".format("1.6", "1.4", "3"))
dict0 = {"language": "python", "id": 3.7}
print("the version of {language} is {id}".format(language="python", id=3.7))
### Use dict
print("the version of {language} is {id}".format(**dict0))
### number format
print("{:.2f}".format(3.1415926))
print("{:b}".format(11))
print("{:o}".format(11))
print("{:x}".format(11))
print("{:#x}".format(11))
### str method
dir(str)
### related functions
print(len("abc"))
print("an" in "acana")
print(max("abc"))
print(min("abc"))

## Operators
### Arithmetic operators
a = 5.0
b = 2.0
print(a / b, a // b, a % b, a * b, a + b, a - b, a ** b)
### Index operator
c = "01234567"
print(c[1:4])
print(c[1:2:4])
### Relational operators
print(a >= b, a <= b, a != b)
v1 = str(123)
v2 = '123'
print(v1 is v2)
print(v1 == v2)
### Logical operators
print(True and False)
print(True or False)
print(not True)
### Bitwise operators
print(1 & 0)
print(0b1010 | 0b1100)
print(0b1010 ^ 0b1100)
print(~0b1010)
print(0b1010 << 1)
print(~0b1010 >> 1)

## List
### construct
L = ["List ", "is ", "changeable", 1]
print(L)
print(L[-3:-1])
### Unpacking
a, b, c, d = L
print(a, b, c, d)
print(type(a))
first, *rest = L
print(first, rest)
first, *rest, last = L
print(first, rest, last)
### Packing
mypackage = a, b, c, d
print(mypackage)
print(type(mypackage))
num1, num2, char1 = 1, 2, 'c'
print(num1, num2, char1)
### Method
print(L.append('ex'))
print(L.extend(L))
print(L.insert(3, '3'))
del L[0:2]
print(L)
dir(list)

## Tuple
### construct
T = ('Tuple ', 'is ', 'not ', 'changeable')
print(T)
T = ('Single',)
print(type(T))
### casting
T = tuple(list(range(10)))
L = list(tuple(range(10)))
print(T, '\n', L)
### List & Tuple
L = ['1', '2', '3']
print((L + L) * 2)
print(type(L))
print(len(L))
dir(tuple)


## Dict
### construction > key-value >> unchangeable-changeable
my_dict = {'math': 140, 'english': 120, 'Chinese': 103}
my_dict = dict([('math', 140), ('english', 120), ('Chinese', 103)])
print(my_dict)
print(my_dict['math'])
### append
my_dict['physic'] = 100
print(my_dict)
### del
del my_dict['physic']
print(my_dict)
### judgement
print('math' in my_dict)
### method
my_dict.update([('math', 100), ('nature', 100)])
print(my_dict)
### traverse
for key in my_dict.keys():
     print(key)
for value in my_dict.values():
     print(value)
for item in my_dict.items():
     print(item)
for key, value in my_dict.items():
    print(key, value)
### other method
print(my_dict.popitem())
print(my_dict.setdefault('math'))
