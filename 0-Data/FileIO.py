from pathlib import *
import os
import locale
import json
import pickle
import scipy.io


# INPUT and OUTPUT
msg = input('Please input: ')
print(msg)
# formatted string literals
year = 2019
event = 'Referendum'
print(f'Results of {year} {event}')
# format method
print('{} data event {} '.format(year, event))

# FILE PATH
file_dir = Path('E:\\myRepos\\PyNote\\0-Data\\resource')
print(file_dir)
locale.getpreferredencoding(False)
with open(file_dir / 'test.txt', 'w', encoding='utf-8') as fp:
    print(fp.mode)
    print(fp.encoding)
    print(fp.closed)
    fp.write('{year": 2018, "math": 90, "Chinese": 80, "is": {"physics": 100, "chem": 101}, 29: 57}')
    fp.writelines(('123' + os.linesep, '456'))
with open(file_dir / 'test.txt', 'r', encoding='gbk') as fp:
    while True:
        ch = fp.read(1)
        if not ch:
            break
        else:
            print(ch, end='')
with open(file_dir / 'test1.txt', 'wb') as fp:
        fp.write('.')
with open(file_dir / 'test1.txt', 'rb') as fp:
    while True:
        ch = fp.read()
        if not ch:
            break
        else:
            print(ch, end='')

# specific format
data1 = {"year": 2018, "math": 90, "Chinese": 80, 'is': {"physics": 100, "chem": 101}, 29: 57}
data2 = ['key', 1, 3, 4]
data3 = (3, 4, 5, 6)
# json