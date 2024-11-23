---
layout: post
title: 2024-10-31-Plano-de-Estudos-para-Primeiro-Emprego-em-Desenvolvimento-de-Software
date: 2024-10-31
categories: Artigo
---

<p align="center">
<img src="{{ site.baseurl }}/images/2024-10-31-Plano-de-Estudos-para-Primeiro-Emprego-em-Desenvolvimento-de-Software.webp" 
height="50%" width="50%" alt="Unform" />
</p>  

# Implementação e Teoria de Subscriptions em GraphQL

## Introdução

Subscriptions são um dos três tipos principais de operações em GraphQL, junto com Queries e Mutations. Elas permitem estabelecer uma conexão em tempo real entre cliente e servidor, possibilitando que o servidor envie atualizações para o cliente quando eventos específicos ocorrem.

## Fundamentos Teóricos

### Como Funcionam as Subscriptions

1. **Estabelecimento de Conexão**
   - Utiliza protocolo WebSocket para manter uma conexão persistente
   - Implementa o protocolo GraphQL over WebSocket
   - Mantém um estado de conexão bidirecional

2. **Modelo de Eventos**
   - Baseado no padrão Publish/Subscribe
   - O servidor publica eventos
   - Clientes inscritos recebem atualizações automaticamente

3. **Fluxo de Dados**
   - Cliente se inscreve em um evento específico
   - Servidor monitora eventos
   - Quando um evento ocorre, todos os clientes inscritos são notificados

## Implementação Prática

### 1. Definição do Schema

```graphql
type Subscription {
  messageAdded: Message
  userStatusChanged: UserStatus
  notificationReceived: Notification
}

type Message {
  id: ID!
  content: String!
  sender: User!
  timestamp: String!
}

type UserStatus {
  userId: ID!
  status: String!
  lastSeen: String!
}

type Notification {
  id: ID!
  type: String!
  message: String!
}
```

### 2. Configuração do Servidor

```javascript
import { createServer } from 'http';
import { ApolloServer } from 'apollo-server-express';
import { WebSocketServer } from 'ws';
import { useServer } from 'graphql-ws/lib/use/ws';
import { makeExecutableSchema } from '@graphql-tools/schema';
import express from 'express';

// Criação do schema executável
const schema = makeExecutableSchema({
  typeDefs,
  resolvers,
});

// Configuração do servidor Express
const app = express();
const httpServer = createServer(app);

// Configuração do Apollo Server
const apolloServer = new ApolloServer({
  schema,
  plugins: [{
    async serverWillStart() {
      return {
        async drainServer() {
          wsServer.close();
        },
      };
    },
  }],
});

// Configuração do WebSocket Server
const wsServer = new WebSocketServer({
  server: httpServer,
  path: '/graphql',
});

// Configuração do Subscription Server
useServer(
  {
    schema,
    context: (ctx) => {
      // Contexto personalizado para subscriptions
      return {
        ...ctx,
        pubsub,
      };
    },
  },
  wsServer
);
```

### 3. Implementação dos Resolvers

```javascript
import { PubSub } from 'graphql-subscriptions';

const pubsub = new PubSub();

const resolvers = {
  Subscription: {
    messageAdded: {
      subscribe: () => pubsub.asyncIterator(['MESSAGE_ADDED']),
      resolve: (payload) => {
        return payload;
      },
    },
    
    userStatusChanged: {
      subscribe: () => pubsub.asyncIterator(['USER_STATUS_CHANGED']),
      resolve: (payload) => {
        return payload;
      },
    },
    
    notificationReceived: {
      subscribe: () => pubsub.asyncIterator(['NOTIFICATION_RECEIVED']),
      resolve: (payload) => {
        return payload;
      },
    },
  },
  
  Mutation: {
    addMessage: async (_, { content, senderId }, { dataSources }) => {
      const message = await dataSources.messages.create({
        content,
        senderId,
        timestamp: new Date().toISOString(),
      });
      
      pubsub.publish('MESSAGE_ADDED', {
        messageAdded: message,
      });
      
      return message;
    },
  },
};
```

### 4. Implementação do Cliente

```javascript
import { ApolloClient, InMemoryCache, split, HttpLink } from '@apollo/client';
import { getMainDefinition } from '@apollo/client/utilities';
import { GraphQLWsLink } from '@apollo/client/link/subscriptions';
import { createClient } from 'graphql-ws';

// Configuração do WebSocket Link
const wsLink = new GraphQLWsLink(
  createClient({
    url: 'ws://localhost:4000/graphql',
  })
);

// Configuração do HTTP Link
const httpLink = new HttpLink({
  uri: 'http://localhost:4000/graphql'
});

// Split links para queries/mutations e subscriptions
const splitLink = split(
  ({ query }) => {
    const definition = getMainDefinition(query);
    return (
      definition.kind === 'OperationDefinition' &&
      definition.operation === 'subscription'
    );
  },
  wsLink,
  httpLink
);

// Criação do cliente Apollo
const client = new ApolloClient({
  link: splitLink,
  cache: new InMemoryCache(),
});
```

### 5. Uso das Subscriptions no Cliente

```javascript
import { gql, useSubscription } from '@apollo/client';

const MESSAGE_SUBSCRIPTION = gql`
  subscription OnMessageAdded {
    messageAdded {
      id
      content
      sender {
        id
        name
      }
      timestamp
    }
  }
`;

function ChatRoom() {
  const { data, loading, error } = useSubscription(MESSAGE_SUBSCRIPTION);

  if (loading) return <p>Carregando...</p>;
  if (error) return <p>Erro: {error.message}</p>;

  return (
    <div>
      <h2>Nova Mensagem:</h2>
      {data && (
        <div>
          <p>{data.messageAdded.content}</p>
          <small>
            Enviado por: {data.messageAdded.sender.name} às{' '}
            {new Date(data.messageAdded.timestamp).toLocaleTimeString()}
          </small>
        </div>
      )}
    </div>
  );
}
```

## Boas Práticas e Considerações

1. **Gerenciamento de Conexões**
   - Implementar reconexão automática
   - Limitar número máximo de conexões por cliente
   - Implementar timeout para conexões inativas

2. **Segurança**
   - Autenticar conexões WebSocket
   - Validar permissões antes de permitir subscrições
   - Implementar rate limiting

3. **Performance**
   - Utilizar filtros para reduzir dados desnecessários
   - Implementar batch processing para eventos frequentes
   - Considerar cleanup de subscrições não utilizadas

4. **Escalabilidade**
   - Usar PubSub externos (Redis, RabbitMQ) para ambientes distribuídos
   - Implementar mecanismos de fallback
   - Monitorar uso de recursos

## Conclusão

Subscriptions são uma ferramenta poderosa do GraphQL para implementar funcionalidades em tempo real. Com a configuração adequada e seguindo as boas práticas, é possível criar aplicações robustas e escaláveis que oferecem uma excelente experiência ao usuário.

## Referências

1. [GraphQL Subscriptions Specification](https://spec.graphql.org/draft/#sec-Subscription)
2. [Apollo GraphQL Subscriptions](https://www.apollographql.com/docs/react/data/subscriptions/)
3. [GraphQL over WebSocket Protocol](https://github.com/apollographql/subscriptions-transport-ws/blob/master/PROTOCOL.md)