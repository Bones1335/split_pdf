import csv
import os

def rename(filenames):
    file = 'names.csv'
    if file in filenames:
        with open(file, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=['NOM', 'Prénom'])
            i = 0
            for row in reader:
                name = row['NOM'] + '_' + row['Prénom']
                if i >= len(filenames):
                    break
                file = filenames[i]
                if file.endswith('.pdf'):    
                    filenames[i] = os.rename(filenames[i], name + '.pdf')
                i += 1
    else:
        print('There is no CSV file to rename files with.')
              