---
layout: post
title: Python SOLID
date: 2023-09-09
categories: Artigo
---

<p align="center">
<img src="{{ site.baseurl }}/images/2023-09-09-Python-metodos-especiais--dataclass.png" height="50%" width="50%" alt="Unform" />
</p>

# Implementando SOLID em Python com os Melhores Frameworks

O SOLID é um conjunto de princípios de design de software que, quando combinados, tornam o software mais compreensível, flexível e sustentável. Eles foram introduzidos por Robert C. Martin e são amplamente reconhecidos na comunidade de desenvolvimento de software. Neste artigo, vamos explorar como implementar esses princípios em Python usando alguns dos melhores frameworks disponíveis.

## 1. Princípio da Responsabilidade Única (SRP)

**Definição:** Uma classe deve ter apenas um motivo para mudar.

### Exemplo sem SRP:

```python
class User:
    def __init__(self, name: str):
        self.name = name

    def get_user_data(self):
        pass  # fetch user data from the database

    def save_user_data(self):
        pass  # save user data to the database
```

### Exemplo com SRP:

```python
class User:
    def __init__(self, name: str):
        self.name = name

class UserDataBase:
    @staticmethod
    def get_user_data(user: User):
        pass  # fetch user data

    @staticmethod
    def save_user_data(user: User):
        pass  # save user data
```

## 2. Princípio Aberto/Fechado (OCP)

**Definição:** Entidades de software (classes, módulos, funções, etc.) devem estar abertas para extensão, mas fechadas para modificação.

### Exemplo com FastAPI:

Usando a dependência de injeção do FastAPI, podemos facilmente estender a funcionalidade sem modificar o código existente.

```python
from fastapi import FastAPI, Depends

app = FastAPI()

def get_db():
    return "original db"

@app.get("/")
def read_root(db=Depends(get_db)):
    return {"db": db}
```

Para estender, podemos substituir a dependência:

```python
def get_new_db():
    return "new db"

app.dependency_overrides[get_db] = get_new_db
```

## 3. Princípio da Substituição de Liskov (LSP)

**Definição:** Objetos de uma superclasse devem ser capazes de ser substituídos por objetos de uma subclasse sem afetar a correção do programa.

### Exemplo com SQLAlchemy:

Usando a herança do SQLAlchemy, podemos garantir que as subclasses se comportem da mesma forma que as superclasses.

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Admin(User):
    __tablename__ = "admins"

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    admin_rights = Column(String)
```

## 4. Princípio da Segregação de Interface (ISP)

**Definição:** Nenhum cliente deve ser forçado a depender de interfaces que não usa.

### Exemplo com classes em Python:

Imagine que temos uma interface que define métodos para um CRUD completo:

```python
from abc import ABC, abstractmethod

class CRUDInterface(ABC):

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def update(self, id, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass
```

Agora, imagine que temos uma classe `UserReadOnly` que só precisa implementar operações de leitura. Se usarmos a interface `CRUDInterface`, seríamos forçados a implementar todos os métodos, mesmo que não os usemos.

Uma solução melhor seria segregarmos a interface:

```python
class ReadInterface(ABC):

    @abstractmethod
    def read(self, id):
        pass

class UserReadOnly(ReadInterface):

    def read(self, id):
        return f"Reading user with id {id}"
```

Agora, a classe `UserReadOnly` implementa apenas o que realmente precisa, seguindo o ISP.

## 5. Princípio da Inversão de Dependência (DIP)

**Definição:** Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.

### Exemplo com FastAPI e PyMySQL:

Ao usar o FastAPI com o PyMySQL, podemos criar uma abstração para o banco de dados, permitindo que o código de alto nível (rotas) não dependa diretamente do código de baixo nível (operações do banco de dados).

```python
from fastapi import FastAPI, Depends
import pymysql

app = FastAPI()

def get_db():
    connection = pymysql.connect(host='localhost', user='user', password='password', db='db')
    return connection

@app.get("/")
def read_root(db=Depends(get_db)):
    with db.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
    return {"db_version": version}
```

## Conclusão

O SOLID oferece uma base sólida para escrever software sustentável e de alta qualidade. Ao combinar esses princípios com frameworks modernos como FastAPI, SQLAlchemy e Pytest, os desenvolvedores Python podem criar aplicações robustas, extensíveis e de fácil manutenção.