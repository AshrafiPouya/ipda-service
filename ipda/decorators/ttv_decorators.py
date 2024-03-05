import os

def command_line(func):
    def inner():
        file_name = input('Enter filename: ')
       
        for root, dirs, files in os.walk("./ipda/exports"):
            if not file_name in files:
                print('There is no such file')
                return
            
        audio_name = input('Enter audio name: ')
        if not os.path.exists('./ipda/resources'):
                os.mkdir(path='./ipda/resources')
        for root, dirs, files in os.walk("./ipda/resources"):
            if not audio_name in files:
                print('There is no such file')
                return

        func(file_name, audio_name)
        
    return inner
