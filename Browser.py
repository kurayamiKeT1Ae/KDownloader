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
                if MP3:
                    _logs.addToLogs(f"CONVERTING {video.default_filename} TO MP3...")
                    if video.default_filename in os.listdir(path):
                        os.rename(f"{path}/{video.default_filename}", f"{path}/{video.default_filename[:-4]}.mp3")
                        _logs.addToLogs("DONE !")
                    else:
                        _logs.addToLogs(f"Failed to convert {video.default_filename} -> MP3")
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
            if MP3:
                _logs.addToLogs(f"CONVERTING {video.default_filename} TO MP3...")
                if video.default_filename in os.listdir(path):
                    os.rename(f"{path}/{video.default_filename}", f"{path}/{video.default_filename[:-4]}.mp3")
                    _logs.addToLogs("DONE !")
                else:
                    _logs.addToLogs(f"Failed to convert {video.default_filename} -> MP3")
        except Exception as e:
            print(e)
            _logs.addToLogs("FAILED !")

        Browser.pringLOGS(path, str(_logs))

