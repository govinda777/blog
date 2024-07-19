---
layout: post
title: 2024-07-19-Projeto--Robo-de-Entrega-Autonomo-Controlado-por-IA
date: 2024-07-19
categories: Projeto
---

<p align="center">
<img src="{{ site.baseurl }}/images/2024-07-19-Projeto--Robo-de-Entrega-Autonomo-Controlado-por-IA.webp" 
height="50%" width="50%" alt="Unform" />
</p>

Project in youtube : https://youtu.be/UVTwoqWhvHE?si=gVg90N9N7JeZnUpl



### Projeto: Robo de Entrega Autônomo Controlado por IA

**Descrição do Projeto:**
Este projeto visa criar um robô autônomo de entrega que se move do ponto A ao ponto B utilizando tecnologia de Inteligência Artificial. O robô será equipado com uma câmera e será controlado remotamente através de uma rede Wi-Fi. O sistema de pagamento será baseado em Bitcoin, utilizando a Lightning Network.

---

### Robo - Hardware

#### Arquitetura do Robo
- **Motores:** O robô possui dois motores amarelos clássicos que permitem movimentos para frente e para trás.
- **Rodinha Giratória:** Facilita manobras e giros no próprio eixo.
- **Conectores:** Utiliza um conector específico para integrar os motores e a alimentação.

#### Montagem
- **Estrutura Simples:** A montagem do robô é básica e acessível para iniciantes, com componentes facilmente montáveis.
- **Componentes:** Seis pilhas conectadas a um driver que alimenta os motores do robô.

#### Blindagem
- **Proteção dos Componentes:** Blindagem básica para proteger os componentes eletrônicos do robô durante o movimento e em diferentes ambientes.

#### Bateria
- **Alimentação:** O robô é alimentado por seis pilhas AA, conectadas para fornecer energia contínua aos motores e componentes eletrônicos.

#### Camera
- **Integração:** Câmera instalada no robô para reconhecimento e seguimento de objetos.
- **Controle Remoto:** A câmera permite controle remoto via Wi-Fi, facilitando a navegação autônoma.

#### Velocidade
- **Ajuste de Velocidade:** A velocidade do robô pode ser ajustada dinamicamente através de comandos específicos, permitindo operações em diferentes cenários.

---

### Robo - Software

#### Controle (Impossível Robo 100% Autônomo)
Por se tratar de um robô autônomo, ele não pode ser controlado diretamente por uma pessoa. O robô apenas recebe uma transação em criptomoeda para se mover do ponto A ao ponto B em uma localidade. Assim, um ser humano não controla o robô, mas ele recebe tarefas e as cobra em criptomoeda.

#### Como o Robo Irá Identificar Coisas a Partir da IA?
- **Reconhecimento de Objetos:** Utiliza uma câmera e algoritmos de visão computacional para identificar e seguir objetos.
- **Processamento de Imagens:** Python será utilizado para processar as imagens capturadas pela câmera e tomar decisões baseadas nas informações visuais.

#### Como o Robo Irá Traçar a Rota do Ponto A ao Ponto B?
- **Mapeamento e Navegação:** Algoritmos de navegação autônoma traçam a rota do ponto de origem ao destino utilizando dados de GPS e outros sensores.
- **Planejamento de Rota:** O software determina a rota mais eficiente e segura para o robô seguir, evitando obstáculos e ajustando conforme necessário.

#### Como o Robo Identifica uma Nova Transação para Iniciar a Coleta e Entrega?
- **Detecção de Transações:** O robô monitora continuamente a rede Lightning Network para identificar novas transações associadas ao seu endereço de pagamento.
- **Início da Tarefa:** Ao detectar uma transação válida, o robô inicia a tarefa de coleta e entrega conforme as instruções recebidas.

##### Carteira
- **Integração com Carteira Digital:** O robô está integrado a uma carteira digital que permite receber pagamentos em Bitcoin via Lightning Network.

##### Rede - Lightning Network
- **Transações Rápidas e Seguras:** Utilização da Lightning Network para garantir transações rápidas e de baixo custo.

##### Política de Reembolso
- **Reembolsos:** Em caso de falha na entrega, o robô retorna ao ponto de coleta. Se a carga for extraviada, será reembolsado 70% do valor da transação.

#### O que Acontece Quando a Entrega Não é Realizada?
- **Retorno ao Ponto de Coleta:** O robô retorna ao ponto de coleta original.
- **Reembolso:** Em caso de extravio da carga, o cliente será reembolsado com 70% do valor da transação efetuada.
