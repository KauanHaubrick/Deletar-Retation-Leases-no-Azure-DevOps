# Azure DevOps – Retention Leases Cleaner

Script em **Python** para remover **retention leases** de builds no Azure DevOps, permitindo a exclusão de pipelines que ficam bloqueadas por retenções antigas.

## 📌 Contexto

Ao tentar excluir uma pipeline no Azure DevOps, é comum receber o erro:

> *One or more builds associated with the requested pipeline(s) are retained by a release.*

Isso acontece porque algumas runs possuem **retention leases** ativos.  
A interface do Azure DevOps **não permite remover essas leases em massa**, tornando o processo manual e demorado.

Este script automatiza essa limpeza usando a **Azure DevOps REST API**.

---

## ⚠️ Importante (leia antes de usar)

- ✅ O script **remove apenas retention leases**
- 🚨 Use com cuidado em ambientes produtivos

---

## 🛠️ Pré-requisitos

- Python **3.9+**
- Biblioteca `requests`
- Personal Access Token (PAT) do Azure DevOps

---
⚙️ Configuração

No script, ajuste as variáveis:

AZURE_DEVOPS_PAT = "SEU_PAT_AQUI"

ORG = "SuaOrganizacao"
PROJECT = "SeuProjeto"
PIPELINE_ID = 00


🔍 Como descobrir o Pipeline ID

Abra a pipeline no Azure DevOps e observe a URL:

https://dev.azure.com/org/project/_build?definitionId=23
