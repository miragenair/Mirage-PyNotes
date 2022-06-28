import time

initial = time.time()
k=0
while(k<=45):
    print("hello harry bhai")
    # time.sleep(2)
    k+=1
print("while loop completed in ", time.time()-initial)


initial2 = time.time()
for i in range(45):
    print("hello harry bhai")
print("for loop completed in ", time.time()- initial2)


localtime = time.asctime(time.localtime(time.time()))
print(localtime)