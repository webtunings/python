class Test():
    def __init__(self):
        print("constructor")
        
    def method1(self, x, y):
        print(x, y)
    @staticmethod
    def method2 (a, b):
        print(a, b)
        

t1 = Test()
t1.method1(4,5)
t1.method2(4,5)
Test.method2(4,5)