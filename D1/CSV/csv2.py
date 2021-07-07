import csv

przykladowy_plik = open("./dane.csv")
przykladowy_reader = csv.reader(przykladowy_plik, delimiter=';')
#przykladowe_dane = list(przykladowy_reader)
lista = []
for wiersz in przykladowy_reader:
    if wiersz[1] == "Warszawa":
        lista.append(wiersz)

for l in lista:
    print(f'{l[1]} dane {l[2]} dane 2')
    

output_plik=open('filtrowane.csv',"w",newline='')
oWriter=csv.writer(output_plik)
oWriter.writerow(["id","miasto","słońce","opady"])
for l in lista:
    oWriter.writerow(l)
output_plik.close()