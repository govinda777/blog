---
layout: post
title: 2024-10-31-Ferramentas-para-Executar-Código-Diretamente-a-partir-do-README-no-GitHub
date: 2024-10-31
categories: Artigo
---

<p align="center">
<img src="{{ site.baseurl }}/images/2024-10-31-Ferramentas-para-Executar-Código-Diretamente-a-partir-do-README-no-GitHub.webp" 
height="50%" width="50%" alt="Unform" />
</p>  

# Ferramentas para Executar Código Diretamente a partir do README no GitHub

## Introdução

Embora o GitHub não permita a execução direta de código a partir de um arquivo `README.md`, existem ferramentas que facilitam a execução de aplicações ou scripts a partir de links ou botões inseridos no README. A seguir, apresentamos algumas dessas ferramentas e como utilizá-las para executar um simples "Olá, mundo!".

## 1. **GitHub Actions**

**Descrição:**
O GitHub Actions permite automatizar fluxos de trabalho diretamente no GitHub, incluindo a execução de scripts em resposta a eventos específicos.

**Como Utilizar:**

1. **Criar um Workflow:**
   - No seu repositório, crie o diretório `.github/workflows/`.
   - Dentro desse diretório, crie um arquivo YAML, por exemplo, `hello-world.yml`.

2. **Configurar o Workflow:**
   - Adicione o seguinte conteúdo ao arquivo `hello-world.yml`:
     ```yaml
     name: Olá Mundo

     on: [workflow_dispatch]

     jobs:
       hello_world_job:
         runs-on: ubuntu-latest
         steps:
           - name: Executando Olá Mundo
             run: echo "Olá, mundo!"
     ```

3. **Adicionar um Botão no README:**
   - No seu `README.md`, adicione um link para acionar manualmente o workflow:
     ```markdown
     [![Executar Olá Mundo](https://img.shields.io/badge/Executar%20Olá%20Mundo-blue)](../../actions/workflows/hello-world.yml)
     ```

**Observações:**
- O botão direciona o usuário à página do workflow, onde ele pode acioná-lo manualmente.
- Para mais detalhes, consulte a [Documentação do GitHub Actions](https://docs.github.com/pt/actions).

## 2. **Gitpod**

**Descrição:**
O Gitpod oferece ambientes de desenvolvimento prontos na nuvem, configurados a partir do seu repositório.

**Como Utilizar:**

1. **Preparar o Repositório:**
   - Crie um arquivo `.gitpod.yml` na raiz do seu repositório com o seguinte conteúdo:
     ```yaml
     tasks:
       - init: echo "Olá, mundo!"
     ```

2. **Adicionar um Botão no README:**
   - No seu `README.md`, adicione o botão para abrir o repositório no Gitpod:
     ```markdown
     [![Abrir no Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/SEU_USUARIO/SEU_REPOSITORIO)
     ```

**Observações:**
- Substitua `SEU_USUARIO` e `SEU_REPOSITORIO` pelo seu nome de usuário e nome do repositório no GitHub.
- Ao clicar no botão, o Gitpod abrirá um ambiente de desenvolvimento e executará o comando especificado.
- Para mais informações, visite o [site oficial do Gitpod](https://www.gitpod.io/).

## 3. **Repl.it**

**Descrição:**
O Repl.it é um ambiente de desenvolvimento online que permite executar código diretamente no navegador.

**Como Utilizar:**

1. **Criar um Repl:**
   - Acesse o [Repl.it](https://repl.it/) e crie um novo Repl com a linguagem de sua escolha.
   - Adicione o seguinte código para exibir "Olá, mundo!":
     ```python
     print("Olá, mundo!")
     ```

2. **Adicionar um Botão no README:**
   - No seu `README.md`, adicione o botão para executar o código no Repl.it:
     ```markdown
     [![Executar no Repl.it](https://repl.it/badge/github/SEU_USUARIO/SEU_REPOSITORIO)](https://repl.it/github/SEU_USUARIO/SEU_REPOSITORIO)
     ```

**Observações:**
- Substitua `SEU_USUARIO` e `SEU_REPOSITORIO` pelo seu nome de usuário e nome do repositório no GitHub.
- Ao clicar no botão, o Repl.it abrirá o ambiente com o código pronto para execução.
- Para mais detalhes, acesse o [Repl.it](https://repl.it/).

## 4. **Heroku**

**Descrição:**
O Heroku é uma plataforma de hospedagem que permite implantar aplicativos web.

**Como Utilizar:**

1. **Preparar o Repositório:**
   - Adicione um arquivo `Procfile` na raiz do seu repositório com o seguinte conteúdo:
     ```
     web: echo "Olá, mundo!"
     ```

2. **Adicionar um Botão no README:**
   - No seu `README.md`, adicione o botão para implantar no Heroku:
     ```markdown
     [![Deploy no Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/SEU_USUARIO/SEU_REPOSITORIO)
     ```

**Observações:**
- Substitua `SEU_USUARIO` e `SEU_REPOSITORIO` pelo seu nome de usuário e nome do repositório no GitHub.
- Ao clicar no botão, o Heroku iniciará o processo de implantação do aplicativo.
- Para mais informações, visite o [Heroku](https://www.heroku.com/).

## 5. **GitHub Codespaces**

**Descrição:**
O GitHub Codespaces oferece ambientes de desenvolvimento baseados em contêineres diretamente no GitHub.

**Como Utilizar:**

1. **Configurar o Repositório:**
   - Crie um arquivo `.devcontainer/devcontainer.json` com a configuração desejada.

2. **Adicionar um Botão no README:**
   - No seu `README.md`, adicione o botão para abrir no Codespaces:
     ```markdown
     [![Abrir no Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&
::contentReference[oaicite:0]{index=0}
 
