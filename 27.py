class A: 
  def show(self): 
    print("Class A") 
class B(A): 
 def show(self): 
    print("Class B") 
obj = B() 
obj.show()