# Contrato da API — Logística e Cadeia de Suprimentos

## 1. Informações gerais

- **Base local:** `http://127.0.0.1:8000`
- **Formato:** JSON (`Content-Type: application/json` nos corpos das requisições)
- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`
- **Health check:** `GET /health`

Os exemplos abaixo descrevem as rotas registradas atualmente pelos Controllers na aplicação. Não estão documentados `PUT` nem `DELETE`, porque não há essas operações implementadas nos Controllers atuais.

## 2. Resumo das rotas

| Método | Rota | Descrição | Sucesso |
|---|---|---|---|
| `GET` | `/health` | Verifica se a aplicação está ativa. | `200 OK` |
| `POST` | `/produtos/` | Cadastra um produto. | `201 Created` |
| `GET` | `/produtos/` | Lista produtos. | `200 OK` |
| `GET` | `/produtos/{produto_id}` | Busca um produto pelo ID. | `200 OK` |
| `POST` | `/estoques/` | Cadastra um registro de estoque. | `201 Created` |
| `GET` | `/estoques/` | Lista registros de estoque. | `200 OK` |
| `GET` | `/estoques/{estoque_id}` | Busca um registro de estoque pelo ID. | `200 OK` |
| `POST` | `/veiculos/` | Cadastra um veículo. | `201 Created` |
| `GET` | `/veiculos/` | Lista veículos. | `200 OK` |
| `GET` | `/veiculos/{veiculo_id}` | Busca um veículo pelo ID. | `200 OK` |
| `POST` | `/rotas/` | Cadastra uma rota. | `201 Created` |
| `GET` | `/rotas/` | Lista rotas. | `200 OK` |
| `GET` | `/rotas/{rota_id}` | Busca uma rota pelo ID. | `200 OK` |
| `POST` | `/entregas/` | Cadastra uma entrega. | `201 Created` |
| `GET` | `/entregas/` | Lista entregas. | `200 OK` |
| `GET` | `/entregas/{entrega_id}` | Busca uma entrega pelo ID. | `200 OK` |
| `POST` | `/rastreamentos/` | Cadastra um registro de rastreamento. | `201 Created` |
| `GET` | `/rastreamentos/` | Lista registros de rastreamento. | `200 OK` |
| `GET` | `/rastreamentos/{rastreamento_id}` | Busca um registro de rastreamento pelo ID. | `200 OK` |

As rotas de listagem retornam uma lista JSON, inclusive quando não há registros (nesse caso, `[]`). As rotas de busca retornam um objeto JSON individual.

## 3. Health check

### `GET /health`

Verifica se a aplicação está em execução.

**Resposta `200 OK`:**

```json
{
  "status": "ok"
}
```

## 4. Produtos

### `POST /produtos/` — cadastrar produto

**JSON de entrada:**

```json
{
  "nome": "Teclado USB",
  "codigo": "TEC-001",
  "descricao": "Teclado USB para teste da API",
  "preco": 89.90
}
```

`codigo` e `descricao` podem ser `null` ou omitidos. `nome` não pode ficar vazio e `preco` deve ser maior que zero, com até duas casas decimais.

**Resposta `201 Created`:**

```json
{
  "id": 1,
  "nome": "Teclado USB",
  "codigo": "TEC-001",
  "descricao": "Teclado USB para teste da API",
  "preco": "89.90"
}
```

### `GET /produtos/` — listar produtos

**Resposta `200 OK` (exemplo):**

```json
[
  {
    "id": 1,
    "nome": "Teclado USB",
    "codigo": "TEC-001",
    "descricao": "Teclado USB para teste da API",
    "preco": "89.90"
  }
]
```

### `GET /produtos/{produto_id}` — buscar por ID

Exemplo: `GET /produtos/1`.

**Resposta `200 OK`:** retorna um objeto no mesmo formato do item mostrado na listagem. Se o ID não existir, a resposta atual é `404 Not Found`.

## 5. Estoques

### `POST /estoques/` — cadastrar estoque

**JSON de entrada:**

```json
{
  "produto_id": 1,
  "localizacao": "Galpão A",
  "quantidade": 50,
  "estoque_minimo": 10
}
```

`quantidade` e `estoque_minimo` podem ser omitidos; o valor padrão é `0`. Ambos devem ser maiores ou iguais a zero. O `produto_id` deve apontar para um produto existente.

**Resposta `201 Created`:**

```json
{
  "id": 1,
  "produto_id": 1,
  "localizacao": "Galpão A",
  "quantidade": 50,
  "estoque_minimo": 10
}
```

### `GET /estoques/` — listar estoques

**Resposta `200 OK` (exemplo):**

```json
[
  {
    "id": 1,
    "produto_id": 1,
    "localizacao": "Galpão A",
    "quantidade": 50,
    "estoque_minimo": 10
  }
]
```

### `GET /estoques/{estoque_id}` — buscar por ID

Exemplo: `GET /estoques/1`.

**Resposta `200 OK`:** retorna um objeto no mesmo formato do item da listagem. Se o estoque não existir, retorna `404 Not Found`.

## 6. Veículos

### `POST /veiculos/` — cadastrar veículo

**JSON de entrada:**

```json
{
  "placa": "ABC1D23",
  "modelo": "Caminhão leve",
  "capacidade_kg": 3500.00,
  "disponivel": true
}
```

`disponivel` pode ser omitido e assume `true`. A placa é convertida para maiúsculas e deve ser única. `capacidade_kg` deve ser maior que zero.

**Resposta `201 Created`:**

```json
{
  "id": 1,
  "placa": "ABC1D23",
  "modelo": "Caminhão leve",
  "capacidade_kg": "3500.00",
  "disponivel": true
}
```

### `GET /veiculos/` — listar veículos

**Resposta `200 OK` (exemplo):**

```json
[
  {
    "id": 1,
    "placa": "ABC1D23",
    "modelo": "Caminhão leve",
    "capacidade_kg": "3500.00",
    "disponivel": true
  }
]
```

### `GET /veiculos/{veiculo_id}` — buscar por ID

Exemplo: `GET /veiculos/1`.

**Resposta `200 OK`:** retorna um objeto no mesmo formato do item da listagem. Se o veículo não existir, retorna `404 Not Found`.

## 7. Rotas de transporte

### `POST /rotas/` — cadastrar rota

**JSON de entrada:**

```json
{
  "origem": "Criciúma - SC",
  "destino": "Florianópolis - SC",
  "distancia_km": 200.00,
  "tempo_estimado_horas": 3.00
}
```

`tempo_estimado_horas` é opcional. A origem e o destino não podem ficar vazios; distância e tempo estimado, quando informado, devem ser maiores que zero.

**Resposta `201 Created`:**

```json
{
  "id": 1,
  "origem": "Criciúma - SC",
  "destino": "Florianópolis - SC",
  "distancia_km": "200.00",
  "tempo_estimado_horas": "3.00"
}
```

### `GET /rotas/` — listar rotas

**Resposta `200 OK` (exemplo):**

```json
[
  {
    "id": 1,
    "origem": "Criciúma - SC",
    "destino": "Florianópolis - SC",
    "distancia_km": "200.00",
    "tempo_estimado_horas": "3.00"
  }
]
```

### `GET /rotas/{rota_id}` — buscar por ID

Exemplo: `GET /rotas/1`.

**Resposta `200 OK`:** retorna um objeto no mesmo formato do item da listagem. Se a rota não existir, retorna `404 Not Found`.

## 8. Entregas

### `POST /entregas/` — cadastrar entrega

**JSON de entrada:**

```json
{
  "rota_id": 1,
  "veiculo_id": 1,
  "destinatario": "Cliente Exemplo",
  "previsao_entrega": "2026-10-20T14:30:00",
  "status": "Em preparação"
}
```

`previsao_entrega` é opcional e deve ser uma data/hora válida no formato ISO 8601. A rota e o veículo informados precisam existir. O código atual valida a existência dos registros relacionados, mas não verifica se o veículo está marcado como disponível nem define uma lista fechada de status.

**Resposta `201 Created`:**

```json
{
  "id": 1,
  "rota_id": 1,
  "veiculo_id": 1,
  "destinatario": "Cliente Exemplo",
  "previsao_entrega": "2026-10-20T14:30:00",
  "status": "Em preparação"
}
```

### `GET /entregas/` — listar entregas

**Resposta `200 OK` (exemplo):**

```json
[
  {
    "id": 1,
    "rota_id": 1,
    "veiculo_id": 1,
    "destinatario": "Cliente Exemplo",
    "previsao_entrega": "2026-10-20T14:30:00",
    "status": "Em preparação"
  }
]
```

### `GET /entregas/{entrega_id}` — buscar por ID

Exemplo: `GET /entregas/1`.

**Resposta `200 OK`:** retorna um objeto no mesmo formato do item da listagem. Se a entrega não existir, retorna `404 Not Found`.

## 9. Rastreamentos

### `POST /rastreamentos/` — cadastrar rastreamento

**JSON de entrada:**

```json
{
  "entrega_id": 1,
  "localizacao": "Centro de distribuição — Criciúma/SC",
  "data_hora": "2026-10-15T08:30:00",
  "observacao": "Mercadoria recebida no centro de distribuição"
}
```

`observacao` é opcional. `entrega_id` deve apontar para uma entrega existente. `localizacao` e `data_hora` são obrigatórios.

**Resposta `201 Created`:**

```json
{
  "id": 1,
  "entrega_id": 1,
  "localizacao": "Centro de distribuição — Criciúma/SC",
  "data_hora": "2026-10-15T08:30:00",
  "observacao": "Mercadoria recebida no centro de distribuição"
}
```

### `GET /rastreamentos/` — listar rastreamentos

**Resposta `200 OK` (exemplo):**

```json
[
  {
    "id": 1,
    "entrega_id": 1,
    "localizacao": "Centro de distribuição — Criciúma/SC",
    "data_hora": "2026-10-15T08:30:00",
    "observacao": "Mercadoria recebida no centro de distribuição"
  }
]
```

### `GET /rastreamentos/{rastreamento_id}` — buscar por ID

Exemplo: `GET /rastreamentos/1`.

**Resposta `200 OK`:** retorna um objeto no mesmo formato do item da listagem. Se o registro de rastreamento não existir, retorna `404 Not Found`.

## 10. Erros e validações

Os corpos de erro abaixo refletem o formato usado atualmente pelo FastAPI/Controllers. Nem todos os erros estão padronizados em um único DTO.

| Situação atual | HTTP | Exemplo de corpo |
|---|---:|---|
| Campo inválido ou JSON incompatível com o schema Pydantic | `422 Unprocessable Entity` | `{"detail": [...]}` |
| ID solicitado não encontrado | `404 Not Found` | `{"detail": "Produto com ID 9999 não encontrado."}` |
| `produto_id` inexistente ao cadastrar estoque | `404 Not Found` | `{"detail": "Produto com ID 9999 não encontrado."}` |
| `rota_id` ou `veiculo_id` inexistente ao cadastrar entrega | `404 Not Found` | `{"detail": "A rota informada não existe."}` ou `{"detail": "O veículo informado não existe."}` |
| `entrega_id` inexistente ao cadastrar rastreamento | `404 Not Found` | `{"detail": "A entrega informada não existe."}` |
| Código de produto duplicado (ou outra falha de integridade no cadastro de produto) | `400 Bad Request` | `{"detail": "Não foi possível cadastrar o produto. Verifique se o código já existe."}` |
| Placa de veículo duplicada | `409 Conflict` | `{"detail": "Não foi possível cadastrar o veículo. Verifique se a placa já está cadastrada."}` |
| Falha de integridade ao cadastrar estoque | `400 Bad Request` | `{"detail": "Não foi possível cadastrar o estoque. Verifique os dados informados."}` |
| Falha de integridade ao cadastrar rota | `409 Conflict` | `{"detail": "Não foi possível cadastrar a rota. Verifique os dados informados."}` |

**Observação para a entrega acadêmica:** o enunciado da disciplina pede `400` para campo inválido e para regra de negócio violada. Na implementação atual, a validação automática do FastAPI retorna `422`, e algumas falhas de domínio retornam `404` ou `409`. O contrato documenta o comportamento existente; para atender integralmente ao critério do professor, o tratamento de status precisa ser uniformizado no código e depois refletido neste documento.
