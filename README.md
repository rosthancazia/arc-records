## 🏗️ Decisões de Arquitetura (ADRs)

Este projeto segue o padrão de **Architecture Decision Records**.
Abaixo estão as decisões técnicas fundamentais que guiam o desenvolvimento do Simonia:

| ID | Decisão | Arquivo |
|:--:|:---|:---|
| 001 | **Arquitetura** | [Microserviços](./docs/adr/001-microservices-architecture.md) |
| 002 | **Tech Stack** | [Python & FastAPI](./docs/adr/002-backend-tech-stack.md) |
| 003 | **Dados** | [Database per Service](./docs/adr/003-database-strategy.md) |
| 004 | **Comunicação** | [Síncrona vs Assíncrona](./docs/adr/004-communication-strategy.md) |
| 005 | **Código** | [Clean Architecture](./docs/adr/005-internal-application-structure.md) |
| 006 | **Infra** | [Docker & Orquestração](./docs/adr/006-containerization-and-orchestration.md) |
| 007 | **Segurança** | [Auth & API Gateway](./docs/adr/007-authentication-and-gateway.md) |
| 008 | **SaaS** | [Multi-tenancy Strategy](./docs/adr/008-multi-tenancy-strategy.md) |
| 009 | **Operação** | [Padrões de Observabilidade](./docs/adr/009-observability-standards.md) |
| 010 | **Qualidade** | [Linting & Typing](./docs/adr/010-code-quality-guidelines.md) |


micro mvp de arquitetura:

1.  **Traefik (Gateway):** Recebe as chamadas e roteia.
2.  **PostgreSQL (Banco):** O banco de dados do Core.
3.  **RabbitMQ (Fila):** Para comunicação assíncrona.
4.  **Service Core:** Um exemplo funcional do seu microserviço em FastAPI.


### Como Rodar o Projeto

```bash
cd simonia-mvp
docker compose up --build
```

Espere baixar as imagens e iniciar. Quando parar de subir logs loucamente, teste os seguintes links no seu navegador:

1.  **Swagger do Service Core (Via Gateway):**
    👉 [http://localhost/api/v1/core/docs](https://www.google.com/search?q=http://localhost/api/v1/core/docs)
    *Se abrir, o Traefik roteou corretamente para o FastAPI\!*

2.  **Dashboard do Traefik (Gateway):**
    👉 [http://localhost:8080](https://www.google.com/search?q=http://localhost:8080)
    *Aqui você vê todos os microserviços conectados.*

3.  **Dashboard do RabbitMQ:**
    👉 [http://localhost:15672](https://www.google.com/search?q=http://localhost:15672)
    *Login: guest / Senha: guest*