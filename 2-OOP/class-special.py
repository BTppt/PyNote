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

