# projeto_backend_satc

Backend desenvolvido em Python utilizando FastAPI, com gerenciamento de migrations por meio do Alembic e banco de dados PostgreSQL. O projeto tem como objetivo implementar uma API voltada à logística e à cadeia de suprimentos, utilizando camadas para organização das responsabilidades e validação dos dados.

## Iniciar projeto

### Abrir a pasta da aplicação do backend

No terminal PowerShell, navegue até a pasta do projeto e entre no diretório app, onde será configurado o ambiente virtual, ou abra o terminal pela IDE dentro da pasta app:

```powershell
cd projeto_backend_satc
cd app
```

### Criar o ambiente virtual

Crie um ambiente virtual Python chamado .venv:

```powershell
python -m venv .venv
```

O ambiente virtual manterá as bibliotecas utilizadas pelo projeto isoladas da instalação global do Python.

### Ativar o ambiente virtual

No PowerShell, execute:

```powershell
.\.venv\Scripts\Activate.ps1
```

Após a ativação, o terminal deverá exibir o nome do ambiente virtual, geralmente (.venv), antes do caminho atual.

Observação: se o PowerShell bloquear a execução do script de ativação por causa da política de execução, você poderá liberar scripts locais apenas para a sessão atual com:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Em seguida, execute novamente o comando de ativação.

### Instalar as dependências

Com o ambiente virtual ativado, instale as bibliotecas listadas no arquivo requirements.txt:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configurar o banco de dados

### Configurar as variáveis de ambiente

A aplicação utiliza a variável de ambiente DATABASE_URL para configurar a conexão com o PostgreSQL. Essa variável deve conter as informações de conexão com o banco de dados, incluindo usuário, senha, endereço, porta e nome do banco logistica.

Exemplo de formato:

```text
postgresql+psycopg://usuario:senha@localhost:5432/logistica
```

Substitua usuario e senha pelas credenciais configuradas no PostgreSQL.

No PowerShell, a variável pode ser definida para a sessão atual com o seguinte comando:

```powershell
$env:DATABASE_URL = "postgresql+psycopg://usuario:senha@localhost:5432/logistica"
```

Importante: configure a variável de acordo com o mecanismo utilizado pela aplicação. Não versione credenciais reais no repositório nem compartilhe arquivos que contenham senhas.

### Criar o banco de dados

Confirme que o PostgreSQL está em execução e que o banco de dados logistica já foi criado.

Caso ainda não exista, execute o comando abaixo no pgAdmin ou em uma ferramenta de consulta SQL conectada ao PostgreSQL:

```sql
CREATE DATABASE logistica;
```

Se o banco já existir, não será necessário criá-lo novamente.

## Executar migrations

As migrations são gerenciadas pelo Alembic e são utilizadas para criar e atualizar a estrutura do banco de dados conforme as alterações registradas nos modelos da aplicação.

Antes de executá-las, confirme que o PostgreSQL está em execução, que a variável DATABASE_URL está configurada corretamente e que o banco de dados logistica já foi criado.

### Aplicar as migrations existentes

A migration inicial do projeto já está versionada no repositório. Portanto, ao preparar o banco de dados em uma nova instalação, não é necessário gerar outra migration inicial.

Com o terminal na pasta app e o ambiente virtual ativado, execute:

```powershell
python -m alembic -c alembic.ini upgrade head
```

Esse comando aplica as migrations pendentes até a versão mais recente registrada no projeto.

### Criar novas migrations

Quando houver alterações nos modelos que precisem ser refletidas no banco de dados, poderá ser gerada uma nova migration com o comando:

```powershell
python -m alembic -c alembic.ini revision --autogenerate -m "descricao da alteracao"
```

Antes de aplicar uma nova migration, revise o arquivo gerado para verificar se as alterações correspondem ao que foi implementado nos modelos.

Depois da revisão, aplique as alterações com:

```powershell
python -m alembic -c alembic.ini upgrade head
```

Não gere uma nova migration apenas para iniciar o projeto quando as migrations necessárias já estiverem versionadas.

## Executar o projeto

Com o ambiente virtual ativado, as dependências instaladas, a variável DATABASE_URL configurada e as migrations aplicadas, inicie o servidor FastAPI utilizando o Uvicorn.

Considerando que o terminal está na pasta app, execute:

```powershell
python -m uvicorn main:app --reload
```

A opção --reload reinicia automaticamente o servidor quando alterações são detectadas nos arquivos durante o desenvolvimento.

Mantenha o terminal aberto enquanto estiver utilizando a API. Para interromper a execução, pressione Ctrl+C.

Após iniciar o servidor, acesse:

```text
API: http://127.0.0.1:8000
Documentação interativa (Swagger): http://127.0.0.1:8000/docs
Documentação alternativa (ReDoc): http://127.0.0.1:8000/redoc
```

## Verificar o funcionamento da API

### Testar o health check

O endpoint GET /health permite verificar se a aplicação está em execução.

