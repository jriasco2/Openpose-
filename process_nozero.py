import numpy as np

fn_data = 'data.txt'
fn_labels = 'label.txt'
np.set_printoptions(threshold='nan')

x_list = []
zeros_list = []
with open(fn_data) as f:
    data = f.readlines()
    for i, x in enumerate(data):
        #Removing newline char
        x1 = x.rstrip()
        #Split at each comma
        x2 = x1.split(',')
        #Remove the first element of each list which is an empty string ''
        x2.pop(0)
        x4 = map(int, x2)
        if sum(x4) == 0:
           zeros_list.append(i)
           continue
        # x5 = np.array(x4)
        x_list.append(x4)

#print(len(x_list))
X = np.matrix(x_list)
np.save('X_BNU_nz.npy', X)

y_list = []
with open(fn_labels) as f2:
    labels = f2.readlines()
    # print labels
    for i, y in enumerate(labels):
        if i in zeros_list:
           continue
        y.rstrip()
        y2 = int(y)
        y_list.append(y2)

#print(len(y_list))
y = np.array(y_list)
np.save('y_BNU_nz.npy', y)
#print(y)
#print(len(data))
#print(len(y))
