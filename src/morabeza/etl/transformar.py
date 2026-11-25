"""Lab 5 · Transformar (limpar) as vendas com funções puras.

Função pura = não altera o que recebe e devolve sempre o mesmo para a mesma
entrada. Testa com:
    pytest tests/test_etl_lab5.py -v
"""

import unicodedata

import pandas as pd

ILHAS_VALIDAS = ["Santiago", "São Vicente", "Sal", "Boa Vista", "Fogo", "Santo Antão"]

# abreviaturas que aparecem nos dados (chave já "achatada")
_ALIASES = {
    "stgo": "Santiago",
    "sv": "São Vicente",
    "svicente": "São Vicente",
    "boavista": "Boa Vista",
    "santao": "Santo Antão",
}


def _achatar(texto):
    """(VEM PRONTA) 'S. Vicente ' -> 'svicente' (minúsculas, sem acentos,
    só letras e números)."""
    sem_acentos = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return "".join(ch for ch in sem_acentos.lower() if ch.isalnum())


_CANON = {_achatar(i): i for i in ILHAS_VALIDAS} | _ALIASES


def normalizar_ilha(texto):
    """'  SAO vicente' -> 'São Vicente'. Ilha não servida, vazia ou None -> None.
    Dica: _CANON.get(_achatar(...))"""
    return _CANON.get(_achatar(texto))


def normalizar_data(texto):
    """Aceita '2025-03-01' e '01/03/2025'. Devolve pd.Timestamp; data
    impossível ou vazia -> pd.NaT. Dica: pd.to_datetime(..., format=..., errors="coerce")"""
    if pd.isna(texto) or texto == "":
        return pd.NaT
    try:
        return pd.to_datetime(texto, format="%Y-%m-%d", errors="raise")
    except ValueError:
        try:
            return pd.to_datetime(texto, format="%d/%m/%Y", errors="raise")
        except ValueError:
            return pd.NaT


def limpar_numero(serie):
    """(VEM PRONTA) '12 un' -> 12.0, '1250 CVE' -> 1250.0, '' -> NaN.
    A expressão regular apanha o primeiro número (com casas decimais opcionais)."""
    return (serie.astype("string")
                 .str.extract(r"(\d+(?:[.,]\d+)?)", expand=False)
                 .str.replace(",", ".", regex=False)
                 .astype(float))


def remover_duplicados(df):
    """Remove linhas com venda_id repetido (fica a primeira)."""
    return df.drop_duplicates(subset=["venda_id"], keep="first")


def limpar_vendas(df):
    """Junta tudo. NÃO altera o df original (usa .assign ou .copy()).
    Passos:
      1. remover duplicados
      2. normalizar ilha e data; limpar quantidade e preco_unitario
      3. remover linhas onde algum destes quatro ficou vazio
      4. quantidade e preco_unitario como int
    """
    df.copy()  # cria cópia para não alterar df original
    df = remover_duplicados(df)
    df = df.assign(
        ilha=df["ilha"].apply(normalizar_ilha),
        data=df["data"].apply(normalizar_data),
        quantidade=limpar_numero(df["quantidade"]),
        preco_unitario=limpar_numero(df["preco_unitario"]),
    )
    df = df.dropna(subset=["ilha", "data", "quantidade", "preco_unitario"])
    df["quantidade"] = df["quantidade"].astype(int)
    df["preco_unitario"] = df["preco_unitario"].astype(int)
    return df

if __name__ == "__main__":
    print(pd.__version__)
