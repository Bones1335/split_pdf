import os
from pypdf import PdfReader, PdfWriter

def main():
    working_directory = input('Input directory path to desired pdf to split: ')
    os.chdir(working_directory)

    reader = PdfReader(input('PDF file name to split: '))
    
    start = 0
    end = 4

    for page in range(int(len(reader.pages) / 2)):
        writer = PdfWriter()
        new_file_name = str(page + 1) + '.pdf'
        for i in range(start,end):
            if i == len(reader.pages) or i > len(reader.pages):
                break
            writer.add_page(reader.pages[i])          
            with open (new_file_name, 'wb') as out:
                writer.write(out)

        start = end
        end = start + 4
            

if __name__ == '__main__':
    main()