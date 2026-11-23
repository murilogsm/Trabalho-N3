from livros import mostrar_livros


def ordenar(livros, campo):
    lista = livros.copy()
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(tamanho - 1 - i):
            a = lista[j][campo]
            b = lista[j + 1][campo]
            if campo == "titulo":
                a = a.lower()
                b = b.lower()
            if a > b:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def listar(livros):
    print("\n--- LISTAR LIVROS ---")
    print("1 - Ordenar por titulo")
    print("2 - Ordenar por ano")
    opcao = input("Escolha: ")

    if opcao == "1":
        mostrar_livros(ordenar(livros, "titulo"))
    elif opcao == "2":
        mostrar_livros(ordenar(livros, "ano"))
    else:
        print("Opcao invalida.")
