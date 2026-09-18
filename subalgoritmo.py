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
    if "nome" not in c:
        print("Coloque o nome do arquivo na opção 1!")
        return
    texto = input("Digite o conteúdo do arquivo: ")
    arquivo = open(c["nome"], "w", encoding="utf-8")
    arquivo.write(texto + "\n")
    arquivo.close()
    print(f"\nO conteúdo: {texto} foi gravado com sucesso!")
