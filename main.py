import os
from pypdf import PdfReader
from send2trash import send2trash
import split

def main():
    working_directory = input('Input directory path to desired pdf to split: ')
    os.chdir(working_directory)

    original_file = input('PDF file name to split: ')
    reader = PdfReader(original_file)
    split.split(reader)
    send2trash(original_file)

            

if __name__ == '__main__':
    main()