import docx


def pobierz_tekst(plik):
    doc = docx.Document(plik)
    tekst = []
    for p in doc.paragraphs:
        tekst.append(p.text)
    return '\n'.join(tekst)


dane=pobierz_tekst('praca1.docx')
print(dane)