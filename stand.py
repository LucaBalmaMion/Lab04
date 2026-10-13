class Stand:
    def __init__(self, riga):
        self.codice = riga[0]
        self.superficie = riga[1]
        self.padiglione = riga[2]
        self.prezzo = float(riga[3])
        try:
            self.preseInPiu = int(riga[4])
            self.prezzo = self.prezzo * (1 + 0.07 * self.preseInPiu)
        except IndexError:
            self.preseInPiu = None
    def __str__(self):
        stampa = f'{self.codice}, Superficie: {self.superficie}, Padiglione: {self.padiglione}, Prezzo: {self.prezzo}'
        if self.preseInPiu is not None:
            stampa += f', Prese in più: {self.preseInPiu}'
        return stampa



class StandPremium(Stand):
    def __init__(self, riga):
        super().__init__(riga[:4])
        self.posizione = riga[4]
        self.prezzo = self.prezzo * 1.30
    def __str__(self):
        return f'{super().__str__()}, Posizione {self.posizione}'

