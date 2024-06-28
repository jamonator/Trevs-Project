from youtube_download_thread import YouTubeDownloadThread

def download_audio_from_youtube(self):
    url = self.youtube_url_input.text()
    if not url:
        self.status_label.setText("Please enter a YouTube URL")
        return

    self.status_label.setText("Downloading audio from YouTube...")
    self.progress.setValue(0)

    self.youtube_download_thread = YouTubeDownloadThread(url)
    self.youtube_download_thread.download_progress.connect(self.update_progress)
    self.youtube_download_thread.download_complete.connect(self.on_download_complete)
    self.youtube_download_thread.start()

def update_progress(self, progress):
    self.progress.setValue(progress)

def on_download_complete(self, audio_path):
    self.audio_path = audio_path
    self.status_label.setText("Audio download complete")
    self.progress.setValue(100)
