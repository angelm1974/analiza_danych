import csv
import os

os.makedirs("BezHeadera", exist_ok=True)

for plikcsv in os.listdir('.'):
    if not plikcsv.endswith('.csv'):
        continue
    print("Usuń nagłówek z", plikcsv)

    csvWiersze = []
    csvplik_obj = open(plikcsv)
    reader_csv = csv.reader(csvplik_obj)
    for wiersz in reader_csv:
        if reader_csv.line_num == 1:
            continue
        csvWiersze.append(wiersz)
    csvplik_obj.close()

    # zapis csv
    csvplik_obj = open(os.path.join("BezHeadera", plikcsv), "w", newline = '')
    csvWriter=csv.writer(csvplik_obj)
    for wiersz in csvWiersze:
        csvWriter.writerow(wiersz)
    csvplik_obj.close()
