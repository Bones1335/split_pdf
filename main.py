import os
from pypdf import PdfReader, PdfWriter
import split

def main():
    working_directory = input('Input directory path to desired pdf to split: ')
    os.chdir(working_directory)

    reader = PdfReader(input('PDF file name to split: '))
    split.split(reader)
            

if __name__ == '__main__':
    main()