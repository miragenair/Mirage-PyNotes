'''
iterable => __iter__() or __getitem__()
iterator => __next__()
iteration
'''
"""
this is a genetator
yield generates the value on the fly
when we want to save ram we use yield
"""

def gen(n):
    for i in range(n):
        yield i

g = gen(12)

for i in g:
    print(i)
