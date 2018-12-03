# Test Python REST APP

### Como rodar?

1. Você precisará do `Docker` e do `Docker Compose` instalados em sua máquina.
2. Após instalar o `Docker` e o `Docker Compose` entre na raiz da aplicação e execute o comando
```docker-compose up -d --build```.

Feito isso a aplicação deve subir normalmente seus conteiners e estará pronta para executar as Migrations. Para rodar as migrations, execute os comandos:

``` docker exec pdv-python flask db init ```

``` docker exec pdv-python flask db migrate ```

``` docker exec pdv-python flask db upgrade ```


### Rotas

As rotas que a aplicaço possui são:

1. ```[GET] /```  - raiz da aplicação. Rota que lista todos os registros (Pontos de Venda) do banco.
2. ```[GET] /<id> ``` - ao passar o parametro ```<id>``` contendo o id de algum ponto de venda no banco, a rota retornará um registro único (o ponto de venda correspondente ao id) 
3. ```[GET] /location/<long>/<lat>``` - recebe os parametros ```long``` e ```lat``` que correspondem a Longitude e Latitude de um ponto de venda. Retorna todos os registros encontrados com os parametros passados
4. ```[POST] /new ``` - recebe um JSON (exemplo abaixo) via POST e insere no banco o ponto de venda, retornando os IDS dos pontos de venda inseridos.

Todas as rotas retornam a resposta em JSON

#### JSON Exemplo de retorno
```
{
  pdvs: [ 
     {
          "id": 1, 
          "tradingName": "PDV Test",
          "ownerName": "Owner Fulano",
          "document": "1234567891011/0001",
          "coverageArea": { 
            "type": "MultiPolygon", 
            "coordinates": [
              [[[0, 0], [0, 0], [0, 0], [0, 0]]], 
              [[[0, 0], [0, 0], [0, 0], [0, 0], [0,0]]]
            ]
          }, //Área de Cobertura
          "address": { 
            "type": "Point",
            "coordinates": [-46.57421, -21.785741]
          },
      }
    ]
  }
  ``` 
  
#### JSON Exemplo para Inserção
```
[ 
    {
        "tradingName": "PDV Test",
        "ownerName": "Owner Fulano",
        "document": "1234567891011/0001",
        "coverageArea": { 
          "type": "MultiPolygon", 
          "coordinates": [
            [[[0, 0], [0, 0], [0, 0], [0, 0]]], 
            [[[0, 0], [0, 0], [0, 0], [0, 0], [0,0]]]
          ]
        }, //Área de Cobertura
        "address": { 
          "type": "Point",
          "coordinates": [-46.57421, -21.785741]
        },
    }
  ]
  ``` 
