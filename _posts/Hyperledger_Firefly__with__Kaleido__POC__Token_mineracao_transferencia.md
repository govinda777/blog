<img src="{{ site.baseurl }}/images/Hyperledger_Firefly__with__Kaleido__POC__Token_mineracao_transferencia.jpeg" height="50%" width="50%" alt="Unform" />

# Hyperledger Firefly [Tutorial] Token / mineracao / transferência 

Objetivo: 

* [X] - Instalar o firefly cli
* [X] - Acessar as interfaces
* [X] - Criar um Token chamado GOV (cripto moeda)
* [X] - Realizar uma transferencia de Tokens para outra Organização ^["Definição_de_organizações_em_uma_block_chain"]("Definição_de_organizações_em_uma_block_chain")
* [X] - Realiza uma analise de Auditoria para ver se os saldos estão corretos e se as taxas foram cobradas corretamente.

## Instalar o firefly cli : 

https://hyperledger.github.io/firefly/gettingstarted/firefly_cli.html

## Acessar as interfaces

### Comandos para subir o ambiente firefly:

- ff init
- ff start dev
- ff logs dev

### Como acessar:

- Web UI: http://127.0.0.1:5000/ui

![]({{ site.baseurl }}/images/firefly06.jpeg)

- Sandbox UI: http://127.0.0.1:5109

![]({{ site.baseurl }}/images/firefly07.jpeg)

- Swagger: http://127.0.0.1:5000/api

![]({{ site.baseurl }}/images/firefly08.jpeg)

## Realizar a transferencia de Tokens para outra Organização

### [PASSO 1] Criação de um pool (criar as suas moedinhas)

POST /namespaces/{ns}/tokens/pools

```py
{
  "name": "testpool",
  "type": "fungible"
}
```
Response

```py
{
  "id": "ff20caf0-fa1f-4516-9d6e-1f0989e33c39",
  "type": "fungible",
  "namespace": "default",
  "name": "testpool",
  "key": "0x27b2351e15b0c3a06a9489d448a2b1ad56115de9",
  "connector": "erc20_erc721",
  "tx": {
    "type": "token_pool",
    "id": "315d6f61-059a-4bf8-a8dd-55738aa64d9c"
  }
}

curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/namespaces/default/tokens/pools' \
  -H 'accept: application/json' \
  -H 'Request-Timeout: 120s' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "testpool",
  "type": "fungible"
}'
```

### [PASSO 2] Get the address of the deployed contract 

GET http://127.0.0.1:5000/api/v1/namespaces/default/tokens/pools/ff20caf0-fa1f-4516-9d6e-1f0989e33c39

### [PASSO 3] Minerar token (Mint tokens )

POST http://127.0.0.1:5000/api/v1/namespaces/default/tokens/mint

```py
{
  "amount": "100000000000000000000"
}

curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/namespaces/default/tokens/mint' \
  -H 'accept: application/json' \
  -H 'Request-Timeout: 120s' \
  -H 'Content-Type: application/json' \
  -d '{
  "amount": "100000000000000000000"
}'
```
	
Response body

```py
{
  "type": "mint",
  "localId": "6a58bb93-d32e-4809-81a6-a561063ad032",
  "pool": "ff20caf0-fa1f-4516-9d6e-1f0989e33c39",
  "connector": "erc20_erc721",
  "key": "0x27b2351e15b0c3a06a9489d448a2b1ad56115de9",
  "from": "0x27b2351e15b0c3a06a9489d448a2b1ad56115de9",
  "to": "0x27b2351e15b0c3a06a9489d448a2b1ad56115de9",
  "amount": "100000000000000000000",
  "tx": {
    "type": "token_transfer",
    "id": "5d32e625-12ad-4564-9c72-a178378d4ede"
  }
}
```

### [PASSO 4] Transfer tokens 

POST /namespaces/{ns}/tokens/transfers

```py
{
  "amount": "54",
  "to": "0x7de83f01f1c27c17c2fd1fcf8387b1279291bee6"
}
```

##ATENÇÃO : Colocar ethereum_address para a org que vc quer transferir o token

```py
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/namespaces/default/tokens/transfers' \
  -H 'accept: application/json' \
  -H 'Request-Timeout: 120s' \
  -H 'Content-Type: application/json' \
  -d '{
  "amount": "54",
  "to": "0x7de83f01f1c27c17c2fd1fcf8387b1279291bee6"
}'
```
	
Response body

```py
{
  "type": "transfer",
  "localId": "3b915f51-bd22-4e2d-b543-8c19ea82d967",
  "pool": "ff20caf0-fa1f-4516-9d6e-1f0989e33c39",
  "connector": "erc20_erc721",
  "key": "0x27b2351e15b0c3a06a9489d448a2b1ad56115de9",
  "from": "0x27b2351e15b0c3a06a9489d448a2b1ad56115de9",
  "to": "0x7de83f01f1c27c17c2fd1fcf8387b1279291bee6",
  "amount": "54",
  "tx": {
    "type": "token_transfer",
    "id": "330ea161-4b4f-4287-be42-d45aede6419d"
  }
}
```

## Links

Building we3 app : https://www.youtube.com/watch?v=oWs6NuOE9uM

Implementacao de token : https://www.youtube.com/watch?v=vKqQYJPvC2E&t=288s

Documentação de implementação do token : https://hyperledger.github.io/firefly/tutorials/tokens/erc20.html

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

