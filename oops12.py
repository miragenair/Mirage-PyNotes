class A:
    classvar1 = "I am a class variable in the class A"
    def __init__(self):
        self.var1 = "I am inside the constructor of class A"
        self.classvar1 = "I am an instance variable in class A"
        self.special = "I am a special variable in class A"

class B(A):
    classvar1 = "I am a variable inside class B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside the constructor of class B"
        self.classvar1 = "I am an instance variable in class B"

        print(super().classvar1)

a = A()
b = B()

print(b.special)




# -----------------------------------------------NOTES------------------------------------------------------------------
'''
            THIS TUT IS ABPOUT OVERWRITTING
            
    sabse pehele preference class instance variable ko milti h
    
    uske baad agar koi cheeze overwrite hogayi toh uske pehele wali cheese k things ko access nahi reheta
    
    
    
'''