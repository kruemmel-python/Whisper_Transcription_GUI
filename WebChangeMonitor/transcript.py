import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import os

class TranscriptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transkriptions-App")
        self.root.geometry("500x300")

        # API-Key Eingabe
        self.api_key_label = tk.Label(root, text="API-Schlüssel:")
        self.api_key_label.pack(pady=5)
        self.api_key_entry = tk.Entry(root, width=50, show="*")
        self.api_key_entry.pack(pady=5)

        # API-Schlüssel Bestätigen Button
        self.verify_button = tk.Button(root, text="API-Schlüssel überprüfen", command=self.verify_api_key)
        self.verify_button.pack(pady=10)

        # MP3-Datei Auswahl
        self.audio_file_label = tk.Label(root, text="Keine Datei ausgewählt")
        self.audio_file_label.pack(pady=5)
        self.select_audio_button = tk.Button(root, text="MP3-Datei auswählen", command=self.select_audio_file)
        self.select_audio_button.pack(pady=5)

        # Speicherort für Transkriptdatei
        self.output_dir_label = tk.Label(root, text="Kein Speicherort ausgewählt")
        self.output_dir_label.pack(pady=5)
        self.select_output_button = tk.Button(root, text="Speicherort für Transkript auswählen", command=self.select_output_dir)
        self.select_output_button.pack(pady=5)

        # Transkript Button
        self.transcribe_button = tk.Button(root, text="Transkribieren", command=self.transcribe_audio)
        self.transcribe_button.pack(pady=20)

    def verify_api_key(self):
        api_key = self.api_key_entry.get()
        if not api_key:
            messagebox.showerror("Fehler", "Bitte geben Sie einen API-Schlüssel ein.")
            return
        headers = {'Authorization': f'Bearer {api_key}'}
        response = requests.get("https://api.openai.com/v1/models", headers=headers)
        if response.status_code == 200:
            messagebox.showinfo("Erfolg", "API-Schlüssel ist gültig.")
        else:
            messagebox.showerror("Fehler", "API-Schlüssel ist ungültig oder nicht erreichbar.")

    def select_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3-Dateien", "*.mp3")])
        if file_path:
            self.audio_file_path = file_path
            self.audio_file_label.config(text=os.path.basename(file_path))
        else:
            self.audio_file_label.config(text="Keine Datei ausgewählt")

    def select_output_dir(self):
        output_dir = filedialog.askdirectory()
        if output_dir:
            self.output_dir_path = output_dir
            self.output_dir_label.config(text=output_dir)
        else:
            self.output_dir_label.config(text="Kein Speicherort ausgewählt")

    def transcribe_audio(self):
        try:
            api_key = self.api_key_entry.get()
            audio_file_path = getattr(self, 'audio_file_path', None)
            output_dir_path = getattr(self, 'output_dir_path', None)

            if not api_key:
                messagebox.showerror("Fehler", "Bitte geben Sie einen API-Schlüssel ein.")
                return
            if not audio_file_path:
                messagebox.showerror("Fehler", "Bitte wählen Sie eine MP3-Datei aus.")
                return
            if not output_dir_path:
                messagebox.showerror("Fehler", "Bitte wählen Sie einen Speicherort aus.")
                return

            url = "https://api.openai.com/v1/audio/transcriptions"
            data = {
                'model': 'whisper-1',
                'language': 'en',
                'response_format': 'verbose_json'
            }

            headers = {'Authorization': f'Bearer {api_key}'}
            files = {'file': open(audio_file_path, 'rb')}

            response = requests.post(url, headers=headers, data=data, files=files)

            if response.status_code == 200:
                transcription = response.json()
                output_file_path = os.path.join(output_dir_path, "transcription.txt")
                with open(output_file_path, "w", encoding="utf-8") as f:
                    for segment in transcription['segments']:
                        f.write(f"Startzeit: {segment['start']}, Endzeit: {segment['end']}, Text: {segment['text']}\n")
                messagebox.showinfo("Erfolg", f"Transkription wurde gespeichert: {output_file_path}")
            else:
                messagebox.showerror("Fehler", f"Transkription fehlgeschlagen: {response.status_code}\n{response.text}")
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = TranscriptionApp(root)
    root.mainloop()