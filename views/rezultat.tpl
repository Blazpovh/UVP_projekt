% rebase( 'base.tpl', title = 'igra')

<h1><big><b><center>Izračun čez koliko časa bo oseba trezna</center></b></big></h1>

<div>
    Čez {{rezultat}} ur boste trezni (0.0)!
</div>


% end
    <form action="/nova_igra/" method="POST">
        <button type="submit">Nova igra</button>
    </form>
  
    <form action="/" method="GET">
        <button type="submit">Začetna stran</button>
    </form>