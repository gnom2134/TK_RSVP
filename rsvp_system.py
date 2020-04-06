class RSVPSystem:
    def __init__(self):
        self.text = ['']
        self.wps = 250
        self.time_gap = (60. / self.wps) * 10**3
        self.current_word = 0

    def set_text(self, text):
        self.text = text.split()
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

    def __add_spaces(self, word):
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
