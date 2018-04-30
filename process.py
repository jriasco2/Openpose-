import numpy as np

fn_data = 'data.txt'
fn_labels = 'label.txt'
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
np.save('X_BNU.npy', X)

y_list = []
with open(fn_labels) as f2:
    labels = f2.readlines()
    # print labels
    for i, y in enumerate(labels):
        y.rstrip()
        y2 = int(y)
        y_list.append(y2)

y = np.array(y_list)
np.save('y_BNU.npy', y)
#print(y)
#print(len(data))
#print(len(y))
