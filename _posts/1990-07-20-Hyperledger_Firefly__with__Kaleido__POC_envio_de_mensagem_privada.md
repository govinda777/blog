# poc-instalacao-firefly-e-envio-de-mensagem-privada

Objetivo: 

Instalar o firefly cli, acessar as interfaces, realizar uma mensagem privada

## Como instalar : 

https://hyperledger.github.io/firefly/gettingstarted/firefly_cli.html

## Comandos para subir o ambiente firefly:

- ff init
- ff start dev
- ff logs dev

## Como acessar:

- Web UI: http://127.0.0.1:5000/ui
- Sandbox UI: http://127.0.0.1:5109
- Swagger: http://127.0.0.1:5000/api

## [PASSO 1] Criar um Datatype  

Data type é como se fosse um Documento, semelhante a um Documento No SQL

POST /api/v1/namespaces/{ns}/broadcast/datatype

{
  "name": "widget",
  "version": "0.0.2",
  "value": {
    "$id": "https://example.com/widget.schema.json",
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Widget",
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "description": "The unique identifier for the widget."
      },
      "name": {
        "type": "string",
        "description": "The person's last name."
      }
    }
  }
}

## [PASSO 2] Envio de mensagem publica

POST /api/v1/namespaces/default/send/message

{
  "header": {
    "tag": "new_widget_created",
    "topic": ["widget_id_12345"]
  },
  "group": {
    "members": [
      {
        "identity": "org_1"
      }
    ]
  },
  "data": [
    {
      "datatype": {
        "name": "widget",
        "version": "0.0.2"
      },
      "value": {
        "id": "widget_id_12345",
        "name": "superwidget"
      }
    }
  ]
}

## Links

Implementacao de token : https://www.youtube.com/watch?v=vKqQYJPvC2E&t=288s

Como funciona o Bitcoin : https://www.youtube.com/watch?v=NoZFWnHMZ48&ab_channel=Vis%C3%A3oLibert%C3%A1ria

Arquitetura P2P: https://www.youtube.com/watch?v=LiOZcck8dfU

P2Ps Escrow Service Work : https://www.binance.com/en/blog/all/how-does-binance-p2ps-escrow-service-work-421499824684900825

Link plataforma: https://www.kaleido.io/

Link de video mostrando como utilizar: https://www.youtube.com/watch?v=2XzxdlqN0ks&ab_channel=Kaleido

Documentação firefly: https://github.com/hyperledger/firefly

AML : https://www.sec.gov/about/offices/ocie/amlsourcetool.htm

Bitcoin Escrow Script: https://www.youtube.com/watch?v=hljavgPb6Yw

What is Escrow: https://www.youtube.com/watch?v=Xt5pUmeicqo

Escrow : https://www.youtube.com/watch?v=jBIfyVFMoHc

Smart Contract : https://www.youtube.com/watch?v=ooN6kZ9vqNQ

