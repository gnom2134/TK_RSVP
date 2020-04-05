class RSVPSystem:
    def __init__(self):
        self.text = []
        self.wps = 250
        self.time_gap = 60. / self.wps
        self.current_word = 0

    def set_text(self, text):
        self.text = text.split()
        self.current_word = 0

    def set_wps(self, wps):
        self.wps = wps
        self.time_gap = 60. / wps

    def next_word(self):
        self.current_word += 1
        if self.current_word > len(self.text):
            return ''
        else:
            return self.text[self.current_word]

    def change_wps(self, delta):
        self.wps += delta
        self.time_gap = 60. / self.wps

    def get_time_gap(self):
        return self.time_gap

    def step(self, x):
        self.current_word += x
        self.current_word = max(self.current_word, 0) % len(self.text)
