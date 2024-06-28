from PyQt5.QtWidgets import QFileDialog

def select_audio(self):
    options = QFileDialog.Options()
    file, _ = QFileDialog.getOpenFileName(self, "Select Audio File", "", "Audio files (*.mp3 *.wav)", options=options)
    if file:
        self.audio_path = file
        self.status_label.setText("Audio file selected")
