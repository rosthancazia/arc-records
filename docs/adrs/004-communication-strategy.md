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