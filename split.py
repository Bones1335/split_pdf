from pypdf import PdfWriter

def split(reader):
    start = 0
    nth_page = int(input('Split every how many pages: '))
    end = nth_page

    for page in range(len(reader.pages)):
        writer = PdfWriter()
        new_file_name = str(page + 1) + '.pdf'
        for i in range(start,end):
            if i == len(reader.pages) or i > len(reader.pages):
                break
            writer.add_page(reader.pages[i])          
            with open (new_file_name, 'wb') as out:
                writer.write(out)

        start = end
        end = start + nth_page