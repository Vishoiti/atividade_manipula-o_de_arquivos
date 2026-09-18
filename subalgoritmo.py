def exibir_menu():
    print("""
        0 - SAIR
        1 - Nome do arquivo
        2 - Gravar o arquivo
        3 - Ler o arquivo
        4 - Editar o arquivo
        5 - Gravar arquivo exclusivo
        """)

def escolha_numero(c: dict) -> None:
    try:
        opcao = int(input("Escolha um número: "))
        return opcao
    except ValueError:
            print("Digite apenas números!")
    except NameError:
            print("Digite apenas números!")
    except:
        print("ERRO!")


def nome_arquivo(c: dict) -> None:
    nome= input("Nome Do arquivo: ")
    if nome == "":
        nome = "default"
    c["nome"] = nome +".txt"
    print("\nO nome Foi salvo com sucesso!")

def gravar_arquivo(c:dict) -> None:
    try:
        arquivo = open(c["nome"], "w", encoding="utf-8")
    except KeyError:
        print("Você precisa definir o nome do arquivo na opção 1!")
        return
    texto = input("Digite o conteúdo do arquivo: ")
    arquivo.write(texto + "\n")
    arquivo.close()
    print(f"\nO conteúdo: {texto} foi gravado com sucesso!")

def ler_arquivo(c:str) -> None:
    try:
        arquivo = open(c["nome"], "r", encoding="utf-8")
    except KeyError:
        print("O programa não possui arquivos registrados para ler.")
        return
    print("Conteúdo do arquivo: ")
    print('-' * 30)
    print(arquivo.read().strip())
    print('-' * 30)
    arquivo.close()

def editar_arquivo(c: dict) -> None:
    try:
        arquivo = open(c["nome"], "a", encoding="utf-8")
    except KeyError:
        print("Registre um arquivo antes!")
        return
    novo_conteudo = input("Conteúdo do arquivo: ")
    arquivo.write(f"{novo_conteudo}\n") 
    arquivo.close()
    print("\nArquivo editado!")
    return novo_conteudo