from PyQt5.QtWidgets import QWidget
from UI.ui_initialization import initUI
from Video_Gen.media_selection import select_media
from Video_Gen.audio_selection import select_audio
from Util.youtube_audio_download import download_audio_from_youtube, update_progress, on_download_complete
from Video_Gen.media_compilation import compile_media, on_compilation_complete, open_video
from UI.stylesheet import apply_stylesheet

class MediaCompilationMaker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.media_paths = []
        self.audio_path = None
        self.compiled_video_path = None

    initUI = initUI
    select_media = select_media
    select_audio = select_audio
    download_audio_from_youtube = download_audio_from_youtube
    update_progress = update_progress
    on_download_complete = on_download_complete
    compile_media = compile_media
    on_compilation_complete = on_compilation_complete
    open_video = open_video
    apply_stylesheet = apply_stylesheet
