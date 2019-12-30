# DATA TYPE
# integer
i0 = 1
i1 = 0b1
i2 = 0o1
i3 = 0x1
i4 = None
# float number
f0 = 1.1
f1 = 1.1e1
# complex number
c0 = 3 + 2j
# bytes
b0 = bytes(5)
b1 = bytes('abc', encoding='utf-8')
b2 = b'abc'
# string
s0 = 'abc'
s1 = "de'f"
s2 = 'ghi\n'
s3 = "abc""def"
s4 = s0 + s1
s5 = r'D:\n\r\t'
# msg = input("please input: ")
s00 = s0.title()
s01 = s0.upper()
s02 = s0.lower()
s6 = '  ab c '
s60 = s6.strip()
s61 = s6.lstrip()
s62 = s6.rstrip()
# list
l0 = [1, 2, 3, 'a', 'bc', 'cd']  # construction
l1 = list(range(0, 5))  # construction
print(l1)       # display
print(l0[0])    # index
for ele in l0:  # traverse
    print(ele)
del l0[0]   # delete ele
print(len(l0))  # length
print(l0 + l0)  # addition
print(l0 * 3)    # multiple
print(l0.count(1))  # counting occurrence number of specific element
print(l1.sort(reverse=True))  # sorting elements
# tuple
t0 = (1, 2, 3, 'a', 'bc', 'cd')
print(t0[0])
for ele in t0:
    print(ele)
print(len(t0))
print(t0 + t0)
print(t0 * 3)
# dictionary
d1 = {'a': 1, 'b': [{'b1': 21}], ('1', '2'): 3, (1, 2): 4}
print(d1['b'][0]['b1'])
for k, v in d1.items():
    print(k, ':', v)
d1.update({4: 5})
print(d1.pop((1, 2)))
print(d1)
d1.clear()
print(d1)

# OPERATION
# assignment and arithmetic operator
a0 = 1 + 1
a0 = 'ab' + 'c'
m0 = 4 - 3
mu0 = 4 * 3
mu1 = 4 ** 3
mu2 = 'ab' * 3
d0 = 4 / 3
d1 = 4 // 3
d2 = 7 % 3
# bitwise operation
print(5 & 9, 5 | 9, 5 ^ 9)
print(~9)
print(9 >> 2, 9 << 2)
# relationship operation
print(4 == 5, 4 >= 5, 4 <= 5)
print(4 > 3, 4 < 3, 4 != 3)
print(4 is 4)
# logical operation
print(4 == 5 and 4 == 4)
print(4 == 5 or 4 == 4)
print(not 4 == 5)
print(5 not in range(5, 8))
print(6 in range(6, 10))
# TYPE CASTING
