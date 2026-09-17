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


def arquivo_vazio(c: dict) -> None:
    vazio = "default"
    arquivo = open(vazio + ".txt", "w", encoding="utf-8")
    arquivo.write(vazio + "\n")
    arquivo.close()
    print("\nArquivo gravado com sucesso!")

def nome_arquivo(c: dict) -> None:
    nome= input("Nome Do arquivo: ")
    if nome == "":
        arquivo_vazio(c)
    else:
        arquivo = open(nome + ".txt", "w", encoding="utf-8")
        arquivo.write(nome + "\n")
        arquivo.close()
        print("\nArquivo gravado com sucesso!")