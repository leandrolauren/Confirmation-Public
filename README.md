# Birthday Party Confirmation API

Este projeto é uma aplicação FastAPI que gerencia confirmações de presença para uma festa de aniversário, construída com Python 3.x e utilizando o servidor ASGI uvicorn. O projeto inclui um frontend em React para interação com os usuários.

## Estrutura do Projeto

## Tecnologias Utilizadas

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI%20Server-green.svg)](https://www.uvicorn.org/en/latest/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Web%20Framework-blue.svg)](https://fastapi.tiangolo.com/)
[![Language](https://img.shields.io/badge/Language-JavaScript-brightgreen.svg)](https://www.javascript.com/)
[![Framework](https://img.shields.io/badge/Framework-React-blue.svg)](https://reactjs.org/)

## Funcionalidades

| Funcionalidade | Descrição |
| --- | --- |
| **Roteador de Confirmação** | Gerencia solicitações de confirmação de presença para a festa de aniversário |
| **Atualizações em Tempo Real** | Utiliza WebSockets para atualizações em tempo real |

## Endpoints

### Roteador de Confirmação

- **POST /api/confirm**: Endpoint para enviar uma confirmação de presença.
    - Corpo da Solicitação: JSON contendo `name`, `email`, `phone`, `confirmation`, `qtt_adult` e `qtt_child`.
    - Resposta: JSON com detalhes da confirmação.

- **GET /api/confirmations**: Endpoint para recuperar todas as confirmações.
    - Resposta: Array JSON de todos os registros de confirmação.

## Variáveis de Ambiente

- **O arquivo `.env` no diretório `backend` deve conter as seguintes variáveis de ambiente para configurar a conexão com o banco de dados PostgreSQL:**
    - **DB_NAME**="nome_do_banco". 
    - **DB_USER**="usuario_do_banco".
    - **DB_PASSWORD**="senha_do_banco". 
    - **DB_HOST**="host_do_banco".
    - **DB_PORT**="porta_do_banco".

- **Também deve conter o Token fixo** para validação no endpoint /confirmations.
    - **API_TOKEN**="token_da_api"

## Banco de Dados

- **Este projeto requer um banco de dados PostgreSQL.** Certifique-se de ter um banco de dados PostgreSQL configurado e rodando. As variáveis de ambiente no arquivo `.env` devem ser configuradas corretamente para que a aplicação possa se conectar ao banco de dados.

## Instruções

### Backend

1. Clone o repositório para sua máquina local usando `git clone`
2. Navegue até o diretório backend: `cd backend`
3. Instale as dependências executando `pip install -r requirements.txt`
4. Execute a aplicação usando `uvicorn main:app --host 127.0.0.1 --port 8000`

### Frontend

1. Navegue até o diretório frontend: `cd frontend`
2. Instale as dependências executando `npm install`
3. Inicie o servidor de desenvolvimento usando `npm start`
4. Abra seu navegador e navegue até `http://localhost:3000` para visualizar a aplicação

### Docker

Você também pode usar Docker para rodar a aplicação. Certifique-se de ter o Docker e o Docker Compose instalados.

1. Navegue até o diretório raiz do projeto
2. Execute `docker-compose up --build`
3. A aplicação backend estará disponível em `http://localhost:8000` e o frontend em `http://localhost:3000`

## Contribuição

Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request com suas alterações.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
