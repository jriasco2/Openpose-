#!/usr/bin/python
import numpy as np
import sys

fn_data = sys.argv[1]
fn_labels = sys.argv[2]
#print fn_data + " " + fn_labels
np.set_printoptions(threshold='nan')

x_list = []
with open(fn_data) as f:
    data = f.readlines()
    for x in data:
        #Removing newline char
        x1 = x.rstrip()
        #Split at each comma
        x2 = x1.split(',')
        #Remove the first element of each list which is an empty string ''
        x2.pop(0)
        x4 = map(int, x2)
        # x5 = np.array(x4)
        x_list.append(x4)

X = np.matrix(x_list)
#np.save(os.path.join('/home/meyer/Openpose/prueba', 'X_BNU.npy'), X)
np.save(open("/home/meyer/Openpose/prueba/X_BNU.npy", "w"),X)
#np.save('X_BNU.npy', X)
#np.save('/home/meyer/Openpose/prueba/X_BNU.npy', X)

y_list = []
with open(fn_labels) as f2:
    labels = f2.readlines()
    # print labels
    for i, y in enumerate(labels):
        y.rstrip()
        y2 = int(y)
        y_list.append(y2)

y = np.array(y_list)
np.save(open("/home/meyer/Openpose/prueba/y_BNU.npy", "w"),y)
#np.save(os.path.join("/home/meyer/Openpose/prueba", "y_BNU.npy"), y)
#np.save('/home/Openpose/prueba/y_BNU.npy', y)
#np.save('y_BNU.npy', y)
#print(y)
#print(len(data))
#print(len(y))
