import json

obj1 = {"math": 90, "Chinese": 80, "is": {"physics": 100, "chem": 101}, 29: 57}
print(obj1)
with open("./resource/test.json", 'w') as fp1:
    json.dump(obj1, fp1)
with open("./resource/test.json", 'r') as fp2:
    obj2 = json.load(fp2)
print(obj2)