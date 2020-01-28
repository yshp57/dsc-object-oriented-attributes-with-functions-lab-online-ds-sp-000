class School:
    def __init__(self, name=None, roster={}):
        self.name = name
        self.roster = roster
        
    def add_student(self, fullname, grade):
        if grade not in self.roster.keys():
            self.roster[grade] = [fullname]
        else:
            self.roster[grade].append(fullname)
            
    def grade(self, grade):
        return self.roster[grade]
    
    def sort_roster(self):
        for grade in self.roster:
            self.roster[grade] = sorted(self.roster[grade])
        return self.roster