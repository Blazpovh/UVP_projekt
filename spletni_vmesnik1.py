import bottle
import glavni

bottle.TEMPLATE_PATH.insert(0,'Users/blazpovh/Documents/Projekti/UVP_projekt/views')
@bottle.get('/')
def osnovna_stran():
    return bottle.template("index.tpl")

@bottle.post("/nova_igra/")
def nova_igra():
    return bottle.template("igra.tpl")

@bottle.get("/igra/")
def pokazi_igro():
    return bottle.template("igra.tpl")

@bottle.post("/igra/")
def pokazi_rezultat():
    age = bottle.request.forms.getunicode("age")
    gender = bottle.request.forms.getunicode("gender")
    weigh = bottle.request.forms.getunicode("weigh")
    food = bottle.request.forms.getunicode("food")
    wine_number = int(bottle.request.forms.getunicode("wine_number"))
    big_beer_number =int(bottle.request.forms.getunicode("big_beer_number"))
    small_beer_number = int(bottle.request.forms.getunicode("small_beer_number"))
    small_shot_number = int(bottle.request.forms.getunicode("small_shot_number"))
    single_shot_number = int(bottle.request.forms.getunicode("single_shot_number"))
    doublle_shot_number = int(bottle.request.forms.getunicode("doublle_shot_number"))
    champagne_number = int(bottle.request.forms.getunicode("champagne_number"))
    seznamcek = []
    seznamcek += int(wine_number) * ['kozarcek_vina']
    seznamcek += int(big_beer_number) * ['veliko_pivo']
    seznamcek += int(small_beer_number) * ['malo_pivo']
    seznamcek += int(small_shot_number) * ['zganje_malo']
    seznamcek += int(single_shot_number) * ['zganje']
    seznamcek += int(doublle_shot_number) * ['zganje_dvojno']
    seznamcek += int(champagne_number) * ['sampanjec']
    podatki = glavni.Oseba(gender, int(age), int(weigh), food, seznamcek)
    rezultat = podatki.stevilo_ur()
    print('------------------------------------')
    print(rezultat, food, seznamcek)
    return bottle.template("rezultat.tpl",
                            age = age,
                            gender = gender,
                            weigh = weigh,
                            food = food,
                            seznamcek = seznamcek,
                            rezultat = rezultat)
                            
@bottle.get("/princip_racunanja/")
def pokazi_princip():
    return bottle.template("pojasnila.tpl")

bottle.run(debug=False)

