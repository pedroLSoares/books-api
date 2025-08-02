# Arquitetura - Books API

Este documento detalha o pipeline completo de dados da Books API, desde a ingestão dos dados do website até o consumo final pelos usuários.

## Arquitetura utilizada no projeto

Atualmente o sistema conta com o seguinte design de infraestrutura, contato com o csv local para armazenamento de dados e endpoints REST para atualização dos dados e informações armazenadas.

![arquitetura](img/architecture_system.png)

O design e arquitetura dos arquivos foram pensadas em possíveis evoluções de nosso sistemas, buscando trazer uma simplicidade em mudanças de infraestrutura ou serviços externos

## Visão Geral do Pipeline de processamento

O pipeline de dados da Books API é composto por 4 etapas principais:

1. **Ingestão e Processamento**: Extração de dados do website books.toscrape.com já realizando a transformação necessária dos dados
2. **API**: Disponibilização dos dados via endpoints REST

![arquitetura](img/processing_pipeline.png)

## Etapas Detalhadas do Pipeline

### 1. Ingestão de Dados 🔍

Disponibilizamos um endpoint que aciona o script de raspagem de dados do site configurado, este script retorna todos os dados encontrados nas páginas e realizando a formatação e processamento de dados.

**Preço do livro:** Realizamos a conversão do preço de string separando em dois campos

- price: Irá conter o valor do livro
- currency: Irá armazenar a moeda do valor do Livro.

**Nota do livro:** A nota no site é retornada como um texto nominal do número, realizamos a conversão para um inteiro.

com os dados já formatados salvamos os resultados em um arquivo CSV local.


#### Exemplo de dado salvo

```json
{
  "title": "A Light in the Attic",
  "price": 51.77,
  "currency": "£",
  "rating": 3,
  "category": "Poetry",
  "image_url": "media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"
}
```

### 2. API REST

Para a consulta dos dados resgatados, disponibilizamos uma série de endpoints REST para consumo.

Todos os endpoints também estão disponíveis na documentação do swagger que podem ser encontradas no endpoint /docs

## Sistema de Autenticação e Armazenamento de Usuários

### Banco de Dados

O sistema utiliza **PostgreSQL** como banco de dados principal para armazenamento persistente dos dados de usuários.

### Segurança de Senhas

O sistema implementa as seguintes medidas de segurança para senhas:

- **Criptografia bcrypt**: Todas as senhas são armazenadas utilizando hash bcrypt

### Sistema de Autenticação JWT

O sistema conta com o uso de tokens JWT para autenticação em endpoints privados. Atualmente geramos tanto o token JWT quanto o token de refresh, utilizado para gerar um novo token quando o primeiro expirar. 

A expiração de um token JWT está configurada em 30 minutos, enquanto o de refresh tem uma validade de 30 dias.

### Fluxo de Autenticação

1. **Registro**: Usuário fornece name, email e password → Sistema valida dados → Senha é criptografada → Usuário salvo no banco
2. **Login**: Usuário fornece email e password → Sistema verifica credenciais → Gera access_token e refresh_token
3. **Acesso a rotas protegidas**: Cliente envia access_token no header Authorization → Sistema valida token → Acesso liberado
4. **Renovação**: Cliente envia refresh_token → Sistema valida → Gera novo access_token

### Middleware de Autenticação

As rotas protegidas utilizam middleware personalizado (`JWTBearer`) que:

- Intercepta requisições para endpoints protegidos
- Valida formato e assinatura do token JWT
- Verifica expiração do token
- Retorna erro 401 para tokens inválidos ou expirados

## Evolução 

- **[Plano de Arquitetura](architecture_plan.md)** - Arquitetura detalhada e roadmap de evolução
