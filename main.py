# Tukaj se bo nahajala moja glavna koda za projekt


class Banka:

    def __init__(self, zacetno_stanje):
        self.zacetno_stanje = zacetno_stanje

    def __str__(self):
        return f'Stanje na računu: {self.zacetno_stanje}'

    def __repr__(self):
        return f'Račun({self.zacetno_stanje})'

    def dvig(self, koliko):
        if koliko >= 0:
            if koliko < self.zacetno_stanje:
                self.zacetno_stanje -= koliko
                return True
            else:
                return False
    
    def polog(self, koliko):
        if koliko >= 0:
            self.zacetno_stanje += koliko
        return self.zacetno_stanje

def prenesi(racun1, racun2, koliko):
    if racun1.dvig(koliko):
        racun2.polog(koliko)
        return True
    return False
            