"""Lab 5 · Extrair de quatro fontes.

As fontes estão em data/fontes_s1_2025/. Testa com:
    pytest tests/test_etl_lab5.py -v
"""

import json
import sqlite3

import pandas as pd


def ler_vendas_csv(caminho):
    """Lê o CSV de vendas com TUDO como texto (dtype=str), para não perder
    informação antes de limpar."""
    vendas = pd.read_csv(caminho, dtype=str)
    return vendas


def ler_produtos_excel(caminho):
    """Lê a folha 'produtos' do Excel."""
    produtos = pd.read_excel(caminho, sheet_name="produtos")
    return produtos


def ler_clientes_sqlite(caminho):
    """SELECT * FROM clientes. Dica: pd.read_sql_query(sql, conn)"""
    conn = sqlite3.connect(caminho)
    clientes = pd.read_sql_query("SELECT * FROM clientes", conn)
    conn.close()
    return clientes


def ler_promocoes_json(caminho):
    """O ficheiro imita a resposta de uma API: os registos estão em 'dados'.
    Se 'estado' não for 'ok', levanta ValueError."""
    with open(caminho, "r") as f:
        promocoes = json.load(f)
    if promocoes.get("estado") != "ok":
        raise ValueError("Erro na API de promoções")
    return pd.DataFrame(promocoes.get("dados", []))
