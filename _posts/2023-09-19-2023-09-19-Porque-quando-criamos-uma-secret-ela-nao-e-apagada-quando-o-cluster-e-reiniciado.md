---
layout: post
title: Porque quando criamos uma secret ela não é apagada quando o cluster é reiniciado?
date: 2023-09-19
categories: Artigo
---

<p align="center">
<img src="{{ site.baseurl }}/images/2023-09-19-Porque-quando-criamos-uma-secret-ela-nao-e-apagada-quando-o-cluster-e-reiniciado.png" height="50%" width="50%" alt="Unform" />
</p>

**Introdução**

No ecossistema Kubernetes, a persistência e segurança dos dados são vitais. Uma das dúvidas frequentes é por que, após a reinicialização de um cluster, as `Secrets` permanecem intactas. Este artigo busca esclarecer essa questão, explorando o núcleo do Kubernetes: o etcd.

---

**O que é etcd**

O etcd é um armazenamento de chave-valor distribuído e consistente. Ele é usado pelo Kubernetes como seu armazenamento de dados de back-end, garantindo que todos os dados do cluster, incluindo `Secrets`, ConfigMaps e a atual configuração do cluster, sejam armazenados de forma segura e confiável.

---

**Como funciona a arquitetura do banco etcd e seu conceito de alta disponibilidade**

O etcd é construído com uma arquitetura de cluster, o que significa que ele pode ter vários nós. Isso não apenas fornece alta disponibilidade, mas também uma forte garantia de consistência de dados. Se um nó falhar, os outros nós continuarão a servir as solicitações, garantindo que o sistema permaneça disponível.

---

**Como são gerenciadas as Secrets de um cluster**

As `Secrets` são objetos que contêm pequenas quantidades de dados sensíveis, como senhas ou tokens. Quando criamos uma `Secret` no Kubernetes, ela é armazenada no etcd. Isso significa que, a menos que o etcd seja apagado ou corrompido, a `Secret` permanecerá intacta, mesmo após reinicializações do cluster.

---

**Como fazer um Backup/Restore do etcd**

1. **Backup**: Use o comando `etcdctl snapshot save` para criar um snapshot do etcd.
2. **Restauração**: Em caso de falha do etcd, use o comando `etcdctl snapshot restore` para restaurar o etcd a partir de um snapshot.

Lembre-se de armazenar seus backups em um local seguro e de fazer backups regularmente.

---

**Erros que geralmente são cometidos na configuração do cluster**

* **Não fazer backups regulares do etcd**: Isso pode levar à perda de dados em caso de falha do etcd.
* **Permissões inadequadas**: Dar a usuários ou aplicativos mais permissões do que o necessário pode levar a alterações indesejadas.
* **Configurações temporárias**: Algumas configurações, se não persistidas corretamente, podem ser perdidas após a reinicialização de um componente. Por exemplo, se você configurar algo diretamente em um Pod ou em um contêiner sem atualizar a definição do Deployment ou StatefulSet, essa configuração será perdida quando o Pod for reiniciado. Outro exemplo comum é a configuração de variáveis de ambiente diretamente em contêineres sem usar ConfigMaps ou Secrets, o que pode resultar em perda de configuração após reinicializações.

---

**Conclusão**

A persistência e segurança das `Secrets` e outros objetos em um cluster Kubernetes são garantidas pelo etcd. Compreender como o etcd funciona e como gerenciar corretamente seus dados é crucial para manter um cluster Kubernetes saudável e seguro.

---

**Referências**

1. [Documentação oficial do Kubernetes](https://kubernetes.io/docs/)
2. [Documentação oficial do etcd](https://etcd.io/docs/)

---

**Glossário**

* **etcd**: Armazenamento de chave-valor distribuído usado pelo Kubernetes.
* **Secret**: Objeto Kubernetes usado para armazenar informações sensíveis.
* **Cluster**: Conjunto de máquinas que executam os componentes do Kubernetes e suas cargas de trabalho.

---