import csv
import sys

# Pfad zur CSV-Datei
csv_file = 'data/health_data.csv'

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
                # Entferne den 'HKQuantityTypeIdentifier' Präfix und speichere den Rest
                cleaned_identifier = cell.replace("HKQuantityTypeIdentifier", "")
                hk_identifiers.add(cleaned_identifier)
        
        # Fortschrittsanzeige nur alle 100 Zeilen oder bei der letzten Zeile aktualisieren
        print_progress(i, total_lines)

# Eindeutige und bereinigte Wörter ausgeben
print("\n\nFolgende bereinigte Bezeichner wurden gefunden:")
for identifier in sorted(hk_identifiers):
    print(identifier)
