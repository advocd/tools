import csv
import sys
import re
import os

data_folder = os.path.abspath('./data')

# Pfad zur CSV-Datei und zur Ausgabe-Textdatei
csv_file = os.path.join(data_folder, 'health_data.csv')
identifiers_file = os.path.join(data_folder, 'identifiers.txt')
output_csv_file = os.path.join(data_folder, 'filtered_health_data.csv')

# Set zum Speichern der Identifier aus der identifiers.txt-Datei
hk_identifiers = set()

# Fortschrittsanzeige
def print_progress(current, total):
    if current % 100 == 0 or current == total:  # Fortschrittsanzeige nur alle 100 Zeilen
        progress = (current / total) * 100
        sys.stdout.write(f"\rFortschritt: {progress:.2f}% ({current}/{total})")
        sys.stdout.flush()

# Schritt 1: Lese die Identifier aus der identifiers.txt-Datei
with open(identifiers_file, mode='r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()  # Entfernt Leerzeichen und Zeilenumbrüche
        if line.startswith("HKQuantityTypeIdentifier"):
            hk_identifiers.add(line)

# Überprüfen, ob Identifier eingelesen wurden
if not hk_identifiers:
    print("Keine gültigen Identifier in der identifiers.txt gefunden.")
    sys.exit(1)

# Funktion, um nicht druckbare Zeichen zu bereinigen
def clean_text(text):
    return re.sub(r'[^\x20-\x7E]+', '', text)

# Zähle die Gesamtzahl der Zeilen in der CSV-Datei, um den Fortschritt zu berechnen
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    total_lines = sum(1 for _ in file)  # Nur einmal zählen

# Schritt 2: Lese die CSV-Datei und filtere die Zeilen basierend auf den Identifiern
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Lese die Kopfzeile
    filtered_rows = []

    for i, row in enumerate(reader, start=1):
        # Bereinige jede Zelle in der Zeile von unsichtbaren Zeichen
        row = [clean_text(cell) for cell in row]

        # Prüfe, ob einer der Einträge in der Zeile in den Identifiers vorkommt
        if any(cell in hk_identifiers for cell in row):
            filtered_rows.append(row)

        # Fortschrittsanzeige nur alle 100 Zeilen oder bei der letzten Zeile aktualisieren
        print_progress(i, total_lines)

# Schritt 3: Schreibe die gefilterten Zeilen in eine neue CSV-Datei
with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Schreibe die Kopfzeile
    writer.writerows(filtered_rows)  # Schreibe die gefilterten Zeilen

print(f"\n\nDie gefilterten Daten wurden erfolgreich in {output_csv_file} gespeichert!")