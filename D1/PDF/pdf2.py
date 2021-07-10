import PyPDF2
pdfplikObj = open('nikon.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfplikObj)

zmienna = ""
for z in range(pdfReader.numPages):
    strona = pdfReader.getPage(z)
    zmienna += strona.extractText()
pdfplikObj.close()

print(zmienna)
