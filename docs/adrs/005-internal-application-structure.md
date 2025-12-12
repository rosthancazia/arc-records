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