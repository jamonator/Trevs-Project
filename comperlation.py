import sys
from PyQt5.QtWidgets import QApplication
from Video_Gen.media_compilation_maker import MediaCompilationMaker

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MediaCompilationMaker()
    ex.show()
    sys.exit(app.exec_())
