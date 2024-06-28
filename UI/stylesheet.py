def apply_stylesheet(self):
    self.setStyleSheet("""
        QWidget {
            background-color: #2E3B55;
            color: #FFFFFF;
            font-family: Arial, sans-serif;
            font-size: 14px;
        }
        QPushButton {
            background-color: #F39C12;
            color: #FFFFFF;
            border: none;
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
        }
        QPushButton:hover {
            background-color: #D35400;
        }
        QLineEdit, QComboBox {
            background-color: #34495E;
            color: #FFFFFF;
            border: 1px solid #FFFFFF;
            padding: 10px;
            border-radius: 8px;
            margin: 10px 0;
        }
        QProgressBar {
            background-color: #34495E;
            border: 1px solid #FFFFFF;
            border-radius: 8px;
            text-align: center;
            height: 30px;
            margin: 10px 0;
        }
        QProgressBar::chunk {
            background-color: #F39C12;
            border-radius: 8px;
        }
        QLabel {
            margin: 10px 0;
        }
    """)
