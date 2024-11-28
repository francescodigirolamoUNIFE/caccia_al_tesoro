import pytest
from unittest.mock import patch, MagicMock
from caccia_al_tesoro.caccia_al_tesoro import CacciaAlTesoro, scegli_difficolta


def test_inizializza_gioco_posizione_tesoro_nella_griglia():
    """
    Testa che la posizione del tesoro sia valida all'interno della griglia.
    """
    gioco = CacciaAlTesoro(dimensione_griglia=5)
    riga, colonna = gioco.posizione_tesoro
    assert 1 <= riga <= 5 and 1 <= colonna <= 5


def test_scegli_difficolta_facile():
    """
    Testa che la difficoltà 'facile' restituisca la dimensione corretta.
    """
    dimensione = scegli_difficolta("facile")
    assert dimensione == 5


def test_scegli_difficolta_medio():
    """
    Testa che la difficoltà 'medio' restituisca la dimensione corretta.
    """
    dimensione = scegli_difficolta("medio")
    assert dimensione == 7


def test_scegli_difficolta_difficile():
    """
    Testa che la difficoltà 'difficile' restituisca la dimensione corretta.
    """
    dimensione = scegli_difficolta("difficile")
    assert dimensione == 9


def test_gioco_aggiunge_tentativo():
    """
    Testa che un tentativo venga correttamente registrato nella lista.
    """
    gioco = CacciaAlTesoro(dimensione_griglia=5)
    gioco.tentativi.append((3, 3))
    assert (3, 3) in gioco.tentativi


@patch("builtins.input", side_effect=["3", "3"])
@patch("builtins.print")
def test_gioco_tesoro_trovato(mock_print, mock_input):
    """
    Testa che il gioco riconosca correttamente quando il tesoro è trovato.
    """
    gioco = CacciaAlTesoro(dimensione_griglia=5)
    gioco.posizione_tesoro = (3, 3)
    gioco.gioca()
    assert gioco.trovato is True


@patch("builtins.input", side_effect=["1", "1", "2", "2", "3", "3"])
@patch("builtins.print")
def test_gioco_tentativi_registrati(mock_print, mock_input):
    """
    Testa che i tentativi vengano registrati correttamente durante il gioco.
    """
    gioco = CacciaAlTesoro(dimensione_griglia=5)
    gioco.posizione_tesoro = (3, 3)
    gioco.gioca()
    assert len(gioco.tentativi) == 3


@patch("builtins.print")
def test_stampa_griglia(mock_print):
    """
    Testa che la griglia venga stampata correttamente.
    """
    gioco = CacciaAlTesoro(dimensione_griglia=3)
    gioco.tentativi = [(1, 1), (2, 2)]
    gioco._stampa_griglia()
    output = mock_print.call_args[0][0]
    assert "X" in output