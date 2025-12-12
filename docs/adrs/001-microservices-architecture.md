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