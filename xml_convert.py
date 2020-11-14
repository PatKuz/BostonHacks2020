import pandas as p
import xml.etree.ElementTree as xml
import sys, os

def convert(path_to_folder):
    rows = []
    for file in os.listdir(path_to_folder):
        if not file.startswith('.'):
            tree = xml.parse(path_to_folder+'/'+file)
            root = tree.getroot()
            for element in root.iter():
                print(element,file)
            row = 'TRAINING,gs://images/'+str(file)+','+
            print(row)

if __name__ == '__main__':
    try:
        p = str(sys.argv[1])
    except:
        print('Missing folder path')
    df = convert(p)
    df.to_csv(('/Users/pkuz/Desktop/BostonHacks2020'),index=None)
