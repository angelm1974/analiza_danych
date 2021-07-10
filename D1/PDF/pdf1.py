import PyPDF2
pdfplikObj = open('nikon.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfplikObj)

print(pdfReader.numPages)
strona = pdfReader.getPage(3)
zmienna = strona.extractText()
pdfplikObj.close()

print(zmienna)
