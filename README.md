# caccia_al_tesoro v01

l progetto "Caccia al Tesoro" è un gioco scritto in Python che simula la ricerca di un tesoro nascosto in una griglia bidimensionale, in cui il giocatore interagisce attraverso un terminale.

L'obiettivo è indovinare la posizione esatta del tesoro nascosto all'interno della griglia specificando le coordinate (riga, colonna) tramite input dell'utente.
La griglia è di dimensioni variabili e viene scelta all'inizio in base al livello di difficoltà:
-Facile(5x5)
-Medio(7x7)
-Difficile(9x9)
Il gioco fornisce feedback sotto forma di suggerimenti direzionali (es. "Il tesoro è più a SUD"), guidando progressivamente il giocatore verso la soluzione.
Quando il giocatore individua la posizione esatta del tesoro, il programma termina congratulandosi e mostrando il numero totale di tentativi effettuati

## Installazione
```
python3 -m pip install .
```

## Utilizzo
```
 --help
usage: caccia_al_tesoro [-h] --difficolta {facile,medio,difficile}

Gioco della Caccia al Tesoro.

options:
  -h, --help            show this help message and exit
  --difficolta {facile,medio,difficile}
                        Difficoltà del gioco: facile, medio, o difficile
```

## Esempio
```
python3 caccia_al_tesoro.py --difficolta facile

Benvenuto alla Caccia al Tesoro!
Il tesoro è nascosto in una griglia di 5x5.
Prova a indovinare la posizione inserendo le coordinate (y, x).


Griglia:
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  .  .  . 

Inserisci la coordinata y (1-5): 3
Inserisci la coordinata x (1-5): 3
Il tesoro è più a NORD.
Il tesoro è più a OVEST.

Griglia:
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  X  .  . 
 .  .  .  .  . 
 .  .  .  .  . 

Inserisci la coordinata y (1-5): 2
Inserisci la coordinata x (1-5): 2
Il tesoro è più a OVEST.

Griglia:
 .  .  .  .  . 
 .  X  .  .  . 
 .  .  X  .  . 
 .  .  .  .  . 
 .  .  .  .  . 

Inserisci la coordinata y (1-5): 2
Inserisci la coordinata x (1-5): 1

Complimenti! Hai trovato il tesoro in (2,1)!

Griglia:
 .  .  .  .  . 
 X  X  .  .  . 
 .  .  X  .  . 
 .  .  .  .  . 
 .  .  .  .  . 

Hai trovato il tesoro in 3 tentativi. Grazie per aver giocato!
```
