% rebase( 'base.tpl', title = 'igra')

<h1><big><b><center>Izračun čez koliko časa bo oseba trezna</center></b></big></h1>
<div>
  V primerna mesta napiši zahtevane stvari.
</div>
<div>
  Prosim upoštevaj opombo v oklepajih in vnesi tako vrednost, ki piše v oklepajih.
</div>

<form action="/igra/" method="post">
    <b>Tvoja starost(naravno stevilo):</b>
    <input type="text" name="age" autofocus autocomplete="off">
    <b>Tvoj spol(M ali Ž):</b>
    <input type="text" name="gender" autofocus autocomplete="off">
    <b>Svoja teža v kg(naravno število):</b>
    <input type="text" name="weigh" autofocus autocomplete="off">
    <b>Prosim izberite koliko ste pojedli v zadnjem času(NIČ ali SREDNJE ali VELIKO):</b>
    <input type="text" name="food" autofocus autocomplete="off">
    <b>Prosim označite koliko ste popili kozarčkov (2dl) vina(naravno število):</b>
    <input type="text" name="wine_number" autofocus autocomplete="off">
    <b>Prosim označite koliko ste popili kozarčkov (0.5l) piva(naravno število):</b>
    <input type="text" name="big_beer_number" autofocus autocomplete="off">
    <b>Prosim označite koliko ste popili kozarčkov (2.5 dl) piva(naravno število):</b>
    <input type="text" name="small_beer_number" autofocus autocomplete="off">
    <b>Prosim označite koliko ste popili kozarčkov (30ml) žgane pijače (naravno število):</b>
    <input type="text" name="small_shot_number" autofocus autocomplete="off">
    <b>Prosim označite koliko ste popili kozarčkov (50ml) žgane pijače (naravno število):</b>
    <input type="text" name="single_shot_number" autofocus autocomplete="off">
    <b>Prosim označite koliko ste popili kozarčkov (100ml) žgane pijače (naravno število):</b>
    <input type="text" name="doublle_shot_number" autofocus autocomplete="off">
    <b>Prosim označite koliko ste popili kozarčkov šampanjca (naravno število):</b>
    <input type="text" name="champagne_number" autofocus autocomplete="off">
    <button type="submit">Izračunaj!</button>
</form>

<a href = "/">Nazaj na začetno stran</a>