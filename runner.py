import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import PyQt5

QMainWindow = PyQt5.QtWidgets.QMainWindow

## ==> MAIN WINDOW
from main import Ui_MainWindow
from playlist_downloader import Playlist_Window
from video_downloader import Video_Window
from Browser import Browser

import time

import threading

currentWin = "MAIN"

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        self.ui.playlistBtn.clicked.connect(self.open_playlistDownloaderWindow)
        self.ui.videoBtn.clicked.connect(self.open_videoDownloaderWindow)


    def open_playlistDownloaderWindow(self):
        self.playlistW = PlayListWindow()
        self.playlistW.show()
        self.hide()
        
    def open_videoDownloaderWindow(self):
        self.videoW = VideoWidnow()
        self.videoW.show()
        self.hide()


class PlayListWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Playlist_Window()
        self.ui.setupUi(self)
            
        self.ui.backArrowBtn.clicked.connect(self.back)
        self.ui.mp4_btn.clicked.connect(self.mp4Downloader)
        self.ui.mp3_btn.clicked.connect(self.mp3Downloader)
    

    def back(self):
        self.main = MainWindow()
        self.main.show()
        self.hide()

    def mp4Downloader(self):
        _dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        URL = self.ui.lineEdit.text()
        if not (_dir in ["", None, " "]):
            DownloadThread = threading.Thread(target=Browser.downloadArray, args=(URL, _dir, False))
            DownloadThread.start()

    def mp3Downloader(self):
        _dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        URL = self.ui.lineEdit.text()
        if not (_dir in ["", None, " "]):
            DownloadThread = threading.Thread(target=Browser.downloadArray, args=(URL, _dir, True))
            DownloadThread.start()
        

class VideoWidnow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Video_Window()
        self.ui.setupUi(self)

        self.ui.backArrowBtn.clicked.connect(self.back)
        self.ui.mp4_btn.clicked.connect(self.mp4Downloader)
        self.ui.mp3_btn.clicked.connect(self.mp3Downloader)
    

    def back(self):
        self.main = MainWindow()
        self.main.show()
        self.hide()

    def mp4Downloader(self):
        _dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        URL = self.ui.lineEdit.text()
        if not (_dir in ["", None, " "]):
            DownloadThread = threading.Thread(target=Browser.DownloadLink, args=(URL, _dir, False))
            DownloadThread.start()

    def mp3Downloader(self):
        _dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        URL = self.ui.lineEdit.text()
        if not (_dir in ["", None, " "]):
            DownloadThread = threading.Thread(target=Browser.DownloadLink, args=(URL, _dir, True))
            DownloadThread.start()



class MAIN(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main = MainWindow()
        self.main.setupUi = self.main.ui.setupUi(self)
        self.playlistW = PlayListWindow()
        

        self.main.show()


    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MAIN()
    sys.exit(app.exec_())