from tkinter import *
from rsvp_system import RSVPSystem


class RSVPApp:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x200')
        self.rsvp = RSVPSystem()
        self.text = StringVar()
        self.text.set('')
        self.label = Label(self.root,  textvariable=self.text, font=('symbol', '18', 'bold'))
        self.label.pack(anchor='center')

    def set_text(self, text):
        self.rsvp.set_text(text)

    def start(self):
        self.update_word()
        self.root.mainloop()

    def update_word(self):
        word = self.rsvp.get_word()
        self.rsvp.step(1)
        self.text.set(word)
        self.root.after(self.rsvp.get_time_gap(), self.update_word)


app = RSVPApp()
app.set_text('''Летел ворон
    Сел на колоду
    Да бух в воду.
    Уж он мок, мок, мок,
    Уж он кис, кис, кис.
    Вымок, выкис, вылез, высох.
    Сел на колоду
    Да бух в воду''')
app.start()
