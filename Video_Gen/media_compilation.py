from compilation_thread import CompilationThread

def compile_media(self):
    if not self.media_paths or not self.audio_path:
        self.status_label.setText("Please select media and audio files")
        return

    self.status_label.setText("Compiling media...")
    self.progress.setValue(0)

    self.compilation_thread = CompilationThread(self.media_paths, self.audio_path, self.filter_menu.currentText(), self.overlay_menu.currentText())
    self.compilation_thread.progress.connect(self.update_progress)
    self.compilation_thread.finished.connect(self.on_compilation_complete)
    self.compilation_thread.start()

def on_compilation_complete(self, output_path):
    self.compiled_video_path = output_path
    self.status_label.setText("Compilation complete")
    self.open_video_button.setEnabled(True)
    self.progress.setValue(100)

def open_video(self):
    if self.compiled_video_path:
        os.startfile(self.compiled_video_path)
