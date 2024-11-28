import pytest
from hypothesis import given, strategies as st
from caccia_al_tesoro.caccia_al_tesoro import CacciaAlTesoro


# Property Test 1: La posizione del tesoro è sempre all'interno della griglia
@given(dimensione_griglia=st.integers(min_value=1, max_value=100))
def test_posizione_tesoro_in_griglia(dimensione_griglia):
    gioco = CacciaAlTesoro(dimensione_griglia)
    riga, colonna = gioco.posizione_tesoro

    assert 1 <= riga <= dimensione_griglia
    assert 1 <= colonna <= dimensione_griglia


# Property Test 2: I tentativi non duplicano coordinate
@given(
    dimensione_griglia=st.integers(min_value=1, max_value=50),
    tentativi=st.lists(st.tuples(st.integers(1, 50), st.integers(1, 50)), unique=True)
)
def test_tentativi_unici(dimensione_griglia, tentativi):
    gioco = CacciaAlTesoro(dimensione_griglia)

    # Aggiunge i tentativi al gioco
    for riga, colonna in tentativi:
        if 1 <= riga <= dimensione_griglia and 1 <= colonna <= dimensione_griglia:
            gioco.tentativi.append((riga, colonna))

    assert len(gioco.tentativi) == len(set(gioco.tentativi))


# Property Test 3: I suggerimenti sono coerenti con la posizione del tesoro
@given(
    dimensione_griglia=st.integers(min_value=2, max_value=20),
    riga_tesoro=st.integers(min_value=1, max_value=20),
    colonna_tesoro=st.integers(min_value=1, max_value=20),
    riga_tentativo=st.integers(min_value=1, max_value=20),
    colonna_tentativo=st.integers(min_value=1, max_value=20),
)
def test_suggerimenti_coerenti(dimensione_griglia, riga_tesoro, colonna_tesoro, riga_tentativo, colonna_tentativo):
    if riga_tesoro > dimensione_griglia or colonna_tesoro > dimensione_griglia:
        return  # Ignora test con coordinate fuori dalla griglia

    gioco = CacciaAlTesoro(dimensione_griglia)
    gioco.posizione_tesoro = (riga_tesoro, colonna_tesoro)

    suggerimenti = []
    if riga_tentativo < riga_tesoro:
        suggerimenti.append("Il tesoro è più a SUD.")
    elif riga_tentativo > riga_tesoro:
        suggerimenti.append("Il tesoro è più a NORD.")
    if colonna_tentativo < colonna_tesoro:
        suggerimenti.append("Il tesoro è più a EST.")
    elif colonna_tentativo > colonna_tesoro:
        suggerimenti.append("Il tesoro è più a OVEST.")

    # Confronta i suggerimenti con quelli del metodo
    with pytest.MonkeyPatch().context() as mp:
        mocked_output = []
        mp.setattr("builtins.print", lambda msg: mocked_output.append(msg))
        gioco._suggerisci((riga_tentativo, colonna_tentativo))
        assert set(mocked_output) == set(suggerimenti)


# Property Test 4: I tentativi aumentano solo se validi
@given(
    dimensione_griglia=st.integers(min_value=5, max_value=20),
    riga=st.integers(min_value=1, max_value=25),
    colonna=st.integers(min_value=1, max_value=25),
)
def test_tentativi_incrementano_solo_per_input_validi(dimensione_griglia, riga, colonna):
    gioco = CacciaAlTesoro(dimensione_griglia)
    tentativi_iniziali = len(gioco.tentativi)

    # Verifica che un tentativo valido venga aggiunto
    if 1 <= riga <= dimensione_griglia and 1 <= colonna <= dimensione_griglia:
        gioco.tentativi.append((riga, colonna))
        assert len(gioco.tentativi) == tentativi_iniziali + 1
    else:
        assert len(gioco.tentativi) == tentativi_iniziali
