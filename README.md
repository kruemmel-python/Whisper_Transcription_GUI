# Whisper Transcription GUI

## Beschreibung
Diese Anwendung bietet eine einfache grafische Benutzeroberfläche (GUI) für die Transkription von MP3-Dateien mithilfe der OpenAI API. Mit dieser GUI können Benutzer:

- Einen OpenAI API-Schlüssel eingeben.
- Eine MP3-Datei für die Transkription auswählen.
- Einen Speicherort für die generierte Transkriptionsdatei auswählen.
- Die Transkription durch Anklicken eines Buttons starten.

Die Transkription erfolgt über das Modell "whisper-1" von OpenAI.

## Installation

1. Klone das Repository:
   ```sh
   git clone <repository-url>
   cd whisper-transcription-gui
   ```

2. Erstelle eine virtuelle Umgebung (optional):
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate    # Windows
   ```

3. Installiere die benötigten Abhängigkeiten:
   ```sh
   pip install -r requirements.txt
   ```

## Benutzung

1. Starte das Skript:
   ```sh
   python whisper_gui.py
   ```

2. Fülle die folgenden Felder aus:
   - **API Key**: Dein OpenAI API-Schlüssel, um auf die Whisper API zuzugreifen.
   - **MP3-Datei auswählen**: Wähle die Audiodatei aus, die du transkribieren möchtest.
   - **Speicherort wählen**: Bestimme, wo das Transkript gespeichert werden soll.

3. Klicke auf den **Bestätigen**-Button, um den API-Schlüssel zu überprüfen.

4. Klicke auf den **Transkript erstellen**-Button, um die Transkription zu starten.

## Abhängigkeiten

- Python 3.7+
- Tkinter (in den meisten Python-Distributionen enthalten)
- requests (für die API-Anfragen)
- bcrypt (für die Sicherheit des API-Schlüssels)
- pyperclip (um den API-Schlüssel in die Zwischenablage zu kopieren)

Die benötigten Abhängigkeiten sind in der Datei `requirements.txt` aufgelistet.

## Features

- Benutzerfreundliche GUI zur Verwaltung von MP3-Dateien, dem API-Schlüssel und dem Speicherort.
- Direkte Überprüfung des API-Schlüssels, bevor die Transkription gestartet wird.
- Die Ausgabe des Transkripts kann als Datei gespeichert werden.

## Lizenz
Dieses Projekt steht unter der MIT-Lizenz. Siehe die `LICENSE`-Datei für weitere Informationen.

## Kontakt
Bei Fragen oder Problemen bitte ein Issue im GitHub-Repository erstellen oder mich direkt kontaktieren.

Viel Spaß bei der Verwendung der Whisper Transcription GUI! Wenn dir das Projekt gefällt, hinterlasse gerne einen Stern auf GitHub.

