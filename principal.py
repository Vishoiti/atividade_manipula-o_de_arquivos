import os 
os.system("cls")

from subalgoritmo import exibir_menu, escolha_numero, nome_arquivo, arquivo_vazio

conteudo = {}

while True:
    exibir_menu()
    opcao = escolha_numero(conteudo)
    match opcao:
        case 0:
            print("Fim do programa!")
            break
        case 1:
            nome_arquivo(conteudo)
        