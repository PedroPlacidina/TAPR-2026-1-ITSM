# 📊 CorpTech ITSM Analytics

<p align="center">
  <b>Pipeline de Dados em Nuvem para Análise de ITSM</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Azure-Cloud-blue?logo=microsoftazure">
  <img src="https://img.shields.io/badge/Python-ETL-yellow?logo=python">
  <img src="https://img.shields.io/badge/PowerBI-Dashboard-F2C811?logo=powerbi">
  <img src="https://img.shields.io/badge/Status-AV1%20Concluída-success">
</p>

---

## 📚 Informações Acadêmicas

- **Disciplina:** TAPR — Tópicos Avançados em Programação  

### 👥 Equipe
- Fellipe Negherbon Prim  
- Lucas Felipe Jacintho  
- Pedro Henrique Placidina Maria  

---

## 📌 Descrição do Projeto

Este projeto tem como objetivo construir uma **pipeline de dados em nuvem** para análise de métricas de **ITSM (IT Service Management)** da empresa fictícia **CorpTech**.

A solução contempla:

- 📥 Extração de dados de uma base SQL (simulação do JSM)  
- ⚙️ Transformação e processamento (ETL)  
- 🗄️ Armazenamento em Data Lake  
- 🧠 Carga em banco analítico  
- 📊 Visualização em dashboards interativos  

> 🎯 **Foco da AV1:** Arquitetura, escolha tecnológica e provisionamento na nuvem.

---

## 🧱 Arquitetura da Solução

A pipeline segue uma arquitetura moderna baseada em serviços da Azure:
Azure SQL (Origem)
↓
Azure Functions (ETL)
↓
Azure Blob Storage (Raw)
↓
Azure SQL (Analítico)
↓
Power BI (Visualização)


### 📷 Diagrama

📁 `/docs/arquitetura.png`

---

## 🔄 Fluxo de Dados

### 📥 Origem — Azure SQL (Mockado)
- Simulação do sistema de ITSM (JSM)

### ⚙️ Processamento — Azure Functions
- Execução via **Timer Trigger**
- Linguagem: **Python**
- Processo de **ETL**

### 🗄️ Armazenamento Raw — Azure Blob Storage
- Formatos: **JSON / CSV**
- Função: **Data Lake (zona de pouso)**

### 🧠 Destino Analítico — Azure SQL Database
- Dados tratados e estruturados
- Base para análise

### 📊 Visualização — Power BI
- Dashboards interativos
- Consumo pelos usuários

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|----------|--------|
| ☁️ Azure | Plataforma de nuvem |
| ⚡ Azure Functions | Processamento serverless (ETL) |
| 🗄️ Blob Storage | Armazenamento de dados brutos |
| 🧠 Azure SQL Database | Banco analítico |
| 🐍 Python | Processamento |
| 📊 Power BI | Visualização |
| 🐙 GitHub | Versionamento |

---

## 📂 Estrutura do Repositório

src/ → Código da aplicação (ETL)
docs/ → Documentação e diagramas
infra/ → Configurações de infraestrutura


### 📌 Arquivos Importantes

- `README.md` → Documentação principal  
- `docs/justificativa-tecnologica.md` → Justificativa técnica  
- `docs/arquitetura.png` → Diagrama  
- `docs/prints-azure/` → Evidências  

---

## ☁️ Provisionamento na Azure

### ✅ Recursos Criados

**Resource Group**

rg-corptech-itsm-2026


**Azure Function App**
- Runtime: Python  
- Plano: Consumption  

📷 Evidências:

docs/prints-azure/


---

## 📚 Justificativa Tecnológica

As escolhas foram baseadas em:

- 💰 Eficiência de custo (serverless)
- 📈 Escalabilidade automática
- 🔧 Facilidade de manutenção
- 🎯 Aderência ao cenário

📄 Documento:

docs/justificativa-tecnologica.md


### 🔍 Serviços Utilizados

| Serviço | Função |
|--------|--------|
| Azure Functions | ETL serverless |
| Azure Blob Storage | Data Lake |
| Azure SQL Database | Banco analítico |
| Power BI | Dashboards |

---

## 🎯 Objetivo da Atividade (AV1)

- ✔ Compreender a arquitetura  
- ✔ Justificar escolhas tecnológicas  
- ✔ Modelar pipeline  
- ✔ Provisionar recursos  

---

## ✅ Critérios Atendidos

- ✔ Estrutura organizada  
- ✔ README documentado  
- ✔ Justificativa tecnológica  
- ✔ Diagrama arquitetural  
- ✔ Provisionamento inicial  

---

## 🚀 Próximos Passos (AV2)

- 🔧 Implementar Azure Function  
- 🔄 Automatizar pipeline  
- 🧠 Criar modelo analítico  
- 📊 Desenvolver dashboards  

---

## 📎 Referências

- https://learn.microsoft.com/pt-br/azure/azure-functions/functions-overview  
- https://learn.microsoft.com/pt-br/azure/storage/blobs/storage-blobs-introduction  
- https://learn.microsoft.com/pt-br/azure/azure-sql/database/sql-database-paas-overview  
- https://learn.microsoft.com/pt-br/power-bi/fundamentals/power-bi-overview  
