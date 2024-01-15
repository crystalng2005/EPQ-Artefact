import PyPDF2
import scrapy
import requests
from scrapy.http import HtmlResponse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import io 
import PyPDF2 
import urllib.request 
import scrapy 
from scrapy.item import Item 
from scrapy import Spider


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


class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = ["https://www.physicsandmathstutor.com/past-papers/a-level-physics/"]
    for pdf_url in pdf_urls:
        yield {'pdf_url': pdf_url}
        
    def parse(self, response: HtmlResponse):
        pdf_urls = response.css('a[href$=".pdf"]::attr(href)').extract()

        for pdf_url in pdf_urls:
            yield {'pdf_url': pdf_url}

'''
