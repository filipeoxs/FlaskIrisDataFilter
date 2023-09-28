# Use a imagem base do Python
FROM python:3.8

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt e instale as dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copie o restante do código-fonte para o contêiner
COPY . .

# Exponha a porta que o aplicativo Flask irá escutar
EXPOSE 5000

# Defina a variável de ambiente FLASK_APP para o seu aplicativo
ENV FLASK_APP=app.py

# Execute o aplicativo Flask quando o contêiner for iniciado
CMD ["flask", "run", "--host", "0.0.0.0"]
