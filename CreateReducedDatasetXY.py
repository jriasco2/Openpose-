#!/usr/bin/python

import sys
import os


def get_avg(point1, point2):
    pt1 = point1[1:-1].split(",")
    pt2 = point2[1:-1].split(",")

    x = (float(pt1[0]) + float(pt2[0]))/2
    y = (float(pt1[1]) + float(pt2[1]))/2
    acc = (float(pt1[2]) + float(pt2[2]))/2

    return output_format % (x,y)

data = sys.argv[1] # openpose X dataset
output = sys.argv[2] # directory to output the reduced dataset

if len(sys.argv) > 3:
    output_format = sys.argv[3] # data format, printf like sintax
else:
    output_format = "[%d,%d] "

dataset = open(data, "r")
output_data = open(output, "w")

sel_points = {
              "left_eye": 69,
              "right_eye": 68,
              "mouth_up": 62,
              "mouth_down": 66,
              "left_eyebrow": 
             }

left_eye = points[69]
right_eye = points[68]
mouth = get_avg(points[62], points[66])
left_eyebrow = points[24]
right_eyebrow = points[19]
nose = points[30]
mouth_left = points[54]
moutn_right = points[48]

for sample in dataset:
    sample_file, data_split = sample.split(":")

    points = data_split.split(" ")[1:-1] #get individual points and remove whitespace and new line

    left_eye = points[69]
    right_eye = points[68]
    mouth = get_avg(points[62], points[66])
    left_eyebrow = points[24]
    right_eyebrow = points[19]
    nose = points[30]
    mouth_left = points[54]
    moutn_right = points[48]

    reduced_points = [left_eye, right_eye, mouth, left_eyebrow, right_eyebrow, nose, mouth_left, moutn_right]

    output_str = "%s: %s \n" % (sample_file, " ".join(reduced_points))

    output_data.write(output_str)

dataset.close()
output_data.close()
