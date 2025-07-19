# Books API Tech Challenge

![technology Python](https://img.shields.io/badge/technology-python>=3.12-yellow.svg)


Este é um projeto responsável por disponibilizar a consulta de livros disponíveis no website https://books.toscrape.com/, com o objetivo que possa ser utilizado para consultas e usos em modelos de machine learning.



## Documentação Complementar

- **[Arquitetura e processos](docs/arquitecture_design)** - Detalhes sobre a arquitetura e fluxo de processamento

- **[Uso para Machine Learning](docs/machine_learning_usage.md)** - Casos de uso e integração com ML

## Arquitetura de pastas e arquivos

```
books_api_tech_challenge/
├── config/                         # Configurações da aplicação
├── docs/                           # Documentação do projeto
│   └── img/                        # Imagens da documentação
├── dto/                            # Data Transfer Objects
├── handler/                        # Handlers da API (camada de apresentação)
├── models/                         # Modelos de dados
├── repository/                     # Repositórios de dados (camada de acesso)
├── scripts/                        # Scripts utilitários
└── services/                       # Serviços de negócio (camada de lógica)
```

### Descrição das principais pastas:

- **`handler/`**: Contém os controllers da API FastAPI, responsáveis por receber as requisições HTTP e chamar os serviços apropriados
- **`services/`**: Implementa a lógica de negócio da aplicação, incluindo o web scraping e processamento de dados
- **`repository/`**: Camada de acesso aos dados, responsável pela leitura e escrita dos dados dos livros
- **`models/`**: Define as estruturas de dados (entidades) utilizadas na aplicação
- **`dto/`**: Data Transfer Objects utilizados para transferir dados entre as camadas da aplicação
- **`config/`**: Configurações da aplicação, incluindo logs e outras configurações específicas
- **`docs/`**: Documentação do projeto, incluindo diagramas e imagens explicativas

## Executando localmente

Para executarmos o projeto localmente será necessário instalar o poetry

```
pipx install poetry
```

*Informações sobre a instalação podem ser consultados diretamente na documentação https://python-poetry.org/docs/*

Com o poetry instalado, podemos realizar a instalação das dependências do projeto


```
poetry install
```

Para executar o projeto, executamos o seguinte comando

```
poetry run uvicorn app:app --host 0.0.0.0 --port 8080 --log-config=log_conf.yaml
```

--host 0.0.0.0 -> Indica o host que o projeto será executado

--port 8080 -> Indica a porta que o projeto será executado

--log-config=log_conf.yaml -> Indica para a execução utilizar as configurações de log contidas no arquivo alvo.

