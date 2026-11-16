"""Código antigo que alguém deixou no projeto. O ruff encontra aqui vários problemas."""
import os
import sys


def margem(preco_venda, preco_custo):
    diferenca = preco_venda - preco_custo
    if preco_venda == 0:
        return 0
    return (preco_venda - preco_custo) / preco_venda
