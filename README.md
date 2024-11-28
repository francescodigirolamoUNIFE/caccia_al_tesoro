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
usage: caccia_al_tesoro [-h] --difficolta {facile,medio,difficile} [--log LOG]

Gioco della Caccia al Tesoro.

options:
  -h, --help            show this help message and exit
  --difficolta {facile,medio,difficile}
                        Difficoltà del gioco: facile, medio, o difficile
  --log LOG             Livello di logging: DEBUG, INFO, WARNING, ERROR, CRITICAL
```

## Esempio
```
caccia_al_tesoro --difficolta facile --log DEBUG

2024-11-28 15:58:42,650 - DEBUG - Tesoro nascosto in posizione: (2, 3)

Benvenuto alla Caccia al Tesoro!
Il tesoro è nascosto in una griglia di 5x5.
Prova a indovinare la posizione inserendo le coordinate (riga, colonna).

2024-11-28 15:58:42,651 - DEBUG - Aggiornamento griglia con i tentativi.

Griglia:
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  .  .  . 

Inserisci la coordinata riga (1-5): 3
Inserisci la coordinata colonna (1-5): 3
2024-11-28 15:59:05,844 - DEBUG - Tentativo corrente: (3, 3)
Il tesoro è più a NORD.
2024-11-28 15:59:05,844 - INFO - Il tesoro è più a NORD.
2024-11-28 15:59:05,844 - DEBUG - Aggiornamento griglia con i tentativi.

Griglia:
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  X  .  . 
 .  .  .  .  . 
 .  .  .  .  . 

Inserisci la coordinata riga (1-5): 2
Inserisci la coordinata colonna (1-5): 3
2024-11-28 15:59:19,463 - DEBUG - Tentativo corrente: (2, 3)
2024-11-28 15:59:19,463 - INFO - Tesoro trovato in (2, 3) dopo 2 tentativi.

Complimenti! Hai trovato il tesoro in (2,3)!
2024-11-28 15:59:19,463 - DEBUG - Aggiornamento griglia con i tentativi.

Griglia:
 .  .  .  .  . 
 .  .  X  .  . 
 .  .  X  .  . 
 .  .  .  .  . 
 .  .  .  .  . 

Hai trovato il tesoro in 2 tentativi. Grazie per aver giocato!
```
