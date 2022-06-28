import pickle

#----------------------------------------------perfect code-------------------------------------------------------------
f = open("iris.data", "r")
lines = f.readlines()

print(lines)

l2 = [item.split(",") for item in lines if len(item)!=0]
print(l2)

with open("myiris.pkl", "wb") as f:
    pickle.dump(l2, f)

# smallsets = lines.split("\n")

# for items in lines:
#     smallsets = items.split(",")
#     print(smallsets)

# def printbhai():
#     for item in f:
#         sp = item.split("\n")
#         # return sp
#         return item
#
# print(printbhai())

# print(item)

#----------------------------------------------perfect code ends here---------------------------------------------------

# file = "pettles1.pkl"
# fileobj = open(file, "wb")
# pickle.dump(sp, fileobj)
# fileobj.close()
#
# f.close()
