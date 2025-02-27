import pickle
import shelve
f = shelve.open('book')
for i in f:
    print(i," - ", f[i])
f.close()