Na documentação Swagger, acesse o endpoint GET /health, clique em Try it out e depois em Execute.

A resposta esperada é HTTP 200, com o seguinte conteúdo:

```json
{
  "status": "ok"
}
```

## Funcionalidades implementadas

### Produtos

A aplicação possui uma implementação inicial de operações relacionadas a produtos, organizada nas camadas de controller, service, repository, models e schemas.

Os endpoints implementados são:

| Método | Endpoint | Descrição |
|---|---|---|
| POST | /produtos/ | Cadastrar um produto |
| GET | /produtos/ | Listar os produtos cadastrados |
| GET | /produtos/{produto_id} | Consultar um produto pelo ID |

### Cadastrar um produto

Para cadastrar um produto, utilize o endpoint POST /produtos/ pela documentação Swagger.

Exemplo de corpo da requisição:

```json
{
  "nome": "Teclado USB",
  "codigo": "TEC-001",
  "descricao": "Teclado USB para teste da API",
  "preco": 89.90
}
```

O endpoint retorna HTTP 201 quando o cadastro é realizado com sucesso, incluindo o identificador gerado pelo banco de dados.

O campo nome é obrigatório e não pode conter apenas espaços em branco. O campo codigo é opcional, mas, quando informado, não pode conter apenas espaços em branco. O preço deve ser maior que zero e respeitar os limites de precisão definidos no schema.

### Listar produtos

O endpoint GET /produtos/ retorna a lista de produtos cadastrados no banco de dados.

Quando a consulta é realizada com sucesso, a API retorna HTTP 200.

### Consultar produto por ID

O endpoint GET /produtos/{produto_id} permite consultar um produto específico pelo identificador.

Quando o produto existe, a API retorna HTTP 200 com os dados encontrados. Quando não existe, retorna HTTP 404 com uma mensagem informando que o produto não foi encontrado.

## Validar os endpoints de produtos

Os testes manuais podem ser executados pela documentação Swagger, disponível em http://127.0.0.1:8000/docs.

### Testar o cadastro de produtos

Envie uma requisição POST /produtos/ com os dados de um produto válido.

Resultado esperado: HTTP 201, com os dados do produto cadastrado.

### Testar a listagem de produtos

Execute uma requisição GET /produtos/.

Resultado esperado: HTTP 200, com uma lista contendo os produtos cadastrados.

### Testar a consulta de um produto existente

Execute uma requisição GET /produtos/{produto_id}, informando o ID de um produto cadastrado.

Resultado esperado: HTTP 200, com os dados do produto encontrado.

### Testar um produto inexistente

Execute uma requisição GET /produtos/9999, desde que não exista um produto com esse identificador.

Resultado esperado: HTTP 404, com uma mensagem informando que o produto não foi encontrado.

### Testar o cadastro com código duplicado

Envie uma requisição POST /produtos/ utilizando um código que já esteja cadastrado.

Resultado esperado na implementação atual: HTTP 400, com uma mensagem informando que não foi possível cadastrar o produto e que o código pode já existir.

### Testar dados inválidos

Envie uma requisição POST /produtos/ com um nome vazio ou composto apenas por espaços e um preço negativo.

Exemplo:

```json
{
  "nome": "  ",
  "codigo": "TEC-004",
  "descricao": "Teste de validação",
  "preco": -90.00
}
```

Resultado esperado: HTTP 422, indicando que os dados enviados não atendem às validações definidas no schema de entrada.

Os procedimentos descritos nesta seção correspondem aos testes manuais realizados pela interface Swagger. Os testes automatizados ainda precisam ser implementados e documentados em uma etapa posterior.

## Estrutura do projeto

A aplicação utiliza uma organização em camadas para separar as responsabilidades e facilitar a manutenção do código.

- controller: recebe as requisições HTTP e define as respostas da API.
- service: concentra as regras de negócio e coordena as operações.
- repository: realiza o acesso aos dados armazenados no banco de dados.
- models: define as entidades persistidas no PostgreSQL.
- schemas: define os formatos dos dados de entrada e saída, incluindo as validações.
- db: concentra a configuração da conexão com o banco e a base dos modelos.
- migrations: registra as alterações estruturais do banco de dados por meio do Alembic.
- docs: reúne a documentação complementar do domínio e do contrato da API.
- tests: destinado à implementação futura dos testes automatizados.

## Próximas etapas

As próximas etapas do projeto incluem a implementação dos CRUDs das demais entidades, a criação das regras de negócio específicas da logística, a revisão do tratamento de erros, a implementação de testes automatizados e a conclusão da documentação do domínio e do contrato da API.

O desenvolvimento deve seguir os requisitos da atividade acadêmica, mantendo a organização em camadas, a validação dos dados, a integridade do banco de dados e a documentação atualizada conforme as funcionalidades forem implementadas.

## Repositório

GitHub: https://github.com/JeanPrei/projeto_backend_satc
