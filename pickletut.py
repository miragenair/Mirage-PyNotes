import pickle

#pickeling a python object
cars = ["Audi","Maruti Suzuki","ferrari", "miragecedes"]
file = "mycar.pkl"
fileobj = open(file, "wb")
pickle.dump(cars, fileobj)
fileobj.close()