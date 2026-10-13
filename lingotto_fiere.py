import csv

import espositore
from stand import Stand
from stand import StandPremium
from espositore import Espositore


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.listaStand = []
        self.listaEspositori = []
        self.coppieStandEspositori = []




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
        esisteStand = False
        esisteEspositore = False
        for el in self.listaStand:
            if el.codice == codice_stand:
                esisteStand = True
                stand = el
        for el in self.listaEspositori:
            if el.codice == codice_espositore:
                esisteEspositore = True
                espositore = el
        standOccupato = False
        espositoreOccupato = False
        for el in self.coppieStandEspositori:
            if el[0] == codice_stand:
                standOccupato = True
            if el[1] == codice_espositore:
                espositoreOccupato = True

        if not esisteStand:
            raise Exception('stand non esistente')
        if not esisteEspositore:
            raise Exception('stand non esistente')
        if standOccupato:
            raise Exception('stand già occupato')
        if espositoreOccupato:
            raise Exception('espositore già assegnato')
        stand.espositore = codice_espositore
        espositore.stand = stand
        self.coppieStandEspositori.append([codice_stand, codice_espositore])



    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for el in self.listaEspositori:
            print(el)
            if el.stand is not None:
                print(f'Stand Assegnato a {el.codice}: {el.stand}')

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
