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
    parser = argparse.ArgumentParser(
        description="Faturação Morabeza",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--config",
        default="config.yaml",
        metavar="FICHEIRO",
        help="ficheiro de configuração",
    )
    parser.add_argument(
        "--ilha",
        metavar="NOME",
        help="nome da ilha para filtrar a faturação (sem valor: todas)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    args = criar_parser().parse_args(argv)

    # TODO 6
    config = carregar_config(args.config)
    vendas = ler_vendas(config["ficheiro_vendas"])

    # TODO 7
    logger.info("Li %d vendas de %s", len(vendas), config["ficheiro_vendas"])
    

    # TODO 8
    por_ilha = faturacao_por_ilha(vendas)
    moeda = config["moeda"]

    if args.ilha is None:
        total = sum(por_ilha.values())
        print(f"Faturação total: {total:.0f} {moeda}")
        return 0

    # Pesquisa sem distinguir maiúsculas/minúsculas (ex.: "santiago" == "Santiago")
    ilhas = {nome.casefold(): nome for nome in por_ilha}
    nome = ilhas.get(args.ilha.casefold())
    if nome is None:
        logger.error("A ilha %s não existe", args.ilha)
        return 1

    print(f"Faturação em {nome}: {por_ilha[nome]:.0f} {moeda}")
    return 0    
if __name__ == "__main__":
    sys.exit(main())
