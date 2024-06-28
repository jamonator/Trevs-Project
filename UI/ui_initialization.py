import os
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel, QProgressBar, QFileDialog, QComboBox, QLineEdit
from PyQt5.QtGui import QIcon

def initUI(self):
    self.setGeometry(100, 100, 400, 750)
    self.setWindowTitle('Media Compilation Maker')
    icon_path = os.path.abspath('C:/Users/61450/Documents/compeltion maker/images/icon.ico')
    self.setWindowIcon(QIcon(icon_path))

    layout = QVBoxLayout()

    self.select_media_button = QPushButton('Select Media', self)
    self.select_media_button.clicked.connect(self.select_media)
    layout.addWidget(self.select_media_button)

    self.select_audio_button = QPushButton('Select Audio from Computer', self)
    self.select_audio_button.clicked.connect(self.select_audio)
    layout.addWidget(self.select_audio_button)

    self.youtube_url_input = QLineEdit(self)
    self.youtube_url_input.setPlaceholderText("Enter YouTube URL")
    layout.addWidget(self.youtube_url_input)

    self.download_audio_button = QPushButton('Download Audio from YouTube', self)
    self.download_audio_button.clicked.connect(self.download_audio_from_youtube)
    layout.addWidget(self.download_audio_button)

    self.filter_label = QLabel('Select Filter', self)
    layout.addWidget(self.filter_label)

    self.filter_menu = QComboBox(self)
    self.filter_menu.addItems(["None", "Grayscale", "Sepia", "Invert"])
    layout.addWidget(self.filter_menu)

    self.overlay_label = QLabel('Select Overlay', self)
    layout.addWidget(self.overlay_label)

    self.overlay_menu = QComboBox(self)
    self.overlay_menu.addItems(["None", "Camcorder 1", "Camcorder 2"])
    layout.addWidget(self.overlay_menu)

    self.compile_button = QPushButton('Compile Media', self)
    self.compile_button.clicked.connect(self.compile_media)
    layout.addWidget(self.compile_button)

    self.progress = QProgressBar(self)
    layout.addWidget(self.progress)

    self.status_label = QLabel('', self)
    layout.addWidget(self.status_label)

    self.open_video_button = QPushButton('Open Video', self)
    self.open_video_button.setEnabled(False)
    self.open_video_button.clicked.connect(self.open_video)
    layout.addWidget(self.open_video_button)

    self.setLayout(layout)
    self.apply_stylesheet()
