import csv
import sys
import os

data_folder = os.path.abspath('./data')

# Pfad zur CSV-Datei und zur Ausgabe-Textdatei
csv_file = os.path.join(data_folder, 'health_data.csv')
output_file = os.path.join(data_folder, 'identifiers.txt')

# Set zum Speichern der eindeutigen Wörter, die mit 'HKQuantityTypeIdentifier' beginnen
hk_identifiers = set()

# Fortschrittsanzeige
def print_progress(current, total):
    if current % 100 == 0 or current == total:  # Fortschrittsanzeige nur alle 100 Zeilen
        progress = (current / total) * 100
        sys.stdout.write(f"\rFortschritt: {progress:.2f}% ({current}/{total})")
        sys.stdout.flush()

# Zähle die Gesamtzahl der Zeilen nur, wenn nötig (für die Fortschrittsanzeige)
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    total_lines = sum(1 for _ in file)  # Nur einmal zählen

# CSV-Datei lesen und die tatsächliche Verarbeitung durchführen
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Durch jede Zeile in der CSV-Datei gehen
    for i, row in enumerate(reader, start=1):
        # Durch jede Zelle in der Zeile gehen
        for cell in row:
            if isinstance(cell, str) and cell.startswith("HKQuantityTypeIdentifier"):
                # Speichere den vollständigen Identifier
                hk_identifiers.add(cell)
        
        # Fortschrittsanzeige nur alle 100 Zeilen oder bei der letzten Zeile aktualisieren
        print_progress(i, total_lines)

# Identifiers in eine Textdatei schreiben
with open(output_file, mode='w', encoding='utf-8') as f:
    for identifier in sorted(hk_identifiers):
        f.write(f"{identifier}\n")

# print(f"\n\nDie Identifikatoren wurden erfolgreich in {output_file} gespeichert!")
input(f"\n\nDie Textdatei mit den Identifikatoren wurden erfolgreich gespeichert in: \n    {output_file} \n\nWenn die Bearbeitung abgschlossen ist bitte hier mit Enter bestaetigen: \n" )
