import json

# JSON
obj1 = {'year': [2018, 2019], "math": 90, "Chinese": 80, "is": {"physics": 100, "chem": 101}, 29: 57}
print(obj1)
with open("./resource/test.json", 'w') as fp:
    json.dump(obj1, fp)
with open("./resource/test.json", 'r') as fp:
    obj2 = json.load(fp)
    for k, v in obj2.items():
        print(type(v))
        print(k, v)
print(obj2)
