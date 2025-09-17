---

```markdown
# 📝 Task Manager API - Flask CRUD Application

Este projeto é uma API RESTful desenvolvida com o framework Flask, que realiza operações de CRUD (Create, Read, Update, Delete) sobre uma estrutura de tarefas. Ideal para fins educacionais, testes com Postman e integração com frontends simples.

---

## 🚀 Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/) — Microframework para aplicações web em Python
- [Postman](https://www.postman.com/) — Testes e simulações de requisições HTTP
- [Pytest](https://docs.pytest.org/) — Framework de testes automatizados
- [Requests](https://docs.python-requests.org/) — Biblioteca para requisições HTTP
- Ambiente virtual (`venv`) para isolamento de dependências

---

## 📦 Estrutura do Projeto

```
├── app.py               # Arquivo principal da aplicação Flask
├── models/
│   └── task.py          # Classe Task com método to_dict()
├── teste.py             # Testes automatizados com Pytest
├── requirements.txt     # Dependências do projeto
└── venv/                # Ambiente virtual Python
```

---

## 📌 Funcionalidades da API

| Método | Endpoint             | Descrição                          |
|--------|----------------------|------------------------------------|
| POST   | `/tasks`             | Cria uma nova tarefa               |
| GET    | `/tasks`             | Lista todas as tarefas             |
| GET    | `/tasks/<id>`        | Retorna uma tarefa específica      |
| PUT    | `/tasks/<id>`        | Atualiza os dados de uma tarefa    |
| DELETE | `/tasks/<id>`        | Remove uma tarefa existente        |

---

## 🧪 Testes Automatizados

Os testes foram desenvolvidos com Pytest e simulam todas as operações da API:

- Criação de tarefa
- Listagem geral
- Consulta por ID
- Atualização de dados
- Exclusão de tarefa

Para rodar os testes:

```bash
pytest teste.py
```

---

## 🔧 Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/task-manager-api.git
   cd task-manager-api
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   python app.py
   ```

---

## 📬 Testando com Postman

Você pode importar os endpoints manualmente no Postman e testar cada rota com os seguintes exemplos de payload:

### 🔹 Criar Tarefa (POST `/tasks`)
```json
{
  "title": "Estudar Flask",
  "description": "Revisar conceitos de API REST"
}
```

### 🔹 Atualizar Tarefa (PUT `/tasks/1`)
```json
{
  "title": "Estudar Flask com Postman",
  "description": "Revisar e testar com Postman",
  "completed": true
}
```

---

## 💡 Observações

- Os dados são armazenados em memória (lista Python), portanto são voláteis.
- Ideal para aprendizado, testes locais e demonstrações técnicas.
- Pode ser facilmente adaptado para persistência com banco de dados (SQLite, PostgreSQL, etc).

---

## 📣 Conecte-se comigo

Se você gostou do projeto ou quer trocar ideias sobre desenvolvimento backend com Python, me chama no [LinkedIn](https://www.linkedin.com/in/seu-usuario/)!

---

```