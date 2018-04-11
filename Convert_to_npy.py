#!/usr/bin/python

import numpy as np
import sys

# use ",%d,%d" as file format

data_path = sys.argv[1] # data path
label_path = sys.argv[2] # label path
data_output = sys.argv[3] # dataset output location
label_output = sys.argv[4] # label output location
image_output = sys.argv[5] # image description output location
data_size = int(sys.argv[6]) # size of data collected per image

data = np.loadtxt(data_path, dtype="f", delimiter=",", usecols=range(1,data_size+1))
label = np.loadtxt(label_path, dtype="i", delimiter=",", usecols=1)
image = np.loadtxt(data_path, dtype="S", delimiter=",", usecols=0)

np.save(data_output, data)
np.save(label_output, label)
np.save(image_output, image)
