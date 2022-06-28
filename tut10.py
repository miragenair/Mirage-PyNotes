# dictionary is nothing but key value pairs
d1={}
# print(type(d1))
d2={"harry":"burger",
    "rohan":"fish",
    "shivansh":"roti",
    "shubham":{"b":"maggie","l":"roti","d":"chiken"}}
# d2["ankit"]="junk food"
# d2[420]="kebabs"
# print(d2)
# del d2[420]
print(d2["shubham"]["b"])
# d3=d2.copy()
# del d3["harry"]
# print(d2)
# print(d3)
d2.update({"leena":"toffee"})
# print(d2.keys())
# print(d2.items())