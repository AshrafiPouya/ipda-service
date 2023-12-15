import os

def command_line(func):
    def inner(obj):
        fname = input('Enter filename: ')
       
        for root, dirs, files in os.walk("./ipda/exports"):
            if not fname in files:
                print('There is no such file')
                return
        f = open(f"./ipda/exports/{fname}", "r")

        result = func(obj, f.read())
        
        print("Operation completed successfully")

        if input("Print the text? [Y/n] ").lower() != "n":
            print(result)
        
        if input("Export the file? [Y/n] ").lower() != "n":
            obj.save_file()  
        
    return inner
