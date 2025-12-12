### ADR 006: Estratégia de Containerização e Orquestração

* **Status:** Aceito
* **Data:** 12-12-2025
* **Contexto:**
  Precisamos garantir paridade entre os ambientes de desenvolvimento, teste e produção. "Funciona na minha máquina" não é aceitável em sistemas distribuídos. Além disso, precisamos gerenciar a vida útil de múltiplos serviços simultaneamente.
* **Decisão:**
  * **Containerização:** Docker (OCI compliant images). Cada microserviço terá seu próprio `Dockerfile`.
  * **Desenvolvimento Local:** Docker Compose (orquestrando serviços + bancos + filas).
  * **Produção:** Kubernetes (K8s) ou serviço gerenciado de containers (ex: AWS ECS / Google Cloud Run).
* **Consequências:**
  * **Positivas:** Portabilidade total; o ambiente é imutável desde o build até o deploy. Facilidade de escalar réplicas de serviços específicos.
  * **Negativas:** Curva de aprendizado de Kubernetes e *overhead* de recursos para rodar tudo localmente (exige máquinas de desenvolvimento com mais RAM).