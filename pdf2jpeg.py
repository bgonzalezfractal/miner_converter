import pdf2image
import os
from pdf2image import convert_from_path

pdf_path = 'pdfs/'
output_path = 'pdf2jpeg/'


for filename in os.listdir(pdf_path):
    ct = 0
    print(filename, ct)
    pages = convert_from_path(pdf_path + filename, 500)
    for page in pages:
        ct = ct + 1
        label = '{}_{}.jpeg'.format(filename,ct)
        page.save(output_path + label, 'JPEG')

