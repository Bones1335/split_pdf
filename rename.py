import csv
import os

def rename(filenames):
    file = 'names.csv'
    if file in filenames:
        with open(file, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=['NOM', 'Prénom'])
            for i, row in enumerate(reader):
                name = row['NOM'] + '_' + row['Prénom']
                if i >= len(filenames):
                    break
                file = filenames[i]
                if file.endswith('.pdf'):    
                    filenames[i] = os.rename(filenames[i], name + '.pdf')
    else:
        print('There is no CSV file to rename files with.')
              