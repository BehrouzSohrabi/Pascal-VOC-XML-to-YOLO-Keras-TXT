import re
import glob
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs

annotations = ''
filename_prefix = ''
filenames = glob.glob("data/*.xml")
for filename in filenames:
    row = filename_prefix + filename.split('data/')[1].replace('xml', 'jpg')
    with open(filename, "r") as file:
        content = file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        result = bs_content.find_all("object")
        for item in result:
            name = item.find('name').text
            xmin = item.xmin.text
            ymin = item.ymin.text
            xmax = item.xmax.text
            ymax = item.ymax.text
            row += ' ' + ','.join([xmin, ymin, xmax, ymax, name])
        annotations += row + '\n'

f = open("annoations.txt", "w")
f.write(annotations)
f.close()