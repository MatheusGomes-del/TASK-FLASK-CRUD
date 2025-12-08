📌 API de Gerenciamento de Tarefas (Flask)

Uma API simples para gerenciamento de tarefas (To-Do List), desenvolvida com Python e Flask, documentada com Swagger e testada com Pytest.
Este projeto tem como objetivo demonstrar boas práticas de desenvolvimento de APIs REST, organização de código, testes automatizados e documentação.

🚀 Funcionalidades

A API permite:

📄 Listar todas as tarefas

➕ Criar uma nova tarefa

🔍 Consultar uma tarefa específica

✏️ Atualizar uma tarefa existente

❌ Excluir uma tarefa

As tarefas são armazenadas temporariamente em memória, apenas para fins educacionais.

📂 Estrutura do Projeto
TASK-FLASK/
├── models/
│   └── task.py         # Modelo de dados Task
│
├── app.py              # App Flask e rotas da API
├── tests.py            # Testes automatizados com Pytest + Requests
├── requirements.txt    # Dependências do projeto
└── .gitignore

📘 Documentação da API (Swagger)

A API pode ser visualizada no Swagger Editor.

▶️ Como visualizar

Acesse: https://editor.swagger.io

Cole o conteúdo do arquivo abaixo:

openapi: 3.0.0
info:
  title: API de Gerenciamento de Tarefas
  description: Documentação da API para o gerenciamento de tarefas (To-Do List)
  version: 1.0.0

servers:
  - url: http://127.0.0.1:5000
    description: Servidor de Desenvolvimento

paths:
  /tasks:
    get:
      summary: Obter todas as tarefas
      responses:
        '200':
          description: Lista de tarefas obtida com sucesso
          content:
            application/json:
              schema:
                type: object
                properties:
                  tasks:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                        title:
                          type: string
                        description:
                          type: string
                        completed:
                          type: boolean
                  total_tasks:
                    type: integer

    post:
      summary: Criar nova tarefa
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                title:
                  type: string
                description:
                  type: string
              required:
                - title
      responses:
        '200':
          description: Nova tarefa criada com sucesso

  /tasks/{taskId}:
    get:
      summary: Buscar tarefa por ID
      parameters:
        - name: taskId
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Tarefa encontrada
        '404':
          description: Tarefa não encontrada

    put:
      summary: Atualizar tarefa existente
      parameters:
        - name: taskId
          in: path
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                title:
                  type: string
                description:
                  type: string
                completed:
                  type: boolean
              required:
                - title
      responses:
        '200':
          description: Tarefa atualizada com sucesso

    delete:
      summary: Deletar tarefa existente
      parameters:
        - name: taskId
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Tarefa deletada com sucesso


Você verá uma interface parecida com esta:

🛠️ Tecnologias Utilizadas

Python 3

Flask

Swagger (OpenAPI 3.0)

Pytest

Requests

JSON

▶️ Como executar o projeto

1. Instale as dependências:

pip install -r requirements.txt


2. Inicie o servidor:

python app.py


O servidor estará disponível em:

👉 http://127.0.0.1:5000

🧪 Rodando os testes

Execute:

pytest -v


Os testes cobrem:

Criação de tarefas

Listagem

Busca por ID

Atualização

Exclusão

🔍 Exemplo de JSON de uma tarefa
{
  "id": 1,
  "title": "Treinar boxe",
  "description": "Toda segunda-feira",
  "completed": false
}

🎯 Objetivo do Projeto

Este projeto faz parte do meu portfólio e demonstra:

✔️ Organização de código
✔️ Desenvolvimento de API REST
✔️ Testes automatizados
✔️ Documentação com Swagger
✔️ Boas práticas de versionamento
✔️ Código simples, limpo e didático

📄 Licença

Este projeto é livre para estudo e modificação.