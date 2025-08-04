#  API4Noobs

> Um projeto minimalista, mas essencial — feito para aprender, testar e dominar os fundamentos de uma API com autenticação, banco de dados e criptografia de senha.

##  Sobre o Projeto

O **API4Noobs** é uma aplicação web construída com Flask que permite a criação, edição, visualização e exclusão de jogos, além da autenticação de usuários com senhas criptografadas.

Criado com a proposta de **aprender na prática** o ciclo de vida de uma API, este projeto cobre:

- Criação e leitura de dados com SQLAlchemy
- Autenticação com Flask-Login + Bcrypt
- Formulários com Flask-WTF
- Proteção CSRF
- Estrutura de templates HTML com Flask

---

##  Tecnologias Utilizadas

- **Flask** — microframework web
- **Flask-WTF** — manipulação de formulários
- **Flask-Bcrypt** — criptografia de senhas
- **SQLAlchemy** — ORM para banco de dados
- **MySQL** — banco relacional
- **WTForms** — validações nos formulários

---

## ⚙️ Funcionalidades

- 🔐 Login e logout com sessões e criptografia
- 📋 Listagem de jogos cadastrados
- ➕ Cadastro de novos jogos
- ✏️ Edição de jogos existentes
- ❌ Exclusão de jogos
- 🧪 Validação de formulário com WTForms
- 🧱 Criação automatizada do banco e tabelas
- 💬 Feedbacks ao usuário com Flask Flash

---

## 🗂 Estrutura Básica
api4noobs/
│
├── app.py # Instância do app Flask
├── game_views.py # Rotas para CRUD de jogos
├── users_views.py # Rotas para autenticação
├── models.py # Definições de tabelas do banco
├── forms.py # Formulários WTForms
├── settings.py # Configurações (chave secreta, URI do banco etc.)
├── init_db.py # Criação inicial do banco e inserção de dados
├── templates/ # Templates HTML
│ ├── list.html
│ ├── new.html
│ ├── edit.html
│ └── login.html
└── static/ # (opcional) Estilos e scripts

