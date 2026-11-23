# Biblioteca - Cadastro de Livros

Trabalho N3 de **Estrutura de Dados e Organização de Arquivos**.

**Aluno:** Murilo Gabriel Santos Marcovicz

## Sobre o projeto

É um programa em Python que roda no terminal e serve para cadastrar os livros de uma biblioteca.
Os livros ficam salvos no arquivo `livros.json`, então nada se perde quando o programa é fechado.

## Requisitos do trabalho

| Requisito | Como foi feito |
|-----------|----------------|
| Cadastro com incluir, alterar e excluir | Arquivo `livros.py`, opções 1, 2 e 3 do menu |
| Persistência em JSON | Arquivo `arquivo.py`, que lê e grava o `livros.json` |
| Pesquisa por campos de texto | Arquivo `busca.py`: pesquisa por título, autor ou gênero |
| Listas ordenadas por 2 campos | Arquivo `ordenacao.py`: ordena por título e por ano |

## Como rodar

Precisa ter o Python 3 instalado. Não precisa instalar nenhuma biblioteca.

```bash
python main.py
```

## Arquivos do projeto

| Arquivo | Para que serve |
|---------|----------------|
| `main.py` | Mostra o menu e chama as outras funções |
| `arquivo.py` | Lê e grava o arquivo JSON |
| `livros.py` | Incluir, alterar, excluir e mostrar livros |
| `busca.py` | Pesquisa de livros |
| `ordenacao.py` | Ordenação das listas |
| `livros.json` | Onde os livros ficam guardados |

## Como os dados são guardados

Cada livro é um **dicionário**, e todos os livros ficam juntos numa **lista**.
No arquivo `livros.json` isso fica assim:

```json
[
    {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "genero": "Romance",
        "ano": 1899
    }
]
```

| Campo | Tipo | O que é |
|-------|------|---------|
| id | número | Código do livro, criado sozinho pelo programa |
| titulo | texto | Nome do livro |
| autor | texto | Quem escreveu |
| genero | texto | Tipo do livro (romance, fantasia...) |
| ano | número | Ano em que foi lançado |

## Como funciona cada parte

### arquivo.py
- `ler_arquivo()`: abre o `livros.json` com `json.load()` e devolve a lista. Se o arquivo não existir, devolve uma lista vazia.
- `gravar_arquivo()`: salva a lista no arquivo com `json.dump()`. É chamada toda vez que um livro é incluído, alterado ou excluído.

### livros.py
- **Incluir**: pede título, autor, gênero e ano. O id é o maior id que já existe mais 1.
- **Alterar**: pede o id do livro e os novos dados. Se deixar o campo em branco, o valor antigo é mantido.
- **Excluir**: pede o id e confirma antes de apagar (`s` ou `n`).
- `procurar_id()`: percorre a lista com um `for` até achar o livro com aquele id.
- `ler_numero()`: só aceita números, para o programa não dar erro se digitar letras no ano ou no id.

### busca.py
O usuário escolhe se quer pesquisar por **título**, **autor** ou **gênero** e digita um texto.
O programa passa por todos os livros e mostra os que têm esse texto no campo escolhido.
Tudo é convertido para minúsculo com `.lower()`, então tanto faz digitar `ROMANCE` ou `romance`.

### ordenacao.py
A lista pode ser mostrada de duas formas:
- **por título**, em ordem alfabética;
- **por ano**, do mais antigo para o mais novo.

Para ordenar foi usado o **Bubble Sort** (ordenação por bolha): o programa compara cada livro com o próximo e troca os dois de lugar se estiverem fora de ordem. Isso se repete até a lista inteira ficar ordenada.

Exemplo ordenando pelo ano:

```
[1997, 1899, 1937]
compara 1997 e 1899 -> troca  -> [1899, 1997, 1937]
compara 1997 e 1937 -> troca  -> [1899, 1937, 1997]
lista ordenada!
```

A ordenação é feita numa cópia da lista (`livros.copy()`), então a ordem original do cadastro não muda.

## Exemplo de uso

```
====== BIBLIOTECA ======
1 - Incluir livro
2 - Alterar livro
3 - Excluir livro
4 - Pesquisar livro
5 - Listar livros
0 - Sair
Opcao: 4

--- PESQUISAR LIVRO ---
1 - Titulo
2 - Autor
3 - Genero
Pesquisar por: 3
Digite o que procura: romance
----------------------------------------
ID: 1
Titulo: Dom Casmurro
Autor: Machado de Assis
Genero: Romance
Ano: 1899
----------------------------------------
ID: 3
Titulo: Capitaes da Areia
Autor: Jorge Amado
Genero: Romance
Ano: 1937
----------------------------------------
```
