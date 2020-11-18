import json
import os
import webbrowser
import sys
from colorama import Fore, Back, Style,init
from pytube import Playlist
from pytube import YouTube
import pytube
init()

class Logs:

    def __init__(self):
        self.logs = []

    def addToLogs(self, message=""):
        self.logs.append(message)

    def __repr__(self):
        message = ''
        for msg in self.logs:
            message += msg+"\n"
        return message

class Browser:
    
    @staticmethod
    def getAllLinks_PlayList(playList):
        pl = Playlist(playList)
        for linkprefix in pl.parse_links():
            yield linkprefix




    @staticmethod
    def downloadArray(URL, path, MP3=True):
        _logs = Logs()
        urls = (Browser.getAllLinks_PlayList(URL))
        for url in urls:
            try:
                yt = pytube.YouTube(url)

                video = yt.streams.get_highest_resolution()
            except:
                _logs.addToLogs((f"FAILED TO GET URL:  {url}"))
                continue
            _logs.addToLogs(f"DOWNLOADING: {video.title}")
            try:
                video.download(path)
                _logs.addToLogs(f"DONE !")
                file = video.title
                file = file.replace(",", "").replace(".", "").replace("'", "")
                FILE = f"{file}.mp4"
                if MP3:
                    _logs.addToLogs(f"CONVERTING {FILE} TO MP3...")
                    if FILE in os.listdir():
                        os.rename(f"{file}.mp4", f"{file}.mp3")
                        _logs.addToLogs("DONE !")
                    else:
                        _logs.addToLogs(f"Failed to convert {FILE} -> MP3")
            except:
                _logs.addToLogs("FAILED !")
                
        Browser.pringLOGS(path, str(_logs))
        
    @staticmethod
    def pringLOGS(filePath, logs="LOGS..."):
        with open(f"{filePath}\\LOGS.txt", 'w') as file:
            file.writelines(logs)


    @staticmethod
    def DownloadLink(URL, /, path, MP3=True):
        url = URL
        _logs = Logs()
        try:
            yt = pytube.YouTube(url)

            video = yt.streams.get_highest_resolution()
        except:
            _logs.addToLogs(f"FAILED TO GET URL:  {url}")
            Browser.pringLOGS(_logs)
            return None

        _logs.addToLogs(f"DOWNLOADING: {video.title}")
        try:
            video.download(path)
            _logs.addToLogs(f"DONE !")
            file = video.title
            file = file.replace(",", "").replace(".", "").replace("'", "")
            FILE = f"{file}.mp4"
            if MP3:
                _logs.addToLogs(f"CONVERTING {FILE} TO MP3...")
                if FILE in os.listdir():
                    os.rename(f"{file}.mp4", f"{file}.mp3")
                    _logs.addToLogs("DONE !")
                else:
                    _logs.addToLogs(f"Failed to convert {FILE} -> MP3")
        except:
            _logs.addToLogs("FAILED !")

        Browser.pringLOGS(path, str(_logs))

