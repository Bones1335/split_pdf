import csv
import os

def rename(filenames):
    
    with open('names.csv', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0
        for row in reader:
            name = row['NOM'] + '_' + row['Prénom']
            file = filenames[i]
            if file.endswith('.pdf'):    
                filenames[i] = os.rename(filenames[i], name + '.pdf')
            i += 1
              