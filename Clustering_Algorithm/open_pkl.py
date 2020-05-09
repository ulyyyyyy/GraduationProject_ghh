import pickle

f = open('km.pkl','rb')
data = pickle.load(f)
print(data)