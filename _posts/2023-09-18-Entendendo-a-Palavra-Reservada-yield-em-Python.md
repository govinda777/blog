---
layout: post
title: Entendendo a Palavra Reservada yield em Python
date: 2023-09-18
categories: Artigo
---

<p align="center">
<img src="{{ site.baseurl }}/images/2023-09-18-Entendendo-a-Palavra-Reservada-yield-em-Python.png" height="50%" width="50%" alt="Unform" />
</p>

**Entendendo a Palavra Reservada `yield` em Python**

---

**Introdução**

Em Python, a palavra-chave `yield` é uma ferramenta poderosa que transforma uma função comum em um gerador. Mas o que isso significa? E por que você usaria um gerador em vez de uma função regular? Neste artigo, mergulharemos profundamente no mundo dos geradores e na magia por trás do `yield`.

---

**O Básico: Funções vs. Geradores**

Antes de nos aprofundarmos no `yield`, é crucial entender a diferença entre funções regulares e geradores.

- **Funções Regulares**: Quando chamadas, executam e retornam um valor usando a palavra-chave `return`. Uma vez que a função retorna um valor, seu estado é perdido.

- **Geradores**: São funções que permitem a geração de uma série de valores ao longo do tempo. Em vez de retornar um valor e sair, os geradores pausam a execução da função, permitindo retomá-la posteriormente. Isso é feito usando a palavra-chave `yield`.

---

**A Magia do `yield`**

O `yield` pausa a função e "retorna" um valor, mas mantém o estado da função intacto. Isso significa que, quando o gerador é chamado novamente, a execução é retomada logo após a última instrução `yield`.

Vamos ver um exemplo simples:

```python
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))  # Saída: 1
print(next(gen))  # Saída: 2
print(next(gen))  # Saída: 3
```

Aqui, cada chamada de `next(gen)` retoma a execução do gerador logo após o último `yield`, produzindo os números 1, 2 e 3 sequencialmente.

---

**Por que usar `yield`?**

1. **Eficiência de Memória**: Geradores são iteráveis "preguiçosos". Eles produzem valores um de cada vez e não mantêm todos os valores na memória. Isso é útil ao trabalhar com grandes conjuntos de dados.

2. **Produção e Consumo Simultâneos**: Como os geradores produzem valores sob demanda, você pode produzir e consumir itens simultaneamente sem esperar que toda a sequência seja gerada.

3. **Simplicidade**: Em muitos casos, escrever um gerador é mais conciso e legível do que a alternativa usando classes ou loops tradicionais.

---

**Exemplo Prático: Sequência de Fibonacci**

Vamos criar um gerador que produz a sequência de Fibonacci:

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)
```

**Saída:**

```
0
1
1
2
3
```

Neste exemplo, a sequência de Fibonacci é gerada um número de cada vez, sem a necessidade de armazenar toda a sequência na memória.

---

**Conclusão**

A palavra-chave `yield` em Python é uma ferramenta poderosa que permite criar geradores, uma espécie especial de iterável. Os geradores são eficientes em termos de memória, permitem a produção e o consumo simultâneos de itens e podem simplificar significativamente o código em muitos casos. Ao compreender e adotar o `yield` em seu arsenal de programação, você pode escrever código Python mais eficiente e elegante.