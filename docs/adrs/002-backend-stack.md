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