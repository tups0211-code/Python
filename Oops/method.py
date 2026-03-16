class student:
    

    def __init__(self,name):
        self.name = name

    def hello(self):    #fun-method
        print("hello", self.name)

s1 = student("sam ram singh")
s1.hello()
