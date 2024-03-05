import os

class FileHandler:


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FileHandler, cls).__new__(cls)
        return cls.instance


    @staticmethod
    def get_file_name(destination: str):
        fname = 0
        find = True
        while find:
            if not os.path.exists(f'./ipda/{destination}'):
                os.mkdir(path=f'./ipda/{destination}')
            for root, dirs, files in os.walk(f"./ipda/{destination}"):
                find = False
                for file in files:
                    if str(fname) == file.split('.')[0]:
                        fname += 1
                        find=True
                        continue
        return str(fname)


    def create_text_file(self, fname: str = None, *, content: str):

        if not content:
            print("there is nothing to export")
            return

        if not fname:
            fname = self.get_file_name("exports")


        f = open(f"./ipda/exports/{fname}.txt", "a")
        f.write(content)
        f.close()

        print("text file created")
