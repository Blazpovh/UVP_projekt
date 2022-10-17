% rebase( "base.tpl", title = "igra")

<h1><big><b><center>Izračun čez koliko časa bo oseba trezna</center></b></big></h1>

<form action="/nova_igra/" method="POST">
    <button type="submit">Nova igra</button>
  </form>
  
  <form action="/" method="GET">
    <button type="submit">Začetna stran</button>
  </form>

<summary>
Ta program deluje tako, da na podlagi naših telesnih značilnosti, števila zaužite hrane v zadnjem času ter števila zaužitih alkoholnih pijač v zadnjem času izračuna čez koliko časa bo oseba trezna.
</summary>

<p>Oseba izbere svojo starost, spol, težo, koliko hrane ter alkoholnih pijač je zaužila v zadnjih urah.</p>
<p>Program nato iz zbranih podatkov izračuna grobo oceno, ki predstavlja število ur, ki jih oseba potrebuje, da bo trezna (0.0).</p>
