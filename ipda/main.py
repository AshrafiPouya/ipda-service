from core.downloader import DownloadManager
from core.voice_to_text import VoiceToText

def start():
    EOF = False
    while not EOF:
        user_input = input("$Home ")
        match user_input:
            case "exit":
                EOF = True
            
            case "download":
                DownloadManager.download_file()
            
            case "vtt":
                VoiceToText().vtt()
            
            case "ts":
                VoiceToText().vtt()

            case _:
                print('invalid command, use help')
    

if __name__ == "__main__":
    start()
    # download_file()