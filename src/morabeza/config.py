"""Leitura da configuração do projeto (Sessão 3)."""
from pathlib import Path

import yaml

CHAVES_OBRIGATORIAS = ("ficheiro_vendas", "moeda")


class ConfigInvalida(Exception):
    """O ficheiro de configuração não existe ou falta-lhe alguma chave obrigatória."""


def carregar_config(caminho: str) -> dict:
    """Lê o ficheiro YAML e devolve um dicionário com a configuração."""
    # TODO 1: se o ficheiro não existir, levanta ConfigInvalida.
    if not Path(caminho).exists():
        raise ConfigInvalida(f"Ficheiro de configuração não encontrado: {caminho}")

    # TODO 2: abre o ficheiro e lê-o com yaml.safe_load.
    with open(caminho, encoding="utf-8") as ficheiro:
        config = yaml.safe_load(ficheiro)

    # Ficheiro vazio devolve None; YAML que não seja um mapa não serve.
    if not isinstance(config, dict):
        raise ConfigInvalida(f"Configuração inválida em {caminho}: esperava pares chave/valor")

    # TODO 3: vê que chaves obrigatórias faltam e levanta ConfigInvalida se faltar alguma.
    em_falta = [chave for chave in CHAVES_OBRIGATORIAS if chave not in config]
    if em_falta:
        raise ConfigInvalida(f"Chaves em falta na configuração: {', '.join(em_falta)}")

    # TODO 4: devolve o dicionário.
    return config
