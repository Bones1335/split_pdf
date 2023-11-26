import os
from pypdf import PdfReader, PdfWriter

def main():
    working_directory = input('Input directory path to desired pdf to split: ')
    os.chdir(working_directory)

    reader = PdfReader(input('PDF file name to split: '))
    writer = PdfWriter()
    writer.add_page(reader.pages[2])
    with open(input('New file name: '), 'wb') as output_stream:
        writer.write(output_stream)

    # print(page.extract_text())

if __name__ == '__main__':
    main()