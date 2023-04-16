import pickle

data ={}
file = open("GPS_Location.dat","rb")
try:
    while True:
        data = pickle.load(file)
        print(data)
except EOFError:
    file.close