### ADR 009: Padrão de Observabilidade (Logging e Tracing)

* **Status:** Aceito
* **Data:** 12-12-2025
* **Contexto:**
  Em microserviços, uma requisição pode falhar no *Service C* por causa de um dado enviado pelo *Service A*. Logs isolados em arquivos de texto locais são inúteis para debug.
* **Decisão:**
  * **Logging Estruturado:** Todos os serviços devem emitir logs em formato JSON (não texto plano).
  * **Tracing Distribuído:** Implementação do **OpenTelemetry**. Um `Correlation-ID` (ou `Trace-ID`) será gerado na entrada do Gateway e repassado nos headers HTTP/Mensagens RabbitMQ para todos os serviços subsequentes.
* **Consequências:**
  * **Positivas:** Capacidade de ver a "história completa" de uma requisição atravessando o sistema. Detecção rápida de gargalos de performance.
  * **Negativas:** Necessidade de infraestrutura adicional para ingerir e visualizar esses logs (Stack ELK, Loki/Grafana ou SaaS como Datadog).
