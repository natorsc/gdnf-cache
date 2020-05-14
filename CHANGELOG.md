# v0.2.0 - 2020.05.14

## Projeto

- Realizada a reescrita dos scripts Python.
- Realizada a reorganização das pastas e arquivos.
- Criado arquivo `config.ini` para centralizar as configurações do aplicativo. 

## Python

- Scripts agora utilizam **decoradores** `@Gtk.Template()` no lugar do `Gtk.Builder()`.
- Cada janela possui um script Python próprio.
- Criado script `Application.py` para inicializar o aplicativo e controlar o seu comportamento.
- Arquivo `dnf_utilits.py` refatorado e realizada uma melhor separação dos métodos e funções.

## Interface

- Arquivos de interface estão utilizando a sintaxe `<template>` para construção das janelas e diálogos.
- Dialogo de informações do pacote exibe se o pacote está instalado ou não.
- Dialogo de informações do pacote agora exibe o campo `release`.
- Aplicativo mantem a ultima configuração de tema (claro ou escuro) que foi utilizado.
- Botão que abre a barra de pesquisa e botão de atualização agora ficam bloqueados até que a criação ou atualização do banco de dados esteja concluída.

## Banco de dados

- Criado campo `release` na tabela `available`.
- Criada tabela `installed` para armazena os programas que estão instalados.

# v0.1.0 - 2020.05.06

## Primeira versão do aplicativo

- Criados os recursos básicos que foram propostos na live.
- Primeira tentativa de empacotamento com PyInstaller e primeira tentativa de criar um **release** no Github.

Pacote `gdnf-cache-python37-fedora31-v0.1.0.tar.xz` criado com:

- Python 3.7.
- PyInstaller 3.6.

Aplicativo testado nos sistemas operacionais:

- Fedora 31 (sistema onde ele foi desenvolvido).
- Fedora 32 (Gnome Boxes).