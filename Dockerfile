# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt
COPY requirements.txt /app/

# Atualize o pip para garantir que você tenha a versão mais recente
RUN pip install --upgrade pip

# Instale as dependências do requirements.txt
RUN pip install -r requirements.txt

# Copie o restante do código da aplicação
COPY . /app/

# Defina a variável de ambiente para o Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Exponha a porta que o Flask vai rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run"]
