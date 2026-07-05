#Lista para armazernar os contatos
contatos = [] 

def adicionar_contato(lista): #O parametro lista é uma "variável" temporária que será substituída pela variável contatos quando a função for chamada.
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato:")
    favorito = False

#Organizando os dados em um dicionário
    novo_contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }

    lista.append(novo_contato)
    print(f"\nContato {nome} foi adicionado com sucesso!")

def ver_contatos(lista):
    for indice, contato in enumerate(lista, start=1):
        if contato["favorito"] == True:
            estrela = "★"
        else:
            estrela = ""
        print(f"[{indice}]. [{estrela}] Nome: {contato['nome']} - Telefone: {contato['telefone']} - Email: {contato['email']}")

def editar_contatos(lista): 
    ver_contatos(lista) 

    try:
        #Pede para o usuário digitar o número do contato, que na verdade é o índice do contato dentro da lista
        numero_digitado = int(input("Digite o número do contato que deseja editar: "))
    except ValueError:
        print("\nNúmero do contato inválido.")
        return
    
    #IF para verificar se o número digitado pelo usuário é válido, ou seja, se ele está dentro do intervalo de contatos existentes na lista.
    if numero_digitado > 0 and numero_digitado <= len(lista):
        indice = numero_digitado - 1 #Subtraio 1 do índice digitado pelo usuário, pois a lista começa no índice 0.     
        contato_editado = lista[indice]  #Aqui eu atribuo o contato que está na posição do índice digitado pelo usuário para a variável contato_editado, que será usada para editar os dados do contato.
    else:
        print("\nNúmero do contato inválido.")
        return

    contato_editado["nome"] = input("Digite o novo nome do contato: ")
    contato_editado["telefone"] = input("Digite o novo telefone do contato: ")
    contato_editado["email"] = input("Digite o novo email do contato: ")
    print("\nContato atualizado com sucesso!")

def marcar_favorito(lista):
    ver_contatos(lista)

    try:
        numero_digitado = int(input("Digite o número do contato que deseja marcar como favorito: "))
    except ValueError:
        print("\nNúmero do contato inválido.")
        return

    #IF para verificar se o número digitado pelo usuário é válido, ou seja, se ele está dentro do intervalo de contatos existentes na lista.
    if numero_digitado > 0  and numero_digitado <= len(lista):
        indice = numero_digitado - 1
        contato_favorito = lista[indice]
    else:
        print("\nNúmero do contato inválido.")
        return

    if contato_favorito["favorito"] == False:
        contato_favorito["favorito"] = True
        print("\nContato favoritado com sucesso!")
    else:
        print("\nContato já está marcado como favorito.")

def desmarcar_favorito(lista):
    ver_contatos(lista)

    try:
        numero_digitado = int(input("Digite o número do contato que deseja desmarcar como favorito: "))
    except ValueError:
        print("\nNúmero do contato inválido.")
        return

    #IF para verificar se o número digitado pelo usuário é válido, ou seja, se ele está dentro do intervalo de contatos existentes na lista.
    if numero_digitado > 0 and numero_digitado <= len(lista):
        indice = numero_digitado - 1
        contato_desmarcado = lista[indice]
    else:
        print("\nNúmero do contato inválido.")
        return


    if contato_desmarcado["favorito"] == True:
        contato_desmarcado["favorito"] = False
        print("\nContato desmarcado como favorito com sucesso!")
    else:
        print("\nContato não está marcado como favorito.")

def ver_contatos_favoritos(lista):
    for indice, contato in enumerate(lista, start=1):
        if contato["favorito"] == True:
            estrela = "★"
            print(f"[{indice}]. [{estrela}] Nome: {contato['nome']} - Telefone: {contato['telefone']} - Email: {contato['email']}")

def apagar_contato(lista):
    ver_contatos(lista)

    try:
        numero_digitado = int(input("Digite o número do contato que deseja remover: "))
    except ValueError:
        print("\nNúmero do contato inválido.")
        return

    #IF para verificar se o número digitado pelo usuário é válido, ou seja, se ele está dentro do intervalo de contatos existentes na lista.
    if numero_digitado > 0 and numero_digitado <= len(lista):
        indice = numero_digitado - 1
        contato_removido = lista[indice]
    else:
        print("\nNúmero do contato inválido.")
        return

    # O método pop() remove o elemente da lista e guarda temporariamente em uma variável, que nesse caso é a variável contato_removido, que será usada para informar o usuário qual contato foi removido.
    contato_removido = lista.pop(indice) 
    print(f"\nContato {contato_removido['nome']} removido com sucesso!")

while True:
    print("\nAgenda de Contatos")
    print("1. Adicionar Contato")
    print("2. Editar Contato")
    print("3. Ver Contatos")
    print("4. Marcar Contato Favorito")
    print("5. Desmarcar Contato Favorito")
    print("6. Ver Contatos Favoritos")
    print("7. Apagar Contato")
    print("8. Sair")

    escolha = input("Digite a opção desejada: ")
    
    if escolha == "1":
        adicionar_contato(contatos)

    elif escolha == "2":
        editar_contatos(contatos)

    elif escolha == "3":
        print("\nLista de Contatos\n")
        ver_contatos(contatos)
    
    elif escolha == "4":
        print("\nMarcar Contato Favorito\n")
        marcar_favorito(contatos)

    elif escolha == "5":
        print("\nDesmarcar Contato Favorito\n")
        desmarcar_favorito(contatos)

    elif escolha == "6":
        print("\nLista de Contatos Favoritos\n")
        ver_contatos_favoritos(contatos)
    
    elif escolha == "7":
        print("\nApagar Contato\n")
        apagar_contato(contatos)

    elif escolha == "8":
        print("Aplicativo finalizado")
        break

