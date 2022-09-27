### Tu bom uvozil potrebne knjižnice
from unicodedata import name
import bottle
import glavni

SKRIVNOST = 'moja skrivnost'
PISKOTEK = 'idizračuna'


### Tu pa se bo nahajala moja koda
@bottle.get('/')
def osnovni_zaslon():
    age = input("Prosim vpišite svojo starost(naravno število): ")
    if int(age) >= 18:
        gender = input("Prosim izberite svoj spol: 1) M | 2) Ž: ")
        if gender != 'M' and gender != 'Ž':
            print('Poskusite ponovno')
            gender = input("Prosim izberite svoj spol: 1) M | 2) Ž: ")
        elif gender == 'M':
           print('Izbrali ste moški spol')
        elif gender == 'Ž':
            print('Izbrali ste ženski spol')

        weigh = input("Prosim vpišite svojo težo(naravno število): ")

        food = input("Prosim označite koliko ste pojedli v zadnjih urah: 1) NIČ | 2) SREDNJE | 3) VELIKO: ")
        if food != 'NIČ' and food != 'SREDNJE' and food != 'VELIKO':
            print('Poskusite ponovno')
            food = input("Prosim označite koliko ste pojedli v zadnjih urah: 1) NIČ | 2) SREDNJE | 3) VELIKO: ")

        wine_number = input('Prosim označite koliko ste popili kozarčkov (2dl) vina(naravno število): ')
    
        big_beer_number = input('Prosim označite koliko ste popili kozarčkov (0.5l) piva(naravno število): ')
        
        small_beer_number = input('Prosim označite koliko ste popili kozarčkov (0.25l) piva(naravno število): ')

        small_shot_number = input('Prosim označite koliko ste popili kozarčkov (30ml) žgane pijače(naravno število): ')

        single_shot_number = input('Prosim označite koliko ste popili kozarčkov (50ml) žgane pijače(naravno število): ')

        double_shot_number = input('Prosim označite koliko ste popili kozarčkov (100ml) žgane pijače(naravno število): ')

        champagne_number = input('Prosim označite koliko ste popili kozarčkov šampanjca (naravno število): ')
        
        seznamcek = []
        seznamcek += int(wine_number) * ['kozarcek_vina']
        seznamcek += int(big_beer_number) * ['veliko_pivo']
        seznamcek += int(small_beer_number) * ['malo_pivo']
        seznamcek += int(small_shot_number) * ['zganje_malo']
        seznamcek += int(single_shot_number) * ['zganje']
        seznamcek += int(double_shot_number) * ['zganje_dvojno']
        seznamcek += int(champagne_number) * ['sampanjec']
        pravi_podatki = glavni.Oseba(gender, int(age), int(weigh), food, seznamcek)
        hours_number = pravi_podatki.stevilo_ur()
        return f'Čez {hours_number} ur boste 0.0.'
    else:
        return f'Oprostite, niste dovolj stari, da bi opravljali ta test'















bottle.run(debug=True)

