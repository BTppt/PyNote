# Selection structure
# if...else
a, b = (4, 5)
if a > b:
    print('a > b')
elif a == b:
    print('a == b')
else:
    print('a < b')
# assert
assert a < b

# Iterative structure
# while
l0 = list(range(0, 10))
num = 0
while num < len(l0):
    print(l0[num])
    num += 1
else:                # else statement
    print('END')
# for
for ele in l0:
    print(ele)
# Jump statement
# break
for it0 in range(0, 10):
    if it0 > 5:
        break
    else:
        print(it0)
# continue
for it0 in range(0, 10):
    if it0 % 3 == 0:
        print(it0)
    else:
        continue

