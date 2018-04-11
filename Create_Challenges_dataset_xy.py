#!/usr/bin/python
import sys
import os
import xml.etree.ElementTree as xml_parser
import string
import subprocess

data_dir = sys.argv[1] # xml root location
output = sys.argv[2] # txt output location of 70 pair points

for directory in sorted(os.listdir(data_dir)):
    create_new_file = os.path.join(output, directory+".txt")
    output_file = open(create_new_file, "w")
    for xml_file in sorted(os.listdir("%s/%s" %(data_dir, directory))):
        if xml_file.endswith("face.xml"):
            xml = "%s/%s/%s" %(data_dir, directory, xml_file)
            xml_tree = xml_parser.parse(xml)
            root = xml_tree.getroot()
            #implementation of search of number matriz of detected points
            #raw_data = root[0][0].text
            #string_data = raw_data.split()[-210:]
            #print string_data[0]
            raw_data = root[0][2].text
            string_data = raw_data.split()[-210:]
            #print string_data
            if string_data[0] == 'u':
                print "U found in frama:", xml
                continue

            data = list(map(float,string_data))
            points = [data[i:i+3] for i in range(0, len(data),3)]
            #print points
            for x,y,z in points:
                text = "%s,%s" %(x,y)
                #print text
                output_file.write(text)
            output_file.write("\n")
    output_file.close()
