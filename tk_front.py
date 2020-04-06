from tkinter import *
from tkinter.font import Font
from rsvp_system import RSVPSystem


class RSVPApp:
    def __init__(self):
        font = ('Symbol', 19)

        self.root = Tk()
        self.root.geometry('500x190')

        self.rsvp = RSVPSystem()
        self.is_running = False

        self.root.bind('<Key>', self.key_press)

        self.ar_up_label = Label(self.root, text='     \u21e7', width=0, height=0, anchor='w', fg='red',
                                 font=font)
        self.ar_down_label = Label(self.root, text='     \u21e9', width=0, height=0, anchor='w', fg='red',
                                   font=font)

        self.text = StringVar()
        self.text.set('')
        self.label = Label(self.root, textvariable=self.text, font=font,
                           width=0, height=0, anchor='w', bg='white')

        self.wps_text = StringVar()
        self.wps_text.set('WPS: ' + str(self.rsvp.get_wps()))
        self.wps_label = Label(self.root, textvariable=self.wps_text, font=font, width=0, height=0,
                               bg='white', anchor='w')

        self.frame = Frame(self.root, width=0, height=0)
        self.after = -1
        self.button_start = Button(self.frame, text='Run', font=font, command=self.start,
                                   width=0, height=0, anchor='w')
        self.button_stop = Button(self.frame, text='Stop', font=font, command=self.stop,
                                  width=0, height=0, anchor='w')

        self.entry = Entry(self.root, font=font)
        self.entry.insert(0, 'text.txt')

        self.ar_down_label.pack(fill=BOTH)
        self.label.pack(fill=BOTH)
        self.ar_up_label.pack(fill=BOTH)
        self.button_start.pack(fill=BOTH, side=LEFT, expand=True)
        self.button_stop.pack(fill=BOTH, side=LEFT, expand=True)
        self.frame.pack(fill=BOTH)
        self.entry.pack(fill=BOTH)
        self.wps_label.pack(fill=BOTH)

        self.root.mainloop()

    def key_press(self, event):
        if event.keysym == 'space':
            if self.is_running:
                self.stop()
            else:
                self.__update_word()
        elif event.keysym == 'Up':
            self.rsvp.change_wps(10)
            self.wps_text.set('WPS: ' + str(self.rsvp.get_wps()))
        elif event.keysym == 'Down':
            self.rsvp.change_wps(-10)
            self.wps_text.set('WPS: ' + str(self.rsvp.get_wps()))
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
        filename = self.entry.get()
        try:
            with open(filename, 'r') as file:
                self.set_text(file.read())
        except FileNotFoundError:
            self.set_text('FILE NOT FOUND!')
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
        self.__reset_after()

    def __reset_after(self):
        if self.after != -1:
            self.root.after_cancel(self.after)
        self.after = self.root.after(self.rsvp.get_time_gap(), self.__update_word)
