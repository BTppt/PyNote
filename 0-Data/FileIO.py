from pathlib import *
import os
import json
import pickle

# file path
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
# JSON
# obj1 = [{'year': 2018, "math": 90, "Chinese": 80, "is": {"physics": 100, "chem": 101}, 29: 57},
#         {'year': 2019, "math": 95, "Chinese": 85, "is": {"physics": 105, "chem": 109}, 24: 67}]
# print(obj1)
# with open("./resource/test.json", 'w') as fp:
#     json.dump(obj1, fp)
# with open("./resource/test.json", 'r') as fp:
#     obj2 = json.load(fp)
# print(obj2)

# pkl
# obj3 = {}
# for num in range(0, 10):
#     obj3.update({num: num ** 2})
# with open('./resource/test.pkl', 'w') as fp:
#     pickle.dump(obj3, fp)
