ls = [i for i in range(100) if i%3==0]              #this is a comprehensions
# this is the normal way to code
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)

print(ls)

# dictionary = {i:f"item{i}" for i in range(100)}
dictionary = {i:f"Item{i}" for i in range(5)}


dictionary2 = {value:key for key, value in dictionary.items()}


print(dictionary,"\n",dictionary2)


dresses = {dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2","dress1","dress2","dress1","dress2", ]}
print(dresses)

evens = (i for i in range(100) if i%2==0)
print(evens.__next__())

for items in evens:
    print(items)