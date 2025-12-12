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