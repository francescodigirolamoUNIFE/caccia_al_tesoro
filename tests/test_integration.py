import pytest
from io import StringIO
from unittest.mock import patch
from caccia_al_tesoro.caccia_al_tesoro import CacciaAlTesoro, scegli_difficolta


# Integration Test 1: Avvio del gioco con griglia piccola
def test_avvio_gioco_griglia_piccola():
    gioco = CacciaAlTesoro(5)
    assert gioco.dimensione_griglia == 5
    assert len(gioco.tentativi) == 0
    assert not gioco.trovato


# Integration Test 2: Verifica suggerimento per posizione del tesoro
def test_suggerimento_direzione():
    gioco = CacciaAlTesoro(5)
    gioco.posizione_tesoro = (3, 3)  # Impostazione manuale del tesoro
    with patch("builtins.print") as mocked_print:
        gioco._suggerisci((1, 1))
        mocked_print.assert_any_call("Il tesoro è più a SUD.")
        mocked_print.assert_any_call("Il tesoro è più a EST.")


# Integration Test 3: Verifica input e tentativi
def test_input_e_tentativi():
    gioco = CacciaAlTesoro(5)
    gioco.posizione_tesoro = (2, 2)  # Impostazione manuale del tesoro
    user_inputs = ["2", "2"]  # L'utente inserisce esattamente le coordinate giuste
    with patch("builtins.input", side_effect=user_inputs), patch("builtins.print"):
        gioco.gioca()
        assert len(gioco.tentativi) == 1
        assert gioco.tentativi[0] == (2, 2)
        assert gioco.trovato


# Integration Test 4: Selezione difficoltà e creazione gioco
def test_selezione_difficolta():
    difficolta = "medio"
    dimensione = scegli_difficolta(difficolta)
    assert dimensione == 7

    gioco = CacciaAlTesoro(dimensione)
    assert gioco.dimensione_griglia == 7
    assert len(gioco.tentativi) == 0
    assert not gioco.trovato
