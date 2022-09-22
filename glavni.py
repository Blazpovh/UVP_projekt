### Tu bom uvozil potrebne knjižnice


### Tu pa se bo začela moja koda
slovar_enot = {'kozarcek_vina': 2, 'veliko_pivo': 2, 'malo_pivo': 1, 'zganje_malo': 1, 'zganje': 2, 'zganje_dvojno': 4, 'sampanjec': 1.5}
STEVILO_UR = 0
KOEFICIENT_SPOL = 0
LETO_PRI_KATEREM_IMA_POVPREČEN_ČLOVEK_NAJVEČJO_TOLERANCO = 25
KOEFICIENT_STAROST = 0
POVPRECNA_TEZA_MOSKI_SLO = 87
POVPRECNA_TEZA_ZENSKA_SLO = 68
KOEFICIENT_TEŽA = 0
KOEFICIENT_HRANA = 1






class Oseba:

    def __init__(self, spol, starost, teža, hrana, seznam_popitih_pijac):
        self.spol = spol
        self.starost = starost
        self.teža = teža
        self.hrana = hrana
        self.seznam_popitih_pijac = seznam_popitih_pijac

    def spol_osebe(self):
        if self.spol == 'M':
            KOEFICIENT_SPOL = 1
        else:
            KOEFICIENT_SPOL = 1.1
        return KOEFICIENT_SPOL

    def starost_osebe(self):
        razlika_let = self.starost - LETO_PRI_KATEREM_IMA_POVPREČEN_ČLOVEK_NAJVEČJO_TOLERANCO
        # to moram še bolj natančno izračunati
        if self.starost >= 18:
            if razlika_let >= 0:
                KOEFICIENT_STAROST = 1 + razlika_let / 100
            else:
                KOEFICIENT_STAROST = 1 - razlika_let / 100
        return KOEFICIENT_STAROST

    def teza_osebe(self):
        if self.spol == 'M':
            razlika_teze = self.teža - POVPRECNA_TEZA_MOSKI_SLO
            if razlika_teze >= 0:
                KOEFICIENT_TEŽA = 1 - razlika_teze / 100
            else:
                KOEFICIENT_TEŽA = 1 - razlika_teze / 100
            return KOEFICIENT_TEŽA
        else:
            razlika_teze = self.teža - POVPRECNA_TEZA_ZENSKA_SLO
            if razlika_teze >= 0:
                KOEFICIENT_TEŽA = 1 - razlika_teze / 100
            else:
                KOEFICIENT_TEŽA = 1 - razlika_teze / 100
            return KOEFICIENT_TEŽA

    def hrana_osebe(self):
        #groba ocena
        #Vir : https://www.duidefensewi.com/how-food-affects-alcohol-consumption/
        if self.hrana == 'NIČ':
            KOEFICIENT_HRANA = 1.5
        elif self.hrana == 'SREDNJE':
            KOEFICIENT_HRANA = 1.36
        return KOEFICIENT_HRANA

    def skupni_koeficient(self):
        koef_skupni = (Oseba.starost_osebe(self) + Oseba.teza_osebe(self) + Oseba.spol_osebe(self) + Oseba.hrana_osebe(self)) / 4
        return koef_skupni

    def stevilo_ur(self):
        ST_UR = 0
        for pijaca in self.seznam_popitih_pijac:
            ST_UR += slovar_enot[pijaca]
        skupno_stevilo_ur = ST_UR * Oseba.skupni_koeficient(self)
        return round(skupno_stevilo_ur, 2)



    

        








    
