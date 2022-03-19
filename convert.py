import glob
from tqdm import tqdm
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs

def main():
    annotations = ''
    classes = set()
    filename_prefix = ''
    directory = 'labels'
    filenames = glob.glob(directory+"/*.xml")
    for filename in tqdm(filenames):
        row = filename_prefix + filename.split(directory+'/')[1].replace('xml', 'jpg')
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
                classes.add(name)
            annotations += row + '\n'

    f = open("annotations.txt", "w")
    f.write(annotations)
    f.close()

    f = open("classes.txt", "w")
    f.write('\n'.join(classes))
    f.close()

if __name__ == 'main':
    main()