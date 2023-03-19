class TWo:
    def foo(self): pass

class Damn(TWo):
    total = {}
    def __init__(self):
        self.total[1] = ["FC"]
    def foo(self):
        print("Damn class")
class Test(TWo):
    def __init__(self):
        a = 5
    def foo(self):
        print("Test class")
        
class Check(Test,Damn):
    def __init__(self):
        Test().foo()
        
        
obj = Check()