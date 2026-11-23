import json
import os

NOME_ARQUIVO = "livros.json"


def ler_arquivo():
    if not os.path.exists(NOME_ARQUIVO):
        return []
    with open(NOME_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def gravar_arquivo(livros):
    with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(livros, f, ensure_ascii=False, indent=4)
