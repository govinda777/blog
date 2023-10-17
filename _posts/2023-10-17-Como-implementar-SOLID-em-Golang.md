---
layout: post
title: Como implementar SOLID em Golang
date: 2023-10-17
categories: Artigo
---

<p align="center">
<img src="{{ site.baseurl }}/images/2023-10-17-Como-implementar-SOLID-em-Golang.png" height="50%" width="50%" alt="Unform" />
</p>

# Implementando os Princípios SOLID em Go

Go, também conhecido como Golang, é uma linguagem de programação que, embora não seja orientada a objetos no sentido tradicional, ainda pode se beneficiar dos princípios SOLID. Estes são cinco princípios de design que visam tornar o software mais compreensível, flexível e sustentável. Neste artigo, exploraremos como aplicar cada um desses princípios em Go.

## 1. Princípio da Responsabilidade Única (SRP)

**Definição**: Uma classe deve ter apenas uma razão para mudar.

**Aplicação em Go**:
Em Go, em vez de classes, trabalhamos com pacotes e tipos. Cada pacote ou tipo deve ter uma única responsabilidade. Por exemplo, se temos um pacote para manipulação de arquivos, ele não deve estar envolvido na lógica de negócios ou na comunicação com a base de dados.

```go
// arquivo.go
package arquivo

func Ler(nome string) (string, error) {
    // lógica para ler um arquivo
}

func Escrever(nome string, conteudo string) error {
    // lógica para escrever em um arquivo
}
```

## 2. Princípio Aberto/Fechado (OCP)

**Definição**: Entidades de software (classes, módulos, funções, etc.) devem estar abertas para extensão, mas fechadas para modificação.

**Aplicação em Go**:
Em Go, podemos usar interfaces para garantir que nosso código esteja aberto para extensão. Isso permite que novas implementações sejam adicionadas sem modificar o código existente.

Vamos considerar um exemplo de um sistema de notificação:

```go
type Notificador interface {
    Enviar(mensagem string) error
}

type Email struct {
    Endereco string
}

func (e Email) Enviar(mensagem string) error {
    // Lógica para enviar email
    fmt.Printf("Enviando email para %s: %s\n", e.Endereco, mensagem)
    return nil
}

type SMS struct {
    Numero string
}

func (s SMS) Enviar(mensagem string) error {
    // Lógica para enviar SMS
    fmt.Printf("Enviando SMS para %s: %s\n", s.Numero, mensagem)
    return nil
}

func Notificar(n Notificador, mensagem string) {
    n.Enviar(mensagem)
}
```

Neste exemplo, temos uma interface `Notificador` que pode ser implementada por diferentes meios de notificação, como `Email` e `SMS`. A função `Notificar` aceita qualquer implementação de `Notificador` e pode enviar notificações sem se preocupar com os detalhes de como a notificação é realmente enviada.

## 3. Princípio da Substituição de Liskov (LSP)

**Definição**: Se `q(x)` é uma propriedade demonstrável dos objetos `x` de tipo `T`. Então `q(y)` deve ser verdadeiro para objetos `y` de tipo `S` onde `S` é um subtipo de `T`.

**Aplicação em Go**:
Em Go, isso significa que os tipos que implementam uma interface devem ser intercambiáveis sem alterar a correção do programa.

```go
type Retangulo struct {
    Largura, Altura float64
}

func (r Retangulo) Area() float64 {
    return r.Largura * r.Altura
}

type Quadrado struct {
    Lado float64
}

func (q Quadrado) Area() float64 {
    return q.Lado * q.Lado
}

func CalculaArea(r Retangulo) float64 {
    return r.Area()
}
```

Aqui, `Quadrado` e `Retangulo` podem ser usados intercambiavelmente, desde que ambos tenham o método `Area`.

## 4. Princípio da Segregação de Interface (ISP)

**Definição**: Nenhum cliente deve ser forçado a depender de interfaces que não usa.

**Aplicação em Go**:
Em Go, é comum ter interfaces pequenas, muitas vezes com apenas um método. Isso torna mais fácil implementar e combinar interfaces conforme necessário.

```go
type Leitor interface {
    Ler() string
}

type Escritor interface {
    Escrever(string)
}

type LeitorEscritor interface {
    Leitor
    Escritor
}
```

## 5. Princípio da Inversão de Dependência (DIP)

**Definição**: Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.

**Aplicação em Go**:
Em Go, isso é frequentemente alcançado através da injeção de dependências. Em vez de depender de implementações concretas, dependemos de interfaces.

```go
type BancoDeDados interface {
    Salvar(dado string) error
}

type Servico struct {
    db BancoDeDados
}

func NovoServico(db BancoDeDados) *Servico {
    return &Servico{db: db}
}
```

Aqui, `Servico` não depende de uma implementação concreta de um banco de dados, mas sim de uma abstração.

## Conclusão

Enquanto Go tem sua própria abordagem para design e organização de código, os princípios SOLID ainda são relevantes e podem ajudar a criar software robusto e sustentável em Go. Ao seguir esses princípios, os desenvolvedores podem garantir que seu código seja flexível, sustentável e fácil de manter.