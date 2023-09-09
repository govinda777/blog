---
layout: post
title: Python, métodos especiais dataclass
date: 2023-09-09
categories: Artigo
---

<p align="center">
<img src="{{ site.baseurl }}/images/2023-09-09-Python-metodos-especiais--dataclass.png" height="50%" width="50%" alt="Unform" />
</p>

Uma das principais vantagens do módulo `dataclasses` é que ele gera automaticamente métodos especiais para você, incluindo o construtor (`__init__`), representação (`__repr__`), e comparação (`__eq__`), entre outros, com base nas anotações de tipo que você fornece para os campos da classe.

Por exemplo, com a classe `User` que definimos anteriormente:

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    email: str
    password: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
```

Você pode criar uma instância de `User` sem precisar definir explicitamente um construtor:

```python
user = User(id=1, first_name="John", last_name="Doe", email="john.doe@example.com", password="secret")
print(user)
```

O método `__repr__` também é gerado automaticamente, então o `print(user)` mostrará uma representação legível da instância.

Se você precisar de um comportamento personalizado no construtor ou em outros métodos, ainda poderá definir esses métodos manualmente, e eles não serão sobrescritos pelo comportamento gerado automaticamente pelo `dataclasses`.

Vamos começar com uma classe básica sem o uso de `dataclasses` para entender o que cada um desses métodos faz:

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"Person(first_name='{self.first_name}', last_name='{self.last_name}', age={self.age})"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.first_name == other.first_name and self.last_name == other.last_name and self.age == other.age
        return False
```

1. **Construtor (`__init__`)**:
   Este é o método que é chamado quando você cria uma nova instância da classe. Ele inicializa os atributos da instância com os valores fornecidos.

   ```python
   person1 = Person("John", "Doe", 30)
   ```

2. **Representação (`__repr__`)**:
   Este método retorna uma representação "oficial" da instância, que, se possível, deve se parecer com um código Python válido que poderia ser usado para recriar um objeto com o mesmo valor. É chamado quando você tenta imprimir a instância ou quando usa a função `repr()`.

   ```python
   print(person1)  # Person(first_name='John', last_name='Doe', age=30)
   ```

3. **Comparação (`__eq__`)**:
   Este método permite comparar duas instâncias da classe para igualdade. Retorna `True` se forem consideradas iguais e `False` caso contrário.

   ```python
   person2 = Person("John", "Doe", 30)
   person3 = Person("Jane", "Doe", 25)

   print(person1 == person2)  # True
   print(person1 == person3)  # False
   ```

Agora, usando `dataclasses`, podemos simplificar a classe `Person`:

```python
from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
```

Com esta versão simplificada:

- O método `__init__` é gerado automaticamente, permitindo que você crie instâncias da mesma forma que antes.
- O método `__repr__` também é gerado automaticamente, fornecendo uma representação similar à anterior.
- O método `__eq__` é gerado automaticamente, permitindo comparações de igualdade entre instâncias.

O uso de `dataclasses` torna o código mais limpo e menos propenso a erros, especialmente para classes que servem principalmente como contêineres de dados.
