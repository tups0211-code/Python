class student:
    branch = "MCA"

    def __init__(self,name):
        self.name = name
        print("self : ",self)
s1 = student("sam ram singh")

print("obj s1",s1)
print("class : ",student)
print("branch",s1.branch)
print("name : ",s1.name)
print(s1.name)     
