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


class DG:

    def __init__(self, max_num):
        self.max_num = max_num
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.max_num:
            self.num = self.num + 1
            return self.num
        else:
            raise StopIteration()


if __name__ == '__main__':
    import time
    for n in DG(6):
        print(n)
        time.sleep(0.5)
