FROM python:3.12-slim

WORKDIR /app

# Instala dependências do sistema necessárias para compilar libs (se precisar)
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

# Copia e instala requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código (será sobrescrito pelo volume no docker-compose, mas bom para prod)
COPY . .

# Porta interna
EXPOSE 8000