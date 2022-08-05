import csv
import fasttext as ft


with open('.tdata.csv') as c:
    reader = csv.reader(c)
    with open('./model.txt', 'w', encoding='UTF-8') as f:
        for row in reader:
            f.write('__label__' + row[0] + ' , ' + row[1]+ '\n')

