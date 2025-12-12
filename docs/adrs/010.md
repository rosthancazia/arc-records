
### ADR 010: Qualidade de Código e Tipagem Estática

* **Status:** Aceito
* **Data:** 12-12-2025
* **Contexto:**
  Python é uma linguagem dinamicamente tipada, o que pode gerar erros de tempo de execução (Runtime Errors) difíceis de pegar em projetos grandes com múltiplos desenvolvedores.
* **Decisão:**
  O uso de **Type Hints** é mandatório em todo o projeto.
  A pipeline de CI/CD deve bloquear merges que falhem nas seguintes ferramentas:
  1.  **Ruff:** Linter e formatador (substituto ultra-rápido para Black/Flake8/Isort).
  2.  **MyPy:** Verificação estática de tipos.
* **Consequências:**
  * **Positivas:** Redução drástica de bugs simples; código autodocumentado; refatoração mais segura.
  * **Negativas:** O desenvolvimento inicial é ligeiramente mais lento ("brigar" com o linter), mas compensa na manutenção.