from pathlib import *
import os

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
file_path_s = PureWindowsPath('E:\\myRepos\\PyNote\\0-Data\\resource\\test.txt')
print(file_path_s)
file_path = Path('E:\\myRepos\\PyNote\\0-Data\\resource\\test.txt')
print(file_path)
with open(file_path, 'w') as fp:
    print(fp.mode)
    print(fp.encoding)
    print(fp.closed)
    fp.write('{"year": 2018, "math": 90, "Chinese": 80, "is": {"physics": 100, "chem": 101}, 29: 57}')
    fp.writelines(('123' + os.linesep, '456'))
with open(file_path, 'r') as fp:
    while True:
        ch = fp.read(1)
        if not ch:
            break
        else:
            print(ch, end='')
with open(file_path, 'rb') as fp:
    while True:
        ch = fp.read(1)
        if not ch:
            break
        else:
            print(ch, end='')

with open(file_path, 'r', encoding='utf-8') as fp:
    while True:
        ch = fp.read()
        if not ch:
            break
        else:
            print(ch, end='')


