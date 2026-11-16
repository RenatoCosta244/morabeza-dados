"""Linha de comandos do projeto Morabeza (Sessão 3).

Uso:  python -m morabeza.cli --ilha Sal
"""
import argparse
import logging
import sys

from morabeza.apoio import faturacao_por_ilha, ler_vendas
from morabeza.config import carregar_config

logger = logging.getLogger(__name__)


def criar_parser() -> argparse.ArgumentParser:
    # TODO 5: cria um argparse.ArgumentParser com dois argumentos opcionais:
    #         --config (por defeito "config.yaml") e --ilha (sem valor por defeito).
    raise NotImplementedError("criar_parser ainda não está feita")


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    args = criar_parser().parse_args(argv)

    # TODO 6: carrega a configuração (args.config) e lê as vendas do ficheiro indicado nela.
    # TODO 7: regista no log: logger.info("Li %d vendas de %s", ...). Não uses print para isto.
    # TODO 8: calcula a faturação por ilha. Sem --ilha, imprime "Faturação total: <valor> <moeda>".
    #         Com --ilha, imprime "Faturação em <ilha>: <valor> <moeda>".
    #         Se a ilha não existir, logger.error(...) e devolve 1. No fim, devolve 0.
    raise NotImplementedError("main ainda não está feita")


if __name__ == "__main__":
    sys.exit(main())
