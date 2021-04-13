import pickle

# loading
load = pickle.load(open("pickle/test.pkl","rb"))
print (load.head)
