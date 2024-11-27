import random
import argparse
import logging
import sys


class CacciaAlTesoro:
    """
    Classe per gestire il gioco della Caccia al Tesoro.
    """

    def __init__(self, dimensione_griglia: int) -> None:
        """
        Inizializza la griglia di gioco con la dimensione specificata.

        :param dimensione_griglia: Dimensione della griglia (es. 5x5, 7x7, etc.).
        """
        self.dimensione_griglia = dimensione_griglia
        self.posizione_tesoro = self._inizializza_gioco()
        self.tentativi = []
        self.trovato = False
        logging.info(f"Tesoro nascosto in posizione: {self.posizione_tesoro}")

    def _inizializza_gioco(self) -> tuple[int, int]:
        """
        Genera casualmente la posizione del tesoro.

        :return: Una tupla contenente le coordinate del tesoro (riga, colonna).
        """
        tesoro_colonna = random.randint(1, self.dimensione_griglia)
        tesoro_riga = random.randint(1, self.dimensione_griglia)
        return tesoro_riga, tesoro_colonna

    def _stampa_griglia(self) -> None:
        """
        Mostra la griglia con i tentativi dell'utente.
        """
        logging.debug("Aggiornamento griglia con i tentativi.")
        griglia = "\nGriglia:\n"
        for riga in range(1, self.dimensione_griglia + 1):
            for colonna in range(1, self.dimensione_griglia + 1):
                if (riga, colonna) in self.tentativi:
                    griglia += " X "
                else:
                    griglia += " . "
            griglia += "\n"
        print(griglia)

    def _suggerisci(self, tentativo_corrente: tuple[int, int]) -> None:
        """
        Fornisce un suggerimento per la posizione del tesoro.

        :param tentativo_corrente: Il tentativo attuale (riga, colonna).
        """
        riga, colonna = tentativo_corrente
        suggerimenti = []
        if riga < self.posizione_tesoro[0]:
            suggerimenti.append("Il tesoro è più a SUD.")
        elif riga > self.posizione_tesoro[0]:
            suggerimenti.append("Il tesoro è più a NORD.")
        if colonna < self.posizione_tesoro[1]:
            suggerimenti.append("Il tesoro è più a EST.")
        elif colonna > self.posizione_tesoro[1]:
            suggerimenti.append("Il tesoro è più a OVEST.")
        for suggerimento in suggerimenti:
            print(suggerimento)
            logging.info(suggerimento)

    def gioca(self) -> None:
        """
        Avvia il ciclo principale del gioco.
        """
        print("\nBenvenuto alla Caccia al Tesoro!")
        print(f"Il tesoro è nascosto in una griglia di {self.dimensione_griglia}x{self.dimensione_griglia}.")
        print("Prova a indovinare la posizione inserendo le coordinate (riga, colonna).\n")

        while not self.trovato:
            self._stampa_griglia()

            try:
                riga = int(input(f"Inserisci la coordinata riga (1-{self.dimensione_griglia}): "))
                colonna = int(input(f"Inserisci la coordinata colonna (1-{self.dimensione_griglia}): "))
            except ValueError:
                logging.warning("Input non valido, richiesta solo numeri.")
                print("Per favore, inserisci solo numeri validi.")
                continue

            if colonna < 1 or colonna > self.dimensione_griglia or riga < 1 or riga > self.dimensione_griglia:
                logging.warning("Coordinate fuori dalla griglia.")
                print("Coordinate fuori dalla griglia! Riprova.")
                continue

            tentativo_corrente = (riga, colonna)
            if tentativo_corrente in self.tentativi:
                logging.info("Tentativo già effettuato.")
                print("Hai già provato queste coordinate. Riprova.")
                continue

            self.tentativi.append(tentativo_corrente)
            logging.debug(f"Tentativo corrente: {tentativo_corrente}")

            if tentativo_corrente == self.posizione_tesoro:
                self.trovato = True
                logging.info(f"Tesoro trovato in {tentativo_corrente} dopo {len(self.tentativi)} tentativi.")
                print(f"\nComplimenti! Hai trovato il tesoro in ({riga},{colonna})!")
            else:
                self._suggerisci(tentativo_corrente)

        self._stampa_griglia()
        print(f"Hai trovato il tesoro in {len(self.tentativi)} tentativi. Grazie per aver giocato!")


def scegli_difficolta(difficolta: str) -> int:
    """
    Restituisce la dimensione della griglia in base alla difficoltà scelta.

    :param difficolta: Difficoltà scelta (facile, medio, difficile).
    :return: Dimensione della griglia corrispondente alla difficoltà.
    """
    if difficolta == "facile":
        return 5
    if difficolta == "medio":
        return 7
    if difficolta == "difficile":
        return 9

    logging.critical("Difficoltà non valida. Usa: facile, medio, o difficile.")
    sys.exit()


def setup_parser():
    """
    Imposta il parser degli argomenti della riga di comando.

    :return: L'oggetto parser con gli argomenti configurati.
    """
    parser = argparse.ArgumentParser(
        prog="caccia_al_tesoro",
        description="Gioco della Caccia al Tesoro."
    )

    parser.add_argument("--difficolta",
                        type=str,
                        required=True,
                        help="Difficoltà del gioco: facile, medio, o difficile",
                        choices=["facile", "medio", "difficile"])
    
    parser.add_argument("--log",
                        type=str,
                        default="WARNING",
                        help="Livello di logging: DEBUG, INFO, WARNING, ERROR, CRITICAL")

    return parser


def main():
    """
    Funzione principale per eseguire il gioco della Caccia al Tesoro.
    """
    parser = setup_parser()
    args = parser.parse_args()

    # Configura il livello di logging
    livello_logging = getattr(logging, args.log.upper(), None)
    if not isinstance(livello_logging, int):
        print("Livello di logging non valido. Usa: DEBUG, INFO, WARNING, ERROR, CRITICAL.")
        sys.exit(1)

    logging.basicConfig(level=livello_logging, format="%(asctime)s - %(levelname)s - %(message)s")

    dimensione_griglia = scegli_difficolta(args.difficolta)

    gioco = CacciaAlTesoro(dimensione_griglia)
    gioco.gioca()
