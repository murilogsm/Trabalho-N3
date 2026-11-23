from livros import mostrar_livros


def pesquisar(livros):
    print("\n--- PESQUISAR LIVRO ---")
    print("1 - Titulo")
    print("2 - Autor")
    print("3 - Genero")
    opcao = input("Pesquisar por: ")

    if opcao == "1":
        campo = "titulo"
    elif opcao == "2":
        campo = "autor"
    elif opcao == "3":
        campo = "genero"
    else:
        print("Opcao invalida.")
        return

    texto = input("Digite o que procura: ").lower()
    resultado = []
    for livro in livros:
        if texto in livro[campo].lower():
            resultado.append(livro)

    mostrar_livros(resultado)
