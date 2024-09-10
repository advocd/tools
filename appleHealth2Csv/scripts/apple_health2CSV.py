import xml.etree.ElementTree as ET
import csv
import os


# Ordnerpfad für die XML- und CSV-Dateien
data_folder = os.path.abspath('./data')

# Pfad zur XML-Datei und zur Ausgabe-CSV-Datei
xml_file = os.path.join(data_folder,'Export.xml')
csv_file = os.path.join(data_folder, 'health_data.csv')

print("--- Start xml parsen ---")

# XML-Datei parsen
tree = ET.parse(xml_file)
root = tree.getroot()

# Eine Liste, um alle Attribute zu speichern, die in der Datei vorkommen
all_attributes = set()

print("--- Zähle alle Records ---")

# Zähle die Gesamtanzahl der Record-Elemente (für den Fortschrittsbalken)
records = root.findall('Record')
total_records = len(records)

print(f"--- Anzahl Records: {total_records} ---")

print("--- Starte alle Attribute zu finden ---")
# Erster Durchlauf: Alle vorhandenen Attribute sammeln
for record in records:
    all_attributes.update(record.attrib.keys())

# Die gesammelten Attribute in eine Liste umwandeln und sortieren (optional)
all_attributes = sorted(list(all_attributes))

#input("Drücke die Eingabetaste, um fortzufahren...")

# Erstelle die CSV-Datei und schreibe die Kopfzeilen (alle gefundenen Attribute)
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=all_attributes)

    # Schreibe die Kopfzeilen
    writer.writeheader()

    # Zweiter Durchlauf: Die Daten in die CSV schreiben
    for i, record in enumerate(records, start=1):
        # Für jedes Record-Element: Schreibe die Attribute als Zeile in die CSV-Datei
        writer.writerow(record.attrib)

        # Fortschrittsanzeige
        if i % 100 == 0 or i == total_records:  # Fortschritt alle 100 Schritte anzeigen
            progress = (i / total_records) * 100
            print(f"Fortschritt: {progress:.2f}% ({i}/{total_records})")

print(f"Die XML-Daten wurden erfolgreich in {csv_file} umgewandelt!")
