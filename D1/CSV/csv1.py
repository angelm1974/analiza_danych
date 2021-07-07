import csv

przykladowy_plik=open("./dane.csv")
przykladowy_reader=csv.reader(przykladowy_plik,delimiter=';')
przykladowe_dane=list(przykladowy_reader)

zmienna=przykladowe_dane[7][1]
print(zmienna)

print(przykladowe_dane)
