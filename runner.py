import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import PyQt5

import os



## ==> MAIN WINDOW
from main import Ui_MainWindow
from playlist_downloader import Playlist_Window
from video_downloader import Video_Window
from Browser import Browser

from configuration import Config

import time

import threading

QMainWindow = PyQt5.QtWidgets.QMainWindow

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

        self.ui.lineEdit.setText("")

    def mp3Downloader(self):
        _dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        URL = self.ui.lineEdit.text()
        if not (_dir in ["", None, " "]):
            DownloadThread = threading.Thread(target=Browser.downloadArray, args=(URL, _dir, True))
            DownloadThread.start()
        self.ui.lineEdit.setText("")
        

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
        self.ui.lineEdit.setText("")

    def mp3Downloader(self):
        _dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        URL = self.ui.lineEdit.text()
        if not (_dir in ["", None, " "]):
            DownloadThread = threading.Thread(target=Browser.DownloadLink, args=(URL, _dir, True))
            DownloadThread.start()
        self.ui.lineEdit.setText("")



class MAIN(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main = MainWindow()
        self.main.setupUi = self.main.ui.setupUi(self)
        self.playlistW = PlayListWindow()
        

        self.main.show()


def RUN():
    app = QApplication(sys.argv)
    window = MAIN()
    sys.exit(app.exec_())



if __name__ == "__main__":
    RUN()
    # isFile = os.path.exists
    # dataFileName = "data.kdownloader"
    # config = Config(path=dataFileName)
    # if isFile(dataFileName):
    #     if config.load()['installed_all']:
    #         RUN()
    #         print("run")
    #     else:
    #         print("exit 1")
    #         sys.exit()
    
    # else:
    #     config.build(data={
    #         "installed_all": False
    #     })
    #     if config.load()['installed_all']:
    #         RUN()
    #         print("run 2")
    #     else:
    #         if config._config():
    #             RUN()
    #             print('run 2')
    #         else:
    #             print('exit 2')
    #             sys.exit()

        