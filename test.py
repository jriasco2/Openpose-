#!/usr/bin/python

import subprocess
import sys

openpose_data_dir_images = sys.argv[1]
openpose_output_dir_xml = sys.argv[2]
dir_face_file_clean_xml = sys.argv[3]
dir_labels_file_database = sys.argv[4]

#python test.py ../BNU-LSVED ../data_BNU-LSVED
#python test.py ../prueba/data ../prueba/xml ../prueba/data.txt ../prueba/label.txt

subprocess.check_call(['./ExecuteOpenposeBNU-LSVED.sh', openpose_data_dir_images, openpose_output_dir_xml])
subprocess.check_call(['./Create_BNU-LSVED_dataset_xy_and_label.py', openpose_output_dir_xml, dir_face_file_clean_xml, dir_labels_file_database])
dir1 = (subprocess.check_output(["readlink","-f",dir_face_file_clean_xml])).rstrip()
dir2 = (subprocess.check_output(["readlink", "-f", dir_labels_file_database])).rstrip()
subprocess.check_call(['./process_BNU_LSVED.py',dir1,dir2])
