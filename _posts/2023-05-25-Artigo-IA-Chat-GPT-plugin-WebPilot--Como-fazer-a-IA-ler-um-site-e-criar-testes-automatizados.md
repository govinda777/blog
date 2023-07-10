---
layout: post
date: 2023-05-25
categories: [IA, Testes automatizados]
---

<p align="center">
<img src="{{ site.baseurl }}/images/19--[Artigo]--Como_ganhar_dinheiro_com_IA.png" height="50%" width="50%" alt="Unform" />
</p>

# [-IA-][- ChatGPT-] plugin WebPilot

> ### Tutorial: Como fazer o plugin WebPilot 
    - 1 - ler Casos de testes em Gherkin 
    - 2 - ler uma página Html
    - 3 - criar um script Cypress correspondente a cada Caso de teste

Neste tutorial, vamos explorar como usar o plugin WebPilot do ChatGPT para ler casos de teste escritos na linguagem Gherkin e gerar um script de teste Cypress correspondente. Vamos usar um caso de teste simples que valida se todos os links em uma página da web levam a uma página com o código de resposta HTTP 200.

## Passo 1: Leitura de Casos de Teste em Gherkin

Primeiro, vamos fornecer ao ChatGPT o caso de teste em Gherkin. Gherkin é uma linguagem de domínio específico (DSL) que é usada para escrever casos de teste de forma clara e compreensível. Aqui está o nosso caso de teste:

```gherkin
# language: pt

Funcionalidade: Acesso a página https://www.productmanagementexercises.com/blog/getting-into-web3-product-managers/

Cenário: Validar se todos os links está indo para uma página com o resultado http code 200
Quando clico em qualquer link da página
Então o resultado da requisição será http code 200
```

## Passo 2: Leitura da Página da Web

Em seguida, vamos usar o plugin WebPilot para visitar a página da web que queremos testar. Aqui está o comando que usamos para isso:

```
web_pilot.visitWebPage({ link: "https://www.productmanagementexercises.com/blog/getting-into-web3-product-managers/", user_has_request: false })
```

## Passo 3: Criação do Script de Teste Cypress

Finalmente, vamos usar o ChatGPT para gerar um script de teste Cypress que implementa o nosso caso de teste. Aqui está o script de teste Cypress:

```
describe('Product Management Exercises Blog Page', () => {
  beforeEach(() => {
    cy.visit('https://www.productmanagementexercises.com/blog/getting-into-web3-product-managers/')
  })

  it('Validar se todos os links está indo para uma página com o resultado http code 200', () => {
    cy.get('a').each(($a) => {
      const href = $a.prop('href')

      cy.request(href).its('status').should('eq', 200)
    })
  })
})
```

Este script de teste visita a página da web, encontra todos os links na página e verifica se cada link leva a uma página com o código de resposta HTTP 200.

Esperamos que este tutorial tenha sido útil para mostrar como você pode usar o plugin WebPilot do ChatGPT para ler casos de teste em Gherkin e gerar scripts de teste Cypress correspondentes. Lembre-se de que este é apenas um exemplo simples e que o WebPilot é uma ferramenta poderosa que pode ser usada de muitas outras maneiras para ajudar a automatizar e melhorar seus processos de teste.

## Exemplo de comando para o ChartGPT (copie e cole o comando no ChatGPT com o plugin WebPilot instalado)

Caso de teste : 

```gherkin

# language: pt

Funcionalidade: Acesso a página https://www.productmanagementexercises.com/blog/getting-into-web3-product-managers/

Cenário: Validar se todos os links está indo para uma página com o resultado http code 200
Quando clico em Blog
Então o resultado da requisição será http code 200

```

Página : web_pilot.visitWebPage({ link: "https://www.productmanagementexercises.com/blog/getting-into-web3-product-managers/", user_has_request: false }) 

Crie um script de testes em cypress implementando o Caso de teste para a Página informada.

## Resultado

```cypress

describe('Acesso a página', () => {
  beforeEach(() => {
    cy.visit('https://www.productmanagementexercises.com/blog/getting-into-web3-product-managers/')
  })

  it('Validar se todos os links está indo para uma página com o resultado http code 200', () => {
    cy.get('a').each(($a) => {
      const href = $a.prop('href')

      // Ignorando links sem href ou que começam com "#"
      if (href && !href.startsWith('#')) {
        cy.request(href).its('status').should('eq', 200)
      }
    })
  })
})
```

