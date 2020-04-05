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
        return self.text[self.current_word]

    def change_wps(self, delta):
        self.wps += delta
        self.set_wps(self.wps)

    def get_time_gap(self):
        return int(self.time_gap)

    def step(self, x):
        self.current_word += x
        self.current_word = max(self.current_word, 0) % len(self.text)
