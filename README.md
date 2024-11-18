# API de Eventos

Este projeto implementa uma API para gerenciar eventos e participantes utilizando o Django Rest
Framework.

## **Funcionalidades**

1. **Gerenciar Eventos**:

- Criar, listar, atualizar e excluir eventos.
- Cada evento possui os atributos:
- Nome (`nome`)
- Data (`data`)
- Local (`local`)

2. **Gerenciar Participantes**:

- Criar, listar e excluir participantes associados a eventos.
- Cada participante possui os atributos:
- Nome (`nome`)
- Email (`email`)
- Evento (`evento`) (associação com o evento).

3. **Permissões de Acesso**:

- Apenas usuários autenticados podem criar ou excluir eventos.
- Todos os usuários podem listar os eventos e participantes.

---

## **Tecnologias Utilizadas**

- **Python**: Linguagem principal.
- **Django**: Framework para desenvolvimento web.
- **Django Rest Framework**: Para construção de APIs RESTful.

---

## **Como rodar o projeto**

### **1. Pré-requisitos**

- Python 3.10 ou superior instalado.
- Gerenciador de pacotes `pip`.
- Ambiente virtual configurado (`venv`).
- Banco de dados SQLite (já configurado no projeto).

---

### **2. Passos para rodar**

#### **Clone o repositório**

```bash
git clone https://github.com/Eduardo071/eventos-api-python.git
cd eventos-api
```

#### **Crie e ative o ambiente virtual**

No terminal:

```bash
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/Mac
source venv/bin/activate
```

#### **Instale as dependências**

No terminal, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

#### **Realize as migrações do banco de dados**

Crie as tabelas no banco de dados SQLite:

```bash
python manage.py migrate
```

#### **Crie um superusuário**

Para acessar a administração do Django:

```bash
python manage.py createsuperuser
```

#### **Execute o servidor**

Inicie o servidor local:

```bash
python manage.py runserver
```

## Acesse a API em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## **Estrutura do Projeto**

- **eventos**: Diretório principal contendo configurações do projeto.
- `settings.py`: Configurações globais do projeto.
- `urls.py`: URLs principais do projeto.
- `wsgi.py` e `asgi.py`: Arquivos para integração com servidores.
- **eventos_api**: Aplicação contendo lógica da API.
- `models.py`: Definição dos modelos (`Evento` e `Participante`).
- `serializers.py`: Serializadores para transformar modelos em JSON.
- `views.py`: ViewSets para gerenciar as operações da API.
- `urls.py`: URLs específicas da aplicação.
- **db.sqlite3**: Banco de dados SQLite gerado automaticamente.
- **venv**: Ambiente virtual para gerenciar dependências.

---

## **Endpoints da API**

| Método | Endpoint                   | Descrição                      |
| ------ | -------------------------- | ------------------------------ |
| GET    | `/api/eventos/`            | Listar todos os eventos.       |
| POST   | `/api/eventos/`            | Criar um novo evento.          |
| GET    | `/api/eventos/<id>/`       | Obter detalhes de um evento.   |
| PUT    | `/api/eventos/<id>/`       | Atualizar um evento existente. |
| DELETE | `/api/eventos/<id>/`       | Excluir um evento.             |
| GET    | `/api/participantes/`      | Listar todos os participantes. |
| POST   | `/api/participantes/`      | Criar um novo participante.    |
| DELETE | `/api/participantes/<id>/` | Excluir um participante.       |

---

### **Testando a API**

Utilize ferramentas como **Postman**, **Insomnia**, ou o próprio navegador para acessar os
endpoints.
