# Integrando com Machine Learning

## Visão Geral

A Books API foi projetada especificamente para servir como uma fonte de dados estruturada para cientistas de dados e engenheiros de machine learning. Nossa API fornece dados limpos, normalizados e prontos para análise, eliminando a necessidade de scraping manual ou processamento complexo de dados.

## Como utilizar a API

Ao iniciar a aplicação já é realizada uma inserção inicial dos dados na base CSV local, porém também é disponibilizado um endpoint para caso seja necessário realizar alguma atualização da base

```
POST /api/v1/jobs/scrape
```

Com os dados já processados, os endpoints de consultas já ficam disponíveis que poderão ser utilizados para o treinamento de modelos. Os resultados já possuem os dados tratados para melhor consumo.

## Dados Disponíveis

A API fornece informações estruturadas sobre livros com os seguintes campos:
- **title**: Título do livro
- **price**: Preço em formato numérico
- **currency**: Moeda (£)
- **rating**: Avaliação de 1 a 5
- **category**: Categoria do livro
- **image**: URL da imagem do livro
