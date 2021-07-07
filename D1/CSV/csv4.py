import csv

przykladowy_plik = open("./poznan.csv", encoding='utf8')
przykladowy_reader = csv.DictReader(przykladowy_plik, delimiter=',')
print(type(przykladowy_reader))
# for row in przykladowy_reader:
#     print(row)


wyjscie = open("./poznan2.csv", 'w', encoding='utf8', newline='')
oDictWriter = csv.DictWriter(wyjscie, ['id', 'miasto', 'słońce', 'opady'])
oDictWriter.writeheader()
for row in przykladowy_reader:
    oDictWriter.writerow(row)
