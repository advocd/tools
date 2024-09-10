import subprocess
import os

# Pfad zum Skriptordner
script_folder = 'scripts'  # Hier ist der Ordner, wo deine Skripte liegen

# Liste der Skripte, die in einer bestimmten Reihenfolge ausgeführt werden sollen
# Trage die Skripte in der Reihenfolge ein, in der sie ausgeführt werden sollen
scripts_to_run = [
    'apple_health2CSV.py', # Schritt 1: Xml in CSV Datei umwandeln 
    'create_identifiers_file.py',  # Schritt 2: Textdatei mit den Identifiers erstellen
    'filter_health_data.py',       # Schritt 3: CSV-Datei filtern basierend auf Textdatei
    # Füge hier weitere Skripte in der gewünschten Reihenfolge hinzu
]

# Skripte in der angegebenen Reihenfolge ausführen
for script in scripts_to_run:
    script_path = os.path.join(script_folder, script)
    print(f"Starte Skript: {script_path}")
    
    # Skript mit subprocess ausführen
    # result = subprocess.run(['python', script_path], capture_output=True, text=True)
    result = subprocess.run(['python', script_path], text=True)
    
    # Überprüfen, ob das Skript erfolgreich war
    if result.returncode != 0:
        print(f"Fehler beim Ausführen von {script}.")
        print(result.stderr)
        break  # Beende, wenn ein Fehler auftritt
    else:
        print(f"{script} erfolgreich abgeschlossen!\n")

print("Alle Skripte wurden erfolgreich ausgeführt!")
