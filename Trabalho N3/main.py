from arquivo import ler_arquivo
from livros import incluir, alterar, excluir
from busca import pesquisar
from ordenacao import listar

livros = ler_arquivo()

while True:
    print("\n====== BIBLIOTECA ======")
    print("1 - Incluir livro")
    print("2 - Alterar livro")
    print("3 - Excluir livro")
    print("4 - Pesquisar livro")
    print("5 - Listar livros")
    print("0 - Sair")
    opcao = input("Opcao: ")

    if opcao == "1":
        incluir(livros)
    elif opcao == "2":
        alterar(livros)
    elif opcao == "3":
        excluir(livros)
    elif opcao == "4":
        pesquisar(livros)
    elif opcao == "5":
        listar(livros)
    elif opcao == "0":
        print("Ate mais!")
        break
    else:
        print("Opcao invalida.")
