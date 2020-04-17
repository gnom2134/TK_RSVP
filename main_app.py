from tk_front import RSVPApp
from tkinter import filedialog
import tkinter

if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry('0x0')
    dirname = filedialog.askdirectory(parent=root, initialdir="/", title="Select directory to run program in")
    root.destroy()

    if dirname == ():
        print('Directory was not selected')
    else:
        app = RSVPApp(dirname)
        app.run()
