### ADR 007: Autenticação Centralizada e Gateway

* **Status:** Aceito
* **Data:** 12-12-2025
* **Contexto:**
  Não é seguro nem eficiente que cada microserviço implemente sua própria lógica de login ou acesse a tabela de usuários. O Frontend não deve conhecer a topologia interna dos microserviços (quais IPs ou portas eles usam).
* **Decisão:**
  Utilizaremos o padrão **API Gateway** como ponto único de entrada.
  * **Fluxo:** O Gateway recebe a requisição -> Verifica a validade do Token JWT (assinatura) -> Faz o roteamento para o microserviço interno.
  * **Microserviços:** Recebem o payload do usuário (ID, Roles) já validado nos headers da requisição, confiando no Gateway.
* **Consequências:**
  * **Positivas:** Simplifica a segurança nos serviços de ponta (Core, Financeiro); centraliza SSL, Rate Limiting e CORS.
  * **Negativas:** O Gateway se torna um ponto crítico de falha (Single Point of Failure); se ele cair, ninguém acessa nada.