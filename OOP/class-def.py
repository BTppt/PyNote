# class def
class C0:
    """help doc"""

    def __init__(self):
        print('initialize a C0 object')
        self.cv1 = 0
        self.cv2 = 'a'

    def getvalue(self):
        print(self.cv1, self.cv2)


c1 = C0()
c1.getvalue()