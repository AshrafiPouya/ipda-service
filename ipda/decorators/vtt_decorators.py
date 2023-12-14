import os

def command_line(func):
    def inner(obj):
        fname = input('Enter filename: ')
       
        for root, dirs, files in os.walk("./ipda/temp"):
            if not fname in files:
                print('There is no such file')
                return

        result = func(obj, fname)
        
        print("Operation completed successfully")

        if input("Print the text? [Y/n] ").lower() != "n":
            print(result)
        
        if input("Export the file? [Y/n] ").lower() != "n":
            obj.save_file()  # Assuming `save_file` is a method in the current or inherited class
        
    return inner