import os
import pickle


class RSVPSystem:
    def __init__(self, storage_dir):
        self.storage_file = os.path.join(storage_dir, '.rsvp_settings')
        if '.rsvp_settings' in os.listdir(storage_dir):
            with open(self.storage_file, 'rb') as file:
                self.file_to_word = pickle.load(file)
            self.current_file = list(self.file_to_word.keys())[0]
            self.current_word = self.file_to_word[self.current_file]
            try:
                with open(self.current_file, 'r') as file:
                    self.text = file.read().split()
            except IOError:
                self.text = 'FILE NOT FOUND!'.split()
        else:
            self.current_file = '__base__'
            self.file_to_word = {}
            self.current_word = ''
            self.text = ['']
            self.current_word = 0
        self.wps = 250
        self.time_gap = (60. / self.wps) * 10**3

    def set_text(self, new_file):
        self.file_to_word[self.current_file] = self.current_word
        self.current_file = new_file
        try:
            with open(new_file, 'r') as file:
                self.text = file.read().split()
        except IOError:
            self.text = 'FILE NOT FOUND!'.split()
            self.current_file = '__base__'
        if new_file in self.file_to_word:
            self.current_word = self.file_to_word[new_file]
        else:
            self.current_word = 0

    def set_wps(self, wps):
        self.wps = max(wps, 1)
        self.time_gap = (60. / self.wps) * 10**3

    def get_word(self):
        return self.__add_spaces(self.text[self.current_word])

    def change_wps(self, delta):
        self.wps += delta
        self.set_wps(self.wps)

    def get_time_gap(self):
        return int(self.time_gap)

    def get_wps(self):
        return int(self.wps)

    def step(self, x):
        self.current_word += x
        self.current_word = max(self.current_word, 0) % len(self.text)

    def __del__(self):
        self.file_to_word[self.current_file] = self.current_word
        with open(self.storage_file, 'wb') as file:
            pickle.dump(self.file_to_word, file)

    @staticmethod
    def __add_spaces(word):
        wl = len(word)
        if wl == 1:
            bias = 1
        elif 1 < wl < 6:
            bias = 2
        elif 5 < wl < 10:
            bias = 3
        elif 9 < wl < 14:
            bias = 4
        else:
            bias = 5
        return ' ' * (6 - bias) + word
