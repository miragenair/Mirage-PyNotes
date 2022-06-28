class A:
    def met(self):
        print("this is a method in class A")

class B(A):
    def met(self):
        print("this is a method in class B")

class C(A):
    def met(self):
        print("this is a method in class C")

class D(C, B):
    def met(self):
        print("this is a method in class D")


#objects

a = A()
b = B()
c = C()
d = D()


d.met()




# -----------------------------------------------NOTES------------------------------------------------------------------
'''
    java doesnt allow multiple inheritanec
    python and c++ allows multiple inheritance
    
    
    diamond problem is solvable in python because of syntax
    in C++ is its difficult to solve but not impossible
    
'''