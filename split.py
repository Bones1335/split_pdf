from pypdf import PdfWriter

def split(reader):
    start = 0
    nth_page = int(input('Split every how many pages: '))
    end = nth_page

    for page in range(len(reader.pages)):
        writer = PdfWriter()
        if page < 9:
            new_file_name = '00' + str(page + 1) + '.pdf'
        elif page >= 9 and page < 99:
            new_file_name = '0' + str(page + 1) +'.pdf'
        elif page >= 99:
            new_file_name = str(page + 1) +'.pdf'
        for i in range(start,end):
            if i >= len(reader.pages):
                break
            writer.add_page(reader.pages[i])          
            with open (new_file_name, 'wb') as out:
                writer.write(out)

        start = end
        end = start + nth_page