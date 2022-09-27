### Tu bom uvozil potrebne knjižnice


### Tu pa se bo začela moja koda
import json


slovar_enot = {'kozarcek_vina': 2, 'veliko_pivo': 2, 'malo_pivo': 1, 'zganje_malo': 1, 'zganje': 2, 'zganje_dvojno': 4, 'sampanjec': 1.5}
STEVILO_UR = 0
KOEFICIENT_SPOL = 0
LETO_PRI_KATEREM_IMA_POVPREČEN_ČLOVEK_NAJVEČJO_TOLERANCO = 25
KOEFICIENT_STAROST = 0
POVPRECNA_TEZA_MOSKI_SLO = 87
POVPRECNA_TEZA_ZENSKA_SLO = 68
KOEFICIENT_TEŽA = 0
KOEFICIENT_HRANA = 0
DATOTEKA_STANJE = 'stanje.json'







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
        global KOEFICIENT_HRANA
        if self.hrana == 'NIČ':
            KOEFICIENT_HRANA = 1.5
        elif self.hrana == 'SREDNJE':
            KOEFICIENT_HRANA = 1.36
        elif self.hrana == 'VELIKO':
            KOEFICIENT_HRANA == 1
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


### Od tu naprej nisem ziher; mislim, da rabim to za vmesnik
#class Igra:
#
#    def __init__(self, datoteka_s_stanjem):
#        self.datoteka_s_stanjem = datoteka_s_stanjem
#        self.nalozi_igro_iz_datoteke()
#
#   def prost_id_igre(self):
#       if len(self.igre) == 0:
#           return 0 #lahko vrne karkoli
#       else:
#           return max(self.igre.keys()) + 1
#
#   def nova_igra(self):
#       id_igre = self.prost_id_igre()
#       igra = nova_igra() #ker smo napisali brez self, smo klicali funkcijo, drugače pa bi metodo v istem razredu
#       self.igre[id_igre] = (igra)
#       self.zapisi_igre_v_datoteko() #vsakič ko se kaj spremeni zapišemo stanje
#       return id_igre
#
#   def nalozi_igre_iz_datoteke(self):
#       with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as f: 
#           igre = json.load(f)
#           self.igre = {int(id_igre): (Oseba(spol, starost, teža, hrana, seznam_popitih_pijac)) for id_igre, (spol, starost, teža, hrana, seznam_popitih_pijac) in igre.items()}

#   def zapisi_igre_v_datoteko(self):
#       with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as f:


    
     



    

        








    
