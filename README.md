# Arquitetura de Soluções e Serviços

> base de governança técnica para o projeto mvp **Simonia**.

### Resumo da Lista de ADRs para o Repositório

Ao colocar esses 10 arquivos no seu GitHub, você cobre:

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


micro mvp de arquitetura : 

Excelente. Para tirar o **Simonia** do papel é a validação do sua arq em micro ambiente.
para isso tem um lab na pasta simonia com os componentes principais de um microserviço backend

Este setup vai levantar:

1.  **Traefik (Gateway):** Recebe as chamadas e roteia.
2.  **PostgreSQL (Banco):** O banco de dados do Core.
3.  **RabbitMQ (Fila):** Para comunicação assíncrona.
4.  **Service Core:** Um exemplo funcional do seu microserviço em FastAPI.


### \. Como Rodar o Projeto

Abra seu terminal na pasta raiz `simonia` e execute:

```bash
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

### Resumo do que fizemos

Você agora tem a infraestrutura **real** rodando na sua máquina. O Traefik está escutando na porta 80. Se você acessar `localhost/api/v1/core`, ele manda para o container Python. Se você criar o serviço financeiro amanhã, basta adicionar no docker-compose e mudar a rota para `/api/v1/financeiro`.

**Próximo passo:** Gostaria que eu configurasse a conexão real com o Banco de Dados no `main.py` usando SQLAlchemy Async para criarmos a primeira tabela (ex: `Condominio`)?