import PyPDF2


def extract_pages_by_keywords(input_pdf_path, output_pdf_path, keywords):
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)
    pdf_writer = PyPDF2.PdfWriter()

    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        text = page.extract_text()

        if any(keyword in text for keyword in keywords):
            pdf_writer.addPage(page)

    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

# Usage
'''
input_pdf_paths = ['input1.pdf', 'input2.pdf', 'input3.pdf']
input_pdf_path = 'input.pdf'
output_pdf_path = 'output.pdf'
keywords = ["Keyword1", "Keyword2"]
extract_pages_by_keywords(input_pdf_path, output_pdf_path, keywords)
'''



