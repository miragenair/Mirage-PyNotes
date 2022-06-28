import pickle

file = "myiris.pkl"
fileboj = open(file, 'rb')
pettles = pickle.load(fileboj)
print(pettles)