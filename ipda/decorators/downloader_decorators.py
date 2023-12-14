import os

def command_line(func):
    def inner():
        url = input('give me url: ')
        whatis = input('media type? ')

        fname = 0
        find = True
        while find:
            for root, dirs, files in os.walk("./ipda/temp"):
                find = False
                for file in files:
                    if str(fname) == file.split('.')[0]:
                        fname += 1
                        find=True
                        continue
        fname = f"{fname}.{whatis}"

        func(url=url, address='./ipda/temp/', fname=fname, chunk_size=1024)
        print(f"download completed successfully done file name is: {fname}")
    return inner
