class student:
    def __init__(self,name, listofmarks):
        self.name= name
        self.listofmarks =listofmarks

    def average(self):
        sum = 0 
        for eachvalue in self.listofmarks:
            sum = sum + eachvalue

        average = sum/3
        print(average)

student1 = student("aditi",[78,89,67])
student1.average()
