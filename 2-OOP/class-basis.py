# class def
class C0:
    """help doc"""

    class_val = 0  # class variable

    def __init__(self):
        print('initialize a C0 object')
        self.cv1 = 'cv1'  # public variable
        self.__cv2 = '__cv2'  # private variable

    def getvalue(self):  # public method
        print(self.cv1, self.__cv2)

    @staticmethod
    def info():  # static method
        print('this is class C0')


# invoking member function
c1 = C0()
c1.getvalue()  # instance
print(c1.class_val)
C0.class_val = 1  # modifying class variable using class name
c2 = C0()
print(c2.class_val)
C0.getvalue(c1)  # class
C0.info()  # static method
c1.info()

# dynamic property
c1.add_v1 = 1


def foo(self):
    print('additional foo')
    print(self.cv1)


c1.add_foo = foo  #
c1.add_foo(c1)  # invoking added member function
C0.add_foo_ = foo  # add function for class!
c2.add_foo_()

# encapsulation
c3 = C0()


# print(c3.__cv2) # error

# inheritance and derivation
class SubC0(C0):
    def __init__(self):
        super().__init__()
        print('this is a SubC0 instance')

    # override
    def getvalue(self):
        print(self.cv1)


c4 = SubC0()
c4.getvalue()
C0.getvalue(c4)


# type
class C1:
    pass


c5 = C1()
print(type(C1), type(c5))
C2 = type('C2', (object,), {'cv1': 1, 'cfoo': foo})
c6 = C2()
print(c6.cv1)
print(c6.cfoo())

# metaclass (__new__)
