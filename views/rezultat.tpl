% rebase( 'base.tpl', title = 'igra')

<h1><big><b><center>Izračun čez koliko časa bo oseba trezna</center></b></big></h1>

% if int(age) < 18:
    <div>
        Oprostite, niste dovolj stari, da bi opravljali ta izračun!
    </div>

% if gender != 'M' and gender != 'Ž':
    <div>
        Prosim poiskusite ponovno!
    </div>

% if food != 'NIČ' and food != 'SREDNJE' and food != 'VELIKO'::
    <div>
        Prosim poiskusite ponovno!
    </div>

% if rezultat >= 0:
    <div>
        Čez int(rezultat) ur boste trezni (0.0)!
    </div>

    <form action="/nova_igra/" method="POST">
        <button type="submit">Nova igra</button>
    </form>
  
    <form action="/" method="GET">
        <button type="submit">Začetna stran</button>
    </form>