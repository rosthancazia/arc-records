### ADR 008: Estratégia de Multi-tenancy (Isolamento de Condomínios)

* **Status:** Aceito
* **Data:** 12-12-2025
* **Contexto:**
  O Simonia é um SaaS B2B. Os dados do "Condomínio A" **jamais** podem vazar para o "Condomínio B". Criar um banco de dados físico para cada condomínio é caro e difícil de manter (migrações em 1000 bancos diferentes).
* **Decisão:**
  Adotaremos o padrão **Shared Database, Schema Discriminator**.
  * Todas as tabelas terão uma coluna obrigatória `condominio_id` (ou `tenant_id`).
  * O código da aplicação (Service Layer) deve obrigatoriamente filtrar todas as queries por este ID, injetado via dependência do token do usuário logado.
* **Consequências:**
  * **Positivas:** Custo de infraestrutura baixo; facilidade para fazer queries analíticas globais.
  * **Negativas:** Risco de vazamento de dados por erro de programação (esquecer o `where condominio_id = X`). Exige testes rigorosos e Code Review focado nisso.

---