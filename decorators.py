def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec

@dec1
def who_is_mirage():
    print("mirage is a good boy")

who_is_mirage()

# -------------------------------practise decorators----------------------------------------------------------

def mirage(name):
    def now_exe():
        print("abhi execute ho raha h function name")
        name()
        print("abhi execute ho chuka h function name")
    return now_exe

@mirage
def who_is_mirage():
    print("mirage is a very good boy")

who_is_mirage()