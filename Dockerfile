# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho para a pasta onde o Flask será executado
WORKDIR /app/projeto

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt /app/

# Atualize o pip para garantir que você tenha a versão mais recente
RUN pip install --upgrade pip

# Instale as dependências do requirements.txt
RUN pip install -r /app/requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho no container
COPY . /app/

# Defina a variável de ambiente para o Flask
ENV FLASK_APP=projeto/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Exponha a porta que o Flask vai rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run"]