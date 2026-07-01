def salvar_contato(agenda, nome, telefone):
    contato = {"nome": nome, "telefone": telefone}
    agenda.append(contato)
    print(f"O contato {nome} foi salvo com sucesso!")
    return

def ver_contatos(agenda):
    print("\nLista de Contatos")
    for indice, contato in enumerate(agenda, start= 1):
        print(f"Contato {indice} -> Nome: {contato["nome"]} - Telefone: {contato["telefone"]}")
    return agenda

agenda = []

while True:
    print("\nAgenda de Contatos")
    print("1. Salvar Contato")
    print("2. Editar Contato")
    print("3. Deletar Contato")
    print("4. Favoritar Contato")
    print("5. Ver Contatos")
    print("6. Sair")

    menu = input("Escolha uma opção:")

    if menu == "1":
        nome = input("Digite o nome do contato:")
        telefone = input("Digite o telefone do contato:")
        salvar_contato(agenda, nome, telefone)

    elif menu == "5":
        ver_contatos(agenda)
  


