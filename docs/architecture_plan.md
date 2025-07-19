# Arquitetura e Plano de Evolução

## Visão Geral

A aplicação, por mais que sua execução seja simples, foi planejada para atender uma quantidade alta de requisições com a maior disponibilidade possível. Desta forma, realizamos a criação de um endpoint responsável por realizar a leitura e escrita dos dados consumidos do website de livros, para que assim possamos utilizar esta chamada em Jobs agendados em horários específicos, buscando diminuir o impacto para os usuários.


## Estratégias de Escalabilidade

### 1. **Arquitetura de Dados Escalável**

#### Migração de Armazenamento

Para uma melhora da resiliência das consultas, será evoluído o ponto de armazenamento dos dados, alterando o armazenamento local de CSV por uma base estruturada como o PostgreSQL, adicionando em seguida uma camada de cache, para garantir a performance nas leituras para altas quantidades de requisições simultâneas. 


#### Estratégia de Dados
- **PostgreSQL**: Banco relacional para armazenamento dos dados recebidos do website
- **Redis**: Cache distribuído para alta performance nas consultas de leitura de livros, em caso de necessidade

## Evolução Técnica

Da forma como foram criados os arquivos de código, conseguimos facilmente realizar mudanças em nossos serviços, principalmente voltado para a base de dados que utilizamos. Adotando um padrão de arquivos repositórios, conseguimos ter um único ponto de entrada e saída quando falamos de leitura da base criada a partir do scrapping do site. Portanto, se em algum futuro quisermos trazer uma base mais robusta, não precisaremos alterar o restante do funcionamento atual de nossa aplicação.
 