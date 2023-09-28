# FlaskIrisDataFilter

# Flask Iris Dataset Web App

Este é um projeto simples de aplicativo da web Flask que utiliza o conjunto de dados Iris para filtragem e exportação de dados. Você pode filtrar os dados com base nos comprimentos e larguras da sépala e pétala e exportar os resultados em um arquivo CSV.

## Requisitos

Antes de executar o aplicativo, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Flask
- scikit-learn (para o conjunto de dados Iris)
- Docker (opcional, se você desejar executar o aplicativo em um contêiner Docker)

## Instalação e Execução

1. Clone este repositório para o seu sistema local:

    git clone https://github.com/seu-usuario/seu-repositorio.git

2. Navegue até o diretório do projeto:

    cd seu-repositorio

3. Instale as dependências Python usando o pip:

    pip install -r requirements.txt
4. Execute o aplicativo Flask:

    python app.py

O aplicativo estará disponível em http://localhost:5000 em seu navegador.

Se preferir, você também pode executar o aplicativo em um contêiner Docker:

## Certifique-se de que o Docker esteja instalado em seu sistema.

1. Construa a imagem Docker:

    docker build -t flask-iris-app .

2. Execute o contêiner Docker:

    docker run -p 5000:5000 flask-iris-app

O aplicativo estará disponível em http://localhost:5000 da mesma forma.

## Uso

- Acesse http://localhost:5000 em seu navegador.
- Preencha os campos do formulário para filtrar os dados do conjunto de dados Iris.
- Clique no botão "Filtrar" para ver os resultados na tabela.
- Clique no botão "Exportar Dados" para baixar os dados filtrados em um arquivo CSV.