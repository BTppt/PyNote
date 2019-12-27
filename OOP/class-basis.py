# class def
class C0:
    """help doc"""

    class_val = 0         # class variable

    def __init__(self):
        print('initialize a C0 object')
        self.cv1 = 0      # public variable
        self.__cv2 = 0    # private variable

    def getvalue(self):   # public method
        print(self.cv1, self.__cv2)

    @staticmethod
    def info():           # static method
        print('this is class C0')


# invoking member function
c1 = C0()
c1.getvalue()         # instance
print(c1.class_val)
C0.class_val = 1      # modifying class variable using class name
c2 = C0()
print(c2.class_val)
C0.getvalue(c1)       # class
C0.info()             # static method
c1.info()

# dynamic property
c1.add_v1 = 1


def foo(self):
    print('additional foo')
    print(self.cv1)


c1.add_foo = foo  #
c1.add_foo(c1)  # invoking added member function

# encapsulation
c3 = C0()
