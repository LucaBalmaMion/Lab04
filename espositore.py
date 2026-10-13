class Espositore:
    def __init__(self, riga):
        self.codice = riga[0]
        self.nome = riga[1]
        self.cognome = riga[2]
        self.stand = None
    def __str__(self):
        return f'{self.codice}, {self.nome}, {self.cognome}'