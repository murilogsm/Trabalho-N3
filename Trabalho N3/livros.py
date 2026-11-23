from arquivo import gravar_arquivo


def ler_numero(mensagem):
    valor = input(mensagem)
    while not valor.isdigit():
        print("Digite apenas numeros.")
        valor = input(mensagem)
    return int(valor)


def mostrar_livros(livros):
    if len(livros) == 0:
        print("Nenhum livro encontrado.")
        return
    print("-" * 40)
    for livro in livros:
        print("ID:", livro["id"])
        print("Titulo:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Genero:", livro["genero"])
        print("Ano:", livro["ano"])
        print("-" * 40)


def procurar_id(livros, codigo):
    for livro in livros:
        if livro["id"] == codigo:
            return livro
    return None


def incluir(livros):
    print("\n--- INCLUIR LIVRO ---")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    genero = input("Genero: ")
    ano = ler_numero("Ano: ")

    novo_id = 1
    for livro in livros:
        if livro["id"] >= novo_id:
            novo_id = livro["id"] + 1

    livros.append({
        "id": novo_id,
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "ano": ano
    })
    gravar_arquivo(livros)
    print("Livro cadastrado com sucesso!")


def alterar(livros):
    print("\n--- ALTERAR LIVRO ---")
    codigo = ler_numero("ID do livro: ")
    livro = procurar_id(livros, codigo)
    if livro is None:
        print("Livro nao encontrado.")
        return

    print("Deixe em branco para manter o valor atual.")
    titulo = input("Titulo (" + livro["titulo"] + "): ")
    autor = input("Autor (" + livro["autor"] + "): ")
    genero = input("Genero (" + livro["genero"] + "): ")
    ano = input("Ano (" + str(livro["ano"]) + "): ")

    if titulo != "":
        livro["titulo"] = titulo
    if autor != "":
        livro["autor"] = autor
    if genero != "":
        livro["genero"] = genero
    if ano.isdigit():
        livro["ano"] = int(ano)

    gravar_arquivo(livros)
    print("Livro alterado com sucesso!")


def excluir(livros):
    print("\n--- EXCLUIR LIVRO ---")
    codigo = ler_numero("ID do livro: ")
    livro = procurar_id(livros, codigo)
    if livro is None:
        print("Livro nao encontrado.")
        return

    resposta = input("Excluir o livro " + livro["titulo"] + "? (s/n): ")
    if resposta == "s":
        livros.remove(livro)
        gravar_arquivo(livros)
        print("Livro excluido com sucesso!")
    else:
        print("Exclusao cancelada.")
