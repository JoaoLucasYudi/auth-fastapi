# FastAPI Authentication Project

## Descrição

Este projeto é uma API desenvolvida utilizando o FastAPI para criar uma aplicação robusta e eficiente, com autenticação JWT e integração com PostgreSQL. O objetivo principal é fornecer uma base sólida para o desenvolvimento de APIs seguras e escaláveis.

## Tecnologias Usadas

- **FastAPI**: Framework web moderno e de alto desempenho para construir APIs com Python 3.6+ baseado em padrões do OpenAPI e JSON Schema.
- **Docker**: Ferramenta para criar, implantar e executar aplicações em contêineres.
- **PostgreSQL**: Sistema gerenciador de banco de dados relacional.
- **DBeaver**: Ferramenta de gerenciamento de banco de dados.
- **Alembic**: Ferramenta de migração de banco de dados para SQLAlchemy.
- **SQLAlchemy**: ORM (Object Relational Mapper) para Python.
- **JWT (JSON Web Tokens)**: Padrão aberto para autenticação segura.
- **CryptContext**: Gerenciamento de hashes de senha.

## Funcionalidades

- **Autenticação JWT**: Implementação de autenticação e autorização utilizando JSON Web Tokens.
- **Gerenciamento de Senhas**: Armazenamento seguro de senhas utilizando hashing com CryptContext.
- **Migrations**: Controle de versões do banco de dados com Alembic.
- **Estrutura Modular**: Organização do código em módulos para facilitar a manutenção e a escalabilidade.

## Configuração e Execução

### Pré-requisitos

- Docker
- Docker Compose

### Passos para Execução

1. Clone o repositório:
    ```sh
    git clone https://github.com/JoaoLucasYudi/auth-fastapi.git
    cd auth-fastapi
    ```

2. Crie e inicie os contêineres Docker:
    ```sh
    docker-compose up --build
    ```

3. Acesse a API:
    A API estará disponível em [http://localhost:8000](http://localhost:8000).

### Documentação da API

A documentação interativa da API (Swagger UI) estará disponível em [http://localhost:8000/docs](http://localhost:8000/docs) e a documentação alternativa (ReDoc) em [http://localhost:8000/redoc](http://localhost:8000/redoc).
