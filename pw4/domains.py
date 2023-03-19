class Same_fnc:
    def in_list(self): pass

class Student(Same_fnc): 
    total = {{}}
    
    def __init__(self, id, name, dob):
        self.total[int(id)]["name"] = name
        self.total[int(id)]["dob"] = dob
        self.total[int(id)]["grade"] = {}
        
    def in_list(self, id):
        if int(id) in self.total:
            return True
        else:
            return False
        
class Course(Same_fnc):
    total = {{}}
    
    def __init__(self, id, name, ect):
        self.total[int(id)]["name"] = name
        self.total[int(id)]["ect"] = ect
        
    def in_list(self, id):
        if id in self.total:
            return True
        else:
            return False