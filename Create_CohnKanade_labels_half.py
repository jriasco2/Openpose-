#!/usr/bin/python

import sys
import os

data_dir = sys.argv[1] # emotions root location
image_dir = sys.argv[2] # image root location
output = sys.argv[3] # txt output location

output_file = open(output, "w")

for directory in sorted(os.listdir(image_dir)):
    image_subdir = "%s/%s" % (image_dir, directory)

    for subdirectory in sorted(os.listdir(image_subdir)):
        if not subdirectory.startswith('.'):
            file_dir = "%s/%s/%s" % (image_dir, directory, subdirectory)

            emotion_dir = "%s/%s/%s" % (data_dir, directory, subdirectory)
            emotion_data = os.listdir(emotion_dir)

            num_images = len(os.listdir(file_dir))

            for idx, image_file in enumerate(sorted(os.listdir(file_dir))):
                if image_file.startswith('.'): # ignore hidden files
                    num_images -= 1
                    continue

                image_path = "%s/%s/%s: " % (directory, subdirectory, image_file.replace(".png", ""))
                output_file.write(image_path)

                if len(emotion_data) != 0: # if the amotion label exists
                    if idx < num_images/2: # first images are neutral
                        emotion = 0
                    else:
                        emotion_path = "%s/%s/%s/%s" % (data_dir, directory, subdirectory, emotion_data[0])
                        emotion_file = open(emotion_path, "r")
                        emotion = float(emotion_file.readline())
                        emotion_file.close()
                else: # tag image without emotion
                    emotion = -1

                output_file.write("%d\n" % emotion)
    print(directory)

output_file.close()
