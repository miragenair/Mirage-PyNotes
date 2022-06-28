class Dad:
    basketball = 1


class Son(Dad):
    dance = 1
    def isdance(self):
        return f"yes i dance {self.dance} no of times"

class Grandson(Son):
    dance = 5
    def isdance(self):
        return f"yes i dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())
print(larry.isdance())

print(harry.basketball)

# -----------------------------------------------------NOTES------------------------------------------------------------

'''
    THIS OOPS TUT IS ABOUT MULTI-LEVEL INHERITANCE
    
'''