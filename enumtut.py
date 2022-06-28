l1 = ["bhindi", "aloo", "chopsticks", "chowmien"]

# i = 1
# for item in l1:
#     if i%2 != 0:
#         print(f"jarvis please buy {item}")
#     i+=1


for index,items in enumerate(l1):
    if index%2==0:
        print(f"jarvis please but{items}")
