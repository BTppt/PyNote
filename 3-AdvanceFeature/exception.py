# Errors and Exceptions

try:
    y = int(input())
    x = 10/y
except ZeroDivisionError:
    print('zero division')
