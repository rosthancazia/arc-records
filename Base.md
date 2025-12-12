### ADR 001: Adoção de Arquitetura de Microserviços

* **Status:** Aceito
* **Data:** 12-12-2025
* **Contexto:**
  O projeto Simonia visa atender condomínios com múltiplos domínios de negócio distintos (financeiro, operacional, portaria, gestão de moradores). Uma arquitetura monolítica poderia acelerar o início, mas traria riscos de acoplamento excessivo entre módulos críticos (ex: uma falha no módulo de reserva de churrasqueira não deve derrubar a emissão de boletos). Precisamos de escalabilidade independente e isolamento de falhas.
* **Decisão:**
  Adotaremos uma arquitetura baseada em **Microserviços**.
  Os domínios iniciais identificados são:
  1.  **Auth Service:** Gestão de identidade e acesso.
  2.  **Core Service:** Cadastros base (Unidades, Blocos, Pessoas).
  3.  **Finance Service:** Contas a pagar/receber, boletos, integração bancária.
  4.  **Ops Service:** Reservas, ocorrências e manutenção.
  5.  **Gatekeeper Service:** Controle de portaria e encomendas.
* **Consequências:**
  * **Positivas:** Deploy independente, escalabilidade granular, liberdade tecnológica por serviço, isolamento de falhas.
  * **Negativas:** Aumento da complexidade operacional (DevOps), necessidade de gestão de consistência eventual e latência de rede entre serviços.

---

### ADR 002: Backend Stack - Python e FastAPI

* **Status:** Aceito
* **Data:** 12-12-2025
* **Contexto:**
  Precisamos de uma tecnologia de backend que ofereça alta performance para I/O (Input/Output), facilidade de manutenção, tipagem forte para segurança de dados e documentação automática para facilitar a integração com o Frontend.
* **Decisão:**
  O backend será desenvolvido em **Python 3.11+** utilizando o framework **FastAPI**.
  * Gerenciador de pacotes: Poetry ou Pip.
  * Servidor ASGI: Uvicorn/Gunicorn.
* **Consequências:**
  * **Positivas:** Suporte nativo a concorrência (async/await), validação automática de dados com Pydantic, geração automática de OpenAPI (Swagger), ecossistema rico de bibliotecas.
  * **Negativas:** Curva de aprendizado inicial para desenvolvedores acostumados apenas com frameworks síncronos (como Django tradicional ou Flask antigo).

---

### ADR 003: Estratégia de Persistência de Dados (Database per Service)

* **Status:** Aceito
* **Data:** 12-12-2025
* **Contexto:**
  Em arquiteturas distribuídas, compartilhar um único banco de dados entre múltiplos serviços cria um acoplamento forte, impedindo mudanças de schema independentes e criando um ponto único de falha e gargalo de performance.
* **Decisão:**
  Aplicaremos o padrão **Database per Service**. Cada microserviço terá seu próprio database lógico ou físico.
  * **Dados Relacionais (Core, Finance):** PostgreSQL + SQLAlchemy (Async).
  * **Dados Não-Estruturados/Logs:** MongoDB.
  * **Cache/Sessão:** Redis.
  * **Migrações:** Alembic.
* **Consequências:**
  * **Positivas:** Desacoplamento total de dados; serviços podem escolher a melhor tecnologia de banco para seu problema.
  * **Negativas:** Impossibilidade de fazer `JOINs` entre tabelas de domínios diferentes. Consultas complexas que agregam dados (ex: "Boletos do Morador X") exigirão composição de API ou replicação de dados via eventos.

---

### ADR 004: Comunicação Inter-serviços

* **Status:** Aceito
* **Data:** 12-12-2025
* **Contexto:**
  Os serviços precisam trocar informações. Depender exclusivamente de chamadas HTTP síncronas cria acoplamento temporal (se o serviço B cai, o serviço A trava) e aumenta a latência.
* **Decisão:**
  Utilizaremos uma abordagem híbrida:
  1.  **Síncrona (HTTP/REST):** Apenas para leituras diretas onde a resposta imediata é mandatória e para comunicação Frontend -> Gateway.
  2.  **Assíncrona (Event-Driven):** Para escritas e efeitos colaterais, utilizando **RabbitMQ** como Message Broker.
      * *Exemplo:* O "Financeiro" publica evento `BOLETO_PAGO`. O "Ops" escuta para liberar reserva.
* **Consequências:**
  * **Positivas:** Resiliência do sistema; se um serviço consumidor estiver offline, a mensagem persiste na fila até ele voltar.
  * **Negativas:** Complexidade de rastreamento (necessário Tracing Distribuído) e necessidade de lidar com consistência eventual.

---

### ADR 005: Estrutura Interna dos Serviços (Clean Architecture)

* **Status:** Aceito
* **Data:** 12-12-2025
* **Contexto:**
  Para garantir a manutenibilidade a longo prazo e facilitar testes unitários, o código não deve misturar lógica de framework (rotas HTTP) com lógica de negócio e acesso a banco de dados.
* **Decisão:**
  Adotaremos uma estrutura inspirada em **Clean Architecture**, dividindo cada microserviço em camadas claras:
  * `app/api`: Camada de Interface (Controllers/Routes).
  * `app/schemas`: Contratos de dados (DTOs/Pydantic).
  * `app/services`: Regra de negócio pura.
  * `app/models`: Entidades de persistência (ORM).
  * `app/db` & `app/core`: Infraestrutura e Configuração.
* **Consequências:**
  * **Positivas:** Testabilidade alta (fácil "mockar" o banco de dados), clareza na separação de responsabilidades e facilidade para novos devs se localizarem.
  * **Negativas:** Aumento no número de arquivos (boilerplate) para funcionalidades simples (ex: criar um arquivo de rota, schema, service e model para um CRUD básico).

---

### Como aplicar isso no GitHub

1.  Crie uma pasta na raiz do projeto chamada `docs`.
2.  Dentro dela, crie uma pasta `adr`.
3.  Salve os textos acima como:
    * `001-microservices-architecture.md`
    * `002-backend-stack.md`
    * `003-database-strategy.md`
    * `004-communication-strategy.md`
    * `005-internal-structure.md`
