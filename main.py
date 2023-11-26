from pypdf import PdfReader

def main():
    reader = PdfReader(input('Input file path to desired pdf to split: '))
    print(reader)

if __name__ == '__main__':
    main()