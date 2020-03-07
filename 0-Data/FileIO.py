from pathlib import *
import os

# Input and Output
msg = input('Please input: ')
print(msg)
# formatted string literals
year = 2019
event = 'Referendum'
print(f'Results of {year} {event}')
# format method
print('{} data event {} '.format(year, event))
# File path and Operation
file_path_s = PureWindowsPath('.\\resource\\test.txt')
print(file_path_s)
file_path = Path('.\\resource\\test.txt')
print(file_path)
with open(file_path, 'w', True) as fp:
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


