from pypdf import PdfReader, PdfWriter

def main():
    reader = PdfReader(input('Input file path to desired pdf to split: '))
    writer = PdfWriter()
    writer.add_page(reader.pages[2])
    with open(input('File name: '), 'wb') as output_stream:
        writer.write(output_stream)

    # print(page.extract_text())

if __name__ == '__main__':
    main()