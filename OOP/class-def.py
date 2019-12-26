# class def
class C0:
    """help doc"""

    def __init__(self):
        print('initialize a C0 object')
        self.cv1 = 0
        self.cv2 = 'a'
        self.__cv3__ = 0
        self.__cv4__ = 'a'

    def getvalue(self):
        print(self.cv1, self.cv2)
        print(self.__cv3__, self.__cv4__)

    @staticmethod
    def info():
        print('this is a example')


c1 = C0()
c1.getvalue()
C0.info()
# dynamic property
c1.addv1 = 1


def foo(self):
    print('additional foo')
    print(self.cv1)


c1.addfoo = foo  #
c1.addfoo(c1)  # invoking
C0.getvalue(c1)  # invoking
