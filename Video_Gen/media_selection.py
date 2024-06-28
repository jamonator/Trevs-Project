from PyQt5.QtWidgets import QFileDialog

def select_media(self):
    options = QFileDialog.Options()
    files, _ = QFileDialog.getOpenFileNames(self, "Select Media Files", "", "Media files (*.mp4 *.mts *.jpg *.jpeg *.png)", options=options)
    if files:
        self.media_paths = files
        self.status_label.setText(f"{len(files)} media files selected")
