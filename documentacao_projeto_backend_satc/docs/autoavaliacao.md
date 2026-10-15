# Autoavaliação — Projeto Backend SATC

**Projeto:** Logística e Cadeia de Suprimentos  
**Repositório:** https://github.com/JeanPrei/projeto_backend_satc  
**Escopo desta autoavaliação:** revisão estática do repositório e dos arquivos consultados. A inicialização em uma instalação limpa e os testes manuais da API precisam ser confirmados pelo grupo antes da entrega.

## Critérios da revisão

Use as marcações do enunciado: ✅ atende; ◐ parcial; ❌ não atende. A autoavaliação abaixo é uma revisão preliminar do estado atual do código, não uma garantia de nota.

| Critério | Avaliação | Evidência e pendências |
|---|---|---|
| **P1 — Sobe pelo README** | ◐ Parcial | O README explica a criação do ambiente Python, a configuração de `DATABASE_URL`, as migrations e a inicialização com Uvicorn. Não há `docker-compose.yml` no repositório e é necessário preparar o PostgreSQL manualmente. Falta testar o procedimento completo em uma máquina ou pasta limpa, seguindo somente o README. |
| **P2 — Camadas** | ◐ Parcial | O código separa `controller`, `service`, `repository`, `models` e `schemas`, mas não possui uma camada explícita `mapper`. Para a adaptação em Python, o README deve explicar o equivalente utilizado e como o projeto atende ao critério de arquitetura da disciplina. |
| **P3 — Banco e entidades** | ✅ Atende | A migration do Alembic cria as seis tabelas (`produtos`, `estoques`, `veiculos`, `rotas`, `entregas` e `rastreamentos`) e inclui as chaves estrangeiras do modelo. Os modelos SQLAlchemy correspondem às tabelas declaradas. |
| **P4 — DTOs de entrada e saída** | ✅ Atende | Há schemas Pydantic de entrada e saída para as seis entidades em `app/schemas/`. Os Controllers declaram os schemas de entrada e os `response_model` de saída. |
| **P5 — Estrutura completa e documentada** | ◐ Parcial | Todas as entidades possuem Controllers, Services, Repositories, Models e Schemas. Porém não existe camada `mapper` explícita e nem todas as classes possuem o comentário de cabeçalho com camada, responsabilidade, regras, rotas e situação. O mapa do README também precisa ser conferido contra as funcionalidades atuais. |
| **P6 — API simples** | ◐ Parcial | As seis entidades possuem `POST`, `GET` de listagem e `GET /{id}` nos Controllers. As buscas por ID inexistente retornam `404`. Entretanto, a validação padrão do FastAPI retorna `422` para campos inválidos, enquanto o critério pede `400`; também não há uma classe própria de exceção para recurso não encontrado. |
| **P7 — Regras de negócio implementadas** | ◐ Parcial | Existem verificações no Service: código de produto único (erro de integridade tratado no Controller), placa de veículo única, estoque vinculado a produto existente, entrega vinculada a rota e veículo existentes e rastreamento vinculado a entrega existente. Falta formalizar no README pelo menos três regras numeradas e garantir que as violações de regra retornem `400` com mensagem explicativa, conforme o enunciado. |
| **P8 — Regras que atendem ao tema** | ◐ Parcial | As verificações de produto, estoque, veículo, rota, entrega e rastreamento têm relação com logística. Ainda faltam regras operacionais mais específicas do problema escolhido, caso façam parte da proposta do grupo, e a demonstração por requisições que comprovem cada regra. |
| **P9 — Código igual ao desenho** | ✅ Atende após incluir estes documentos | O modelo de domínio e o contrato da API desta pasta descrevem as seis entidades, os relacionamentos e as rotas registradas pelos Controllers atuais. Antes de entregar, o grupo deve executar a migration e conferir exemplos e respostas pela documentação Swagger. |
| **P10 — README** | ◐ Parcial | O README contém instalação, configuração do banco, migrations, execução, Swagger e exemplos. Porém descreve a funcionalidade de Produtos como a única implementação e diz que as demais operações ficam para etapas futuras, apesar de os Controllers atuais já possuírem rotas para as seis entidades. Também precisa destacar claramente o problema que o sistema resolve, quem o utiliza e pelo menos três regras de negócio numeradas. |

## Regras atualmente identificadas no código

Estas verificações foram encontradas nos Services, schemas ou restrições do banco. O grupo deve confirmar se elas correspondem às regras de negócio apresentadas no README e preparar testes demonstráveis para elas.

| Identificador sugerido | Regra identificada | Onde é verificada atualmente |
|---|---|---|
| **R1** | O código de um produto, quando informado, não pode se repetir. | `Produto` possui restrição `UNIQUE` para `codigo`; o Controller de produto trata falhas de integridade no cadastro. |
| **R2** | Um registro de estoque só pode ser criado para um produto já cadastrado. | `EstoqueService.criar()`. |
| **R3** | Uma entrega só pode ser cadastrada se a rota e o veículo referenciados existirem. | `EntregaService.criar()`. |
| **R4** | Um registro de rastreamento só pode ser criado para uma entrega existente. | `RastreamentoService.criar()`. |
| **R5** | A placa do veículo deve ser única. | Restrição `UNIQUE` em `Veiculo.placa`; `VeiculoService.criar()` trata a violação. |

**Atenção:** a existência de uma checagem no código não garante, sozinha, que todos os critérios do professor estejam atendidos. As regras precisam estar claramente descritas no README, ter relação com o problema de logística que o grupo definiu e ser demonstradas pela API. Além disso, os status de erro precisam seguir o formato exigido pela atividade.

## Pendências prioritárias antes da entrega

1. Atualizar o README para descrever as seis entidades e as rotas que já estão funcionando; remover a afirmação de que só Produtos tem endpoints implementados.
2. Escrever no README o problema específico do grupo, os usuários do sistema e ao menos três regras de negócio numeradas, indicando o Service onde cada uma está implementada.
3. Ajustar o tratamento para o contrato acadêmico exigido: campo inválido e regra de negócio violada devem retornar `400`, com mensagem explicativa; ID inexistente deve retornar `404`.
4. Criar uma forma reproduzível de iniciar o PostgreSQL (idealmente Docker Compose, conforme as orientações da disciplina) e validar todos os comandos do README a partir de um clone limpo.
5. Revisar a organização equivalente à camada Mapper e acrescentar cabeçalhos de documentação nas classes, explicando no README como a solução em Python atende aos critérios originalmente escritos para Java/Spring.
6. Testar pelo Swagger pelo menos: um `POST` válido, listagem, busca por ID existente, busca por ID inexistente, campo inválido e uma requisição para cada regra de negócio escolhida.

## Registro do grupo

Após realizar as verificações acima, os integrantes devem revisar as marcações desta autoavaliação em conjunto e alterá-las para refletir o estado real da branch `main` no momento da entrega.
