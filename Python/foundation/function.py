# Function

## Definition
### positional and keyword-only argument
def myfun(p1, p2=0):
    """
    param p1: the added number 1
    param p2: the added number 2
    return: the sum
    """
    p1 = p1 ** p2
    return p1

print(myfun(2, 3))
print(myfun(p2=4, p1=2))
print(myfun(2))
print(myfun.__doc__)

# support packing and unpacking >> using Tuple
def unpacking(p1, p2, p3):
    return [p1, p2, p3]

def packing(p1, p2, p3):
    return p1, p2, p3

return_para_tuple = packing(1, 2, 3)
print(return_para_tuple)
return_p1, return_p2, return_p3 = unpacking('p1', 'p2', 'p3')
print(return_p1, return_p2, return_p3)

### arguments collection
def tsum(p1, *rp, p2):
    thesum = p1 + p2
    for num in rp:
        thesum += num
    return thesum

### print(tsum(1, 2, 3, 4)) >> TypeError: tsum() missing 1 required keyword-only argument: 'p2'
print(tsum(1, 2, 3, p2=4))
print(tsum(1, p2=4))  # *rp can be empty

def dictshow(number, *subjects, **table):
    print('the number of subjects is ', number)
    print('containing: ', subjects)
    print('scores: ', table)

dictshow(3, 'Math', 'Chines', 'Nature', Math=100, Chinese=100, Nature=100)

### reverse argument collection
def acmu(mp1, mp2):
    return mp1 * mp2

mp = (3, 4)
print(acmu(*mp))
mp = {'mp1': 3, 'mp2': 4}
print(acmu(**mp))
## Lambda Function
### Lambda
func = lambda n: n ** n
print(func(2))
### modifier
def funa(fn):
    print('A')
    fn()
    return 'fkit'

@funa
def funb():
    print('B')

print(funb)