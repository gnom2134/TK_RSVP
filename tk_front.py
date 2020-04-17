import tkinter
from tkinter import filedialog
from rsvp_system import RSVPSystem


class RSVPApp:
    def __init__(self, storage_dir):
        font = ('Symbol', 19)

        self.root = tkinter.Tk()
        self.root.geometry('500x160')

        self.rsvp = RSVPSystem(storage_dir)
        self.is_running = False

        self.root.bind('<Key>', self.key_press)

        self.ar_up_label = tkinter.Label(self.root, text='     \u21e7', width=0, height=0, anchor='w', fg='red',
                                         font=font)
        self.ar_down_label = tkinter.Label(self.root, text='     \u21e9', width=0, height=0, anchor='w', fg='red',
                                           font=font)

        self.text = tkinter.StringVar()
        self.text.set('')
        self.label = tkinter.Label(self.root, textvariable=self.text, font=font,
                                   width=0, height=0, anchor='w', bg='white')

        self.wps_text = tkinter.StringVar()
        self.wps_text.set('WPM: ' + str(self.rsvp.get_wps()))
        self.wps_label = tkinter.Label(self.root, textvariable=self.wps_text, font=font, width=0, height=0,
                                       bg='white', anchor='w')

        self.frame = tkinter.Frame(self.root, width=0, height=0)
        self.after = -1
        self.button_start = tkinter.Button(self.frame, text='Pick a file', font=font, command=self.start,
                                           width=0, height=0, anchor='w')
        self.button_stop = tkinter.Button(self.frame, text='Stop', font=font, command=self.stop,
                                          width=0, height=0, anchor='w')

        self.ar_down_label.pack(fill=tkinter.BOTH, padx=100)
        self.label.pack(fill=tkinter.BOTH, padx=100)
        self.ar_up_label.pack(fill=tkinter.BOTH, padx=100)
        self.button_start.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
        self.button_stop.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
        self.frame.pack(fill=tkinter.BOTH)
        self.wps_label.pack(fill=tkinter.BOTH)

    def run(self):
        self.root.mainloop()

    def key_press(self, event):
        if event.keysym == 'space':
            if self.is_running:
                self.stop()
            else:
                self.__update_word()
        elif event.keysym == 'Up':
            self.rsvp.change_wps(10)
            self.wps_text.set('WPM: ' + str(self.rsvp.get_wps()))
        elif event.keysym == 'Down':
            self.rsvp.change_wps(-10)
            self.wps_text.set('WPM: ' + str(self.rsvp.get_wps()))
        elif event.keysym == 'Right':
            self.stop()
            self.rsvp.step(1)
            self.text.set(self.rsvp.get_word())
        elif event.keysym == 'Left':
            self.stop()
            self.rsvp.step(-1)
            self.text.set(self.rsvp.get_word())

    def set_text(self, text):
        self.rsvp.set_text(text)

    def start(self):
        self.stop()
        filename = filedialog.askopenfilename(initialdir="/", title="Select file", parent=self.root,
                                              filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        if filename == ():
            self.rsvp.set_text('__false_value__')
        else:
            self.rsvp.set_text(filename)
        self.text.set(self.rsvp.get_word())
        self.__reset_after()

    def stop(self):
        self.is_running = False
        self.root.after_cancel(self.after)

    def __update_word(self):
        self.is_running = True
        self.rsvp.step(1)
        word = self.rsvp.get_word()
        self.text.set(word)
        self.__reset_after(len(word.strip()) > 12)

    def __reset_after(self, add_time=False):
        if self.after != -1:
            self.root.after_cancel(self.after)
        if add_time:
            self.after = self.root.after(int(self.rsvp.get_time_gap() * 1.5), self.__update_word)
        else:
            self.after = self.root.after(self.rsvp.get_time_gap(), self.__update_word)
