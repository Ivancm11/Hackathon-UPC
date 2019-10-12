#Set-Up
import os
import PyPDF2
import tabula

#Read
pdf_name=""
pdfFileObj=open(pdf_name,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
text=pageObj.extractText()
#df = tabula.read_pdf(pdf_name,pages='all',multiple_tables=True)

