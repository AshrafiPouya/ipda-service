from core.downloader import DownloadManager
from core.voice_to_text import VoiceToText
from core.text_summarization import TextSummarization
from core.text_to_voice import TextToVoice

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
                TextSummarization().summarize()
            
            case "ttv":
                TextToVoice.ttv()

            case _:
                print('invalid command, use help')
    

if __name__ == "__main__":
    start()
