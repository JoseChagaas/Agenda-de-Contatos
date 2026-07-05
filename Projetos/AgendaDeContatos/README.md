# 📔 Agenda de Contatos

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Projeto prático desenvolvido durante o curso de Python da Rocketseat. Trata-se de uma aplicação de linha de comando (CLI) para gerenciamento completo de uma agenda de contatos, aplicando conceitos fundamentais de lógica de programação, estruturas de dados e tratamento de exceções em Python.

---

## 🚀 Funcionalidades

O sistema foi modularizado em funções para garantir a organização e independência do código, cobrindo os seguintes requisitos:

- [x] **Adicionar Contato:** Cadastro de contatos contendo nome, telefone, e-mail e status de favorito (inicializado como falso).
- [x] **Visualizar Contatos:** Listagem limpa e organizada dos contatos cadastrados, exibindo um indicador visual (`★`) para os favoritos.
- [x] **Editar Contato:** Alteração dos dados (nome, telefone ou e-mail) de um contato existente selecionado através do seu índice.
- [x] **Marcar/Desmarcar Favorito:** Gerenciamento do status de favorito de qualquer contato de forma simples.
- [x] **Visualizar Contatos Favoritos:** Filtragem dinâmica para exibir apenas os contatos marcados com a estrela.
- [x] **Apagar Contato:** Remoção de contatos da lista com feedback visual via terminal informando o nome do contato excluído.

---

## 🛠️ Conceitos Práticos Aplicados (Engenharia de Software)

Durante o desenvolvimento deste projeto, evoluí o código aplicando boas práticas de mercado:

* **Estruturas de Dados:** Uso combinado de `listas` para armazenamento e `dicionários` para modelagem dos objetos (chave-valor).
* **Passagem por Referência:** Compreensão de como o Python manipula endereços de memória ao alterar dicionários vinculados a uma lista sem a necessidade de reatribuição manual.
* **Validação de Dados:** Implementação de travas com `len()` para evitar erros de índice (`IndexError`) caso o usuário digite posições inexistentes.
* **Tratamento de Exceções (`Try / Except`):** Blindagem da aplicação contra dados inválidos. O uso de `try/except ValueError` garante que o programa não sofra *crash* caso o usuário digite letras onde o sistema espera números inteiros.
* **Alinhamento de UX (User Experience):** Sincronização entre a contagem humana (baseada em 1) e a contagem computacional (baseada em 0) usando a função `enumerate(start=1)` integrada a ajustes matemáticos de índices.

---

## ☕ Conecte-se Comigo

Este projeto foi um marco importante nos meus estudos de Python, onde pude transformar lógica pura em uma aplicação resiliente e bem estruturada. Se você gostou do projeto ou quer trocar uma ideia sobre desenvolvimento:

- 💬 Sinta-se à vontade para explorar o código e deixar seus insights!
- ⭐ Se este repositório te ajudou de alguma forma, deixe uma estrela!

**Desenvolvido com dedicação por José Chagas 🚀**      
