# the normal arguement should always come before the args and kwargs otherwise it will give an error

def funargs(normal, *args, **kwargs):
    print(normal)
    for items in args:
        print(items)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

harry = ["harry","mirage","nair","satish","aditya","kumar","sagar"]
normal = "I am a normal arguement and the following are the name of the students: "

kw = {"mirage":"monitor", "aditya":"bhadwa", "sahil":"kuttaman"}

funargs(normal,*harry, **kw)

