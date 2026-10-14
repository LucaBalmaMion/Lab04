import csv
from enum import nonmember

from stand import Stand
from stand import StandPremium
from espositore import Espositore
from operator import attrgetter

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.listaStand = []
        self.listaEspositori = []




    """Aggiungere setter e getter se necessari"""
    # TODO

    def è_uno_stand(self, codice):
        if codice.startswith("S"):
            return True
        else:
            return False

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        try:
            file = open(file_path, "r")
            infile = csv.reader(file)
            for line in infile:
                èStand = self.è_uno_stand(line[0])
                if èStand:
                    if len(line) == 4:
                        self.listaStand.append(Stand(line))
                    elif line[4].isdigit():
                        self.listaStand.append(Stand(line))
                    else:
                        self.listaStand.append(StandPremium(line))
                else:
                    self.listaEspositori.append(Espositore(line))

        except FileNotFoundError:
            raise FileNotFoundError





    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        stand = None
        espositore = None

        for el in self.listaStand:
            if el.codice == codice_stand:
                stand = el

        for el in self.listaEspositori:
            if el.codice == codice_espositore:
                espositore = el


        if stand is None:
            raise Exception('stand non esistente')
        if espositore is None:
            raise Exception('espositore non esistente')

        if stand.espositore is not None:
            raise Exception('stand già occupato')
        if espositore.stand is not None:
            raise Exception('espositore già assegnato')

        stand.espositore = codice_espositore
        espositore.stand = stand



    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for el in self.listaEspositori:
            print(el)
            if el.stand is not None:
                print(f'Stand Assegnato a {el.codice}: {el.stand}')

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        self.listaStand.sort(key=attrgetter('prezzo'))
        return self.listaStand
