# projeto_backend_satc
Backend desenvolvido em Python utilizando FastAPI, com gerenciamento de migrations por meio do Alembic e banco de dados PostgreSQL.

## Inciar projeto
### Abrir a pasta da aplicação do backend
No terminal PowerShell, navegue até a pasta do projeto e entre no diretório app, onde será configurado o ambiente virtual ou abra o terminal pela IDE, dentro da pasta app:
```
cd projeto_backend_satc
cd app
```

### Criar o ambiente virtual
Crie um ambiente virtual Python chamado .venv:

```
python -m venv .venv
```
O ambiente virtual manterá as bibliotecas utilizadas pelo projeto isoladas da instalação global do Python.

### Ativar o ambiente virtual
No PowerShell, execute:
```
.\.venv\Scripts\Activate.ps1
```

Após a ativação, o terminal deverá exibir o nome do ambiente virtual, geralmente (.venv), antes do caminho atual.

Observação: se o PowerShell bloquear a execução do script de ativação por causa da política de execução, você poderá liberar scripts locais apenas para a sessão atual com:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
Em seguida, execute novamente o comando de ativação.

### Instalar as dependências
Com o ambiente virtual ativado, instale as bibliotecas listadas no arquivo requirements.txt:
```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Configurar as variáveis de ambiente
Configure a variável DATABASE_URL, dentro do Arquivo db/database.py utilizada pela aplicação e pelo Alembic para acessar o PostgreSQL.

A URL deve conter as informações de conexão do banco de dados, incluindo usuário, senha, endereço, porta e nome do banco logistica.

Exemplo de formato:
```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/logistica
```
Substitua usuario e senha pelas credenciais configuradas no PostgreSQL.

Importante: configure a variável de ambiente conforme o mecanismo utilizado pela aplicação. Se o projeto utilizar um arquivo .env, preencha-o de acordo com as variáveis esperadas pelo código. Não versione credenciais reais no repositório.

Confirme também que o PostgreSQL está em execução e que o banco logistica já foi criado:
```
CREATE DATABASE logistica;
```

## Executar o projeto

Com o ambiente virtual ativado e as dependências instaladas, inicie o servidor FastAPI utilizando o Uvicorn:
```
python -m uvicorn main:app --reload
```

A opção --reload reinicia automaticamente o servidor quando alterações são detectadas nos arquivos durante o desenvolvimento.

Após iniciar o servidor, acesse:
```
    API: http://127.0.0.1:8000
    Documentação interativa (Swagger): http://127.0.0.1:8000/docs
    Documentação alternativa (ReDoc): http://127.0.0.1:8000/redoc
```
## Executar migrations

As migrations são gerenciadas pelo Alembic e usam a configuração `DATABASE_URL` da aplicação.
Antes de executá-las, confirme que o PostgreSQL está rodando, que a URL de conexão está configurada corretamente e que o banco de dados `logistica` já foi criado.

Como o Alembic é uma biblioteca, é necessário conferir se, você já está na pasta app e o venv está ativado, caso contrário, é necessário executar os comandos abaixo (assumindo que os requisitos já foram adicionados a venv ao iniciar o projeto, no passo a passo anterior):

```powershell
cd app
.\.venv\Scripts\Activate.ps1
```

Na primeira migration do projeto, gere a revisão inicial a partir dos modelos e aplique-a:

```powershell
python -m alembic -c alembic.ini revision --autogenerate -m "initial schema"
python -m alembic -c alembic.ini upgrade head
```
