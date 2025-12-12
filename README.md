# Arquitetura de Soluções e Serviços

> base de governança técnica para o projeto mvp **Simonia**.

### Resumo da Lista de ADRs para o Repositório

1.  **Arquitetura:** Microserviços (001)
2.  **Tech Stack:** Python/FastAPI (002)
3.  **Dados:** DB por Serviço (003)
4.  **Comunicação:** Sync/Async (004)
5.  **Código:** Clean Arch (005)
6.  **Infra:** Docker/K8s (006)
7.  **Segurança:** Gateway/Auth (007)
8.  **Negócio/SaaS:** Multi-tenancy (008)
9.  **Operação:** Observabilidade (009)
10. **Qualidade:** Linting/Typing (010)


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