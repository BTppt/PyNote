# Advanced Feature and Related Built-in Lib
import sys
import os
import json

# sys >> System-specific parameters and functions
# The list of strings that specifies the search path for modules.
for p in sys.path:
    print(p)
# The list of command line arguments passed to a Python script
print(sys.argv)
# A string giving the absolute path of the executable binary for
# the Python interpreter, on systems where this makes sense.
print(sys.executable)
# A string containing the version number of the Python interpreter
# plus additional information on the build number and compiler used.
print(sys.version)

# os >> Miscellaneous operating system interfaces
# Return the value of the environment variable key if it exists,
# or default if it doesn’t. key, default and the result are str.
print(os.getenv('PATH'))

# json >> JSON encoder and decoder
myjson = json.dumps({'math':90, 'chinese':100},indent=4)
print(myjson)
print(type(myjson))
data = json.loads(myjson)
print(data)
print(type(data))

mfp = open('mine.json','r')
temp = json.load(mfp)
print(type(temp))
for item in temp.items():
    print(item)
mfp.close()

mfp = open('mine.json', 'w')
json.dump(temp,fp=mfp,indent=4)
mfp.close()

# fileinput >> Iterate over lines from multiple input streams



