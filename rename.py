import csv

def rename():
    file = 'names.csv'
    
    with open(file, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['NOM'] + '_' + row['Prénom'])

rename()