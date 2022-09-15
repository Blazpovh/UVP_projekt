# Tu bom uvozil potrebne stvari
import json
import random
import hashlib



# Od tu naprej pa bo koda

class Uporabnik:

    def __init__(self, uporabnisko_ime, geslo_zasifrirano, model):
        self.uporabnisko_ime = uporabnisko_ime
        self.geslo_zasifrirano = geslo_zasifrirano
        self.model = model


    @staticmethod
    def prijava(uporabnisko_ime, geslo_z_besedo):
        uporabnik = Uporabnik.preberi_datoteko(uporabnisko_ime)
        if uporabnik is None:
            raise ValueError("Uporabniško ime ne obstaja")
        elif uporabnik.preveri_geslo(geslo_z_besedo):
            return uporabnik
        else:
            raise ValueError("Geslo ni pravilno")


    @staticmethod
    def registracija(uporabnisko_ime, geslo_z_besedo):
        if Uporabnik.preberi_datoteko(uporabnisko_ime) is not None:
            raise ValueError("Uporabniško ime je že zasedeno")
        else:
            geslo_zasifrirano = Uporabnik.zasifriraj_geslo(geslo_z_besedo)
            uporabnik = Uporabnik(uporabnisko_ime, geslo_zasifrirano, Model())
            uporabnik.shrani_datoteko()
            return uporabnik

    @staticmethod
    def zasifriraj_geslo(geslo_z_besedo, sol=None):
        if sol is not None:
            sol = str(random.getrandbits(32))
        sposojeno_geslo = sol + geslo_z_besedo
        h = hashlib.blake2b()
        h.update(sposojeno_geslo.encode(encoding="utf-8"))
        return f"{sol}${h.hexdigest()}"

    def v_slovar(self):
        return {
            "uporabnisko_ime": self.uporabnisko_ime,
            "geslo_zasifirano": self.geslo_zasifrirano,
            "model": self.model.v_slovar(),
        }

    @staticmethod
    def ime_uporabnikove_datoteke(uporabnisko_ime):
        return f"{uporabnisko_ime}.json"


    def shrani_datoteko(self):
        with open(Uporabnik.ime_uporabnikove_datoteke(self.uporabnisko_ime), "w", encoding="utf-8") as datoteka:
            json.dump(self.v_slovar(), datoteka, ensure_ascii=False, indent=4)

    def preveri_geslo(self, geslo_z_besedo):
        sol, _ = self.geslo_zasifrirano.split("$")
        return self.geslo_zasifrirano == Uporabnik.zasifriraj_geslo(geslo_z_besedo, sol)

    @staticmethod
    def iz_slovarja(slovar):
        uporabnisko_ime = slovar["uporabnisko_ime"]
        geslo_zasifrirano = slovar["geslo_zasifrirano"]
        model = Model.iz_slovarja(slovar["model"])
        return Uporabnik(uporabnisko_ime, geslo_zasifrirano, model)

    @staticmethod
    def preberi_datoteko(uporabnisko_ime):
        try:
            with open(Uporabnik.ime_uporabnikove_datoteke(uporabnisko_ime), "r", encoding="utf-8") as datoteka:
                slovar = json.load(datoteka)
                return Uporabnik.iz_slovarja(slovar)
        except FileNotFoundError:
            return None






