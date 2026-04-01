# Israel-Related MCP Servers

A curated list of Model Context Protocol (MCP) servers that provide access to Israeli data sources, government APIs, and services relevant to those living in or interested in Israel.

*Last updated: 2026-03-18*

## Table of Contents

<!-- INDEX_START -->

- [Economics & Statistics](#economics--statistics)
- [Finance & Banking](#finance--banking)
- [Government & Open Data](#government--open-data)
- [Government Services](#government-services)
- [Healthcare & Medical](#healthcare--medical)
- [Library & Archives](#library--archives)
- [Real Estate & Land](#real-estate--land)
- [Safety & Emergency](#safety--emergency)
- [Transportation](#transportation)
- [Weather & Environment](#weather--environment)

<!-- INDEX_END -->

# Economics & Statistics

Economic indicators, price indices, and statistical data

## [Israel Statistics MCP Server](https://github.com/reuvenaor/israel-statistics-mcp)

![GitHub stars](https://img.shields.io/github/stars/reuvenaor/israel-statistics-mcp?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/reuvenaor/israel-statistics-mcp)

Access to Israeli economic data from the Central Bureau of Statistics (CBS)

**Features:**
- Consumer Price Index (CPI) data
- Housing Market Index
- Producer Price Indices
- Construction materials, agriculture, transportation costs
- Price linkage calculator (inflation-adjusted values)
- Catalog browsing and topic navigation

**Data Sources:** Israeli Central Bureau of Statistics (CBS)

**Language:** Typescript

**Author:** [reuvenaor](https://github.com/reuvenaor)

---

# Finance & Banking

Banking transactions, financial analysis, and economic data

## [IL Bank MCP](https://github.com/glekner/il-bank-mcp)

![GitHub stars](https://img.shields.io/github/stars/glekner/il-bank-mcp?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/glekner/il-bank-mcp)

AI-powered financial analysis through automated Israeli bank scraping

**Features:**
- Transaction history retrieval
- Financial summary (income, expenses, trends)
- Transaction search
- Monthly credit summary
- Recurring charges identification
- Merchant spending analysis
- Data refresh across providers
- Local SQLite storage

**Data Sources:** Israeli banks via israeli-bank-scrapers

**Author:** [glekner](https://github.com/glekner)

---

## [GreenInvoice MCP](https://github.com/danielrosehill/GreenInvoice-MCP)

![GitHub stars](https://img.shields.io/github/stars/danielrosehill/GreenInvoice-MCP?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/danielrosehill/GreenInvoice-MCP)

MCP server for Israeli invoicing and accounting via the Green Invoice API

**Features:**
- Create, search, update, delete, close, send, and preview invoices, receipts, quotes
- Full client management (CRUD + search + document history)
- Product/service catalog management
- Payment link creation and status checking
- Webhook management
- Automatic JWT token management with caching and refresh
- Sandbox mode support for testing

**Data Sources:** Green Invoice API (greeninvoice.co.il)

**Language:** Typescript

**Author:** [danielrosehill](https://github.com/danielrosehill)

---

## [Israeli Bank MCP](https://github.com/mottibec/israeli-bank-mcp)

![GitHub stars](https://img.shields.io/github/stars/mottibec/israeli-bank-mcp?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/mottibec/israeli-bank-mcp)

MCP server for managing Israeli bank accounts and transactions

**Features:**
- Transaction fetching with customizable date ranges
- Bank listing with credential requirements
- Two-factor authentication handling
- Support for 17 Israeli financial institutions

**Data Sources:** Israeli banks via israeli-bank-scrapers library

**Language:** Typescript

**Author:** [mottibec](https://github.com/mottibec)

---

# Government & Open Data

Access to Israeli government datasets, budgets, and public information

## [Data.gov.il MCP Server](https://github.com/DavidOsherdiagnostica/data-gov-il-mcp)

![GitHub stars](https://img.shields.io/github/stars/DavidOsherdiagnostica/data-gov-il-mcp?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/DavidOsherdiagnostica/data-gov-il-mcp)

Advanced MCP server for accessing Israeli government open data through data.gov.il CKAN API

**Features:**
- Dataset search and discovery (Hebrew/English)
- Tag exploration by topic/category
- Dataset information retrieval
- Data record extraction and analysis
- Organization browsing
- Specialized analysis prompts (food/nutrition, environmental, real estate)

**Data Sources:** data.gov.il, Government ministries, Local authorities, Public companies

**Language:** Javascript

**Author:** [DavidOsherdiagnostica](https://github.com/DavidOsherdiagnostica)

---

## [Data Israel](https://github.com/LiorVainer/data-israel)

![GitHub stars](https://img.shields.io/github/stars/LiorVainer/data-israel?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/LiorVainer/data-israel)

AI agent network that connects to Israeli open data APIs (data.gov.il & CBS) — ask questions in Hebrew, get answers grounded in real data with charts and sources

**Features:**
- Hebrew language queries against Israeli open data
- data.gov.il API integration
- Central Bureau of Statistics (CBS) integration
- Chart and visualization generation
- Source-grounded answers

**Data Sources:** data.gov.il, Israeli Central Bureau of Statistics (CBS)

**Language:** Typescript

**Author:** [LiorVainer](https://github.com/LiorVainer)

---

## [DataGov Israel MCP Server](https://github.com/aviveldan/datagov-mcp)

![GitHub stars](https://img.shields.io/github/stars/aviveldan/datagov-mcp?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/aviveldan/datagov-mcp)

MCP server providing access to Israel's government public data platform (data.gov.il)

**Features:**
- Search and list government packages/datasets
- Retrieve organizational information and metadata
- Query resources with filtering and pagination
- Access datastore records with advanced search
- Fetch specific datasets by name

**Data Sources:** data.gov.il

**Author:** [aviveldan](https://github.com/aviveldan)

---

## [ILBudget MCP](https://github.com/david-aftergut/ILBudget-mcp)

![GitHub stars](https://img.shields.io/github/stars/david-aftergut/ILBudget-mcp?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/david-aftergut/ILBudget-mcp)

Access to Israeli government budget data

**Data Sources:** Israeli government budget

**Author:** [david-aftergut](https://github.com/david-aftergut)

---

## [Knesset MCP](https://github.com/zohar/knesset-mcp)

![GitHub stars](https://img.shields.io/github/stars/zohar/knesset-mcp?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/zohar/knesset-mcp)

Access to Israeli parliament (Knesset) data

**Data Sources:** Knesset

**Author:** [zohar](https://github.com/zohar)

---

# Government Services

Public services and administrative functions

## [Disabled Parking Permit MCP](https://github.com/MaorEi/disabled-parking-permit-mcp-server)

![GitHub stars](https://img.shields.io/github/stars/MaorEi/disabled-parking-permit-mcp-server?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/MaorEi/disabled-parking-permit-mcp-server)

Israeli disabled parking permit information

**Data Sources:** Israeli disabled parking permit database

**Author:** [MaorEi](https://github.com/MaorEi)

---

# Healthcare & Medical

Medical data, pharmaceuticals, and health services information

## [ILHealth MCP](https://github.com/david-aftergut/ILHealth-mcp)

![GitHub stars](https://img.shields.io/github/stars/david-aftergut/ILHealth-mcp?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/david-aftergut/ILHealth-mcp)

Access to Israeli Ministry of Health data dashboard

**Features:**
- Medical Services data
- Health Services Quality metrics
- War Casualties statistics
- Child Checkup and Development data
- Beach safety information
- Health Funds (Insurance) data

**Data Sources:** Israeli Ministry of Health dashboard

**Language:** Python

**Author:** [david-aftergut](https://github.com/david-aftergut)

---

## [Israel Drugs MCP Server](https://github.com/DavidOsherdiagnostica/israel-drugs-mcp-server)

![GitHub stars](https://img.shields.io/github/stars/DavidOsherdiagnostica/israel-drugs-mcp-server?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/DavidOsherdiagnostica/israel-drugs-mcp-server)

Comprehensive access to Israel's pharmaceutical database from the Ministry of Health

**Features:**
- Medication discovery by name
- Symptom-based treatment lookup
- Generic alternative exploration
- Visual drug verification with official images
- Therapeutic category browsing (1,172+ ATC categories)
- Health basket coverage and pricing
- Safety profiles and contraindications

**Data Sources:** Israel Ministry of Health pharmaceutical registry

**Author:** [DavidOsherdiagnostica](https://github.com/DavidOsherdiagnostica)

**Demo:** [https://github.com/DavidOsherdiagnostica/israel-drugs-mcp-server-demo](https://github.com/DavidOsherdiagnostica/israel-drugs-mcp-server-demo)

---

# Library & Archives

Library collections and archival data

## [NLI AI Search](https://github.com/mula2812/NLI_AI_Search)

![GitHub stars](https://img.shields.io/github/stars/mula2812/NLI_AI_Search?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/mula2812/NLI_AI_Search)

National Library of Israel AI-powered search

**Data Sources:** National Library of Israel

**Author:** [mula2812](https://github.com/mula2812)

---

# Real Estate & Land

Property data, land tenders, and real estate information

## [Nadlan MCP](https://github.com/nitzpo/nadlan-mcp)

![GitHub stars](https://img.shields.io/github/stars/nitzpo/nadlan-mcp?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/nitzpo/nadlan-mcp)

Israeli real estate data (Nadlan = Real Estate in Hebrew)

**Data Sources:** Israeli real estate sources

**Author:** [nitzpo](https://github.com/nitzpo)

---

## [Remy MCP (Israeli Land Authority)](https://github.com/barvhaim/remy-mcp)

![GitHub stars](https://img.shields.io/github/stars/barvhaim/remy-mcp?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/barvhaim/remy-mcp)

Access to Israeli Land Authority public tender data

**Features:**
- Tender search and filtering
- Detailed tender information retrieval
- Active tender listings
- Recent tender outcomes
- Geographic mapping data
- Settlement name-to-code conversion
- Hebrew language support

**Data Sources:** Israeli Land Authority (רשות מקרקעי ישראל)

**Language:** Python

**Author:** [barvhaim](https://github.com/barvhaim)

---

# Safety & Emergency

Public shelters, emergency services, and civil defense data

## [Miklat MCP](https://github.com/danielrosehill/Miklat-MCP)

![GitHub stars](https://img.shields.io/github/stars/danielrosehill/Miklat-MCP?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/danielrosehill/Miklat-MCP)

MCP server enabling AI agents to guide users towards miklatim tziburim (public shelters) in Israel

**Features:**
- Search shelters by free-text queries across names, addresses, and neighborhoods
- Locate nearest shelters using geographic coordinates
- Filter by shelter type, capacity, and accessibility
- Neighborhood breakdowns and statistical summaries
- Navigation links to Google Maps or Waze
- List all supported cities and individual shelter details

**Data Sources:** Miklat-MCP-Data repository, JLM-Shelters-Dot-Com project

**Language:** Typescript

**Author:** [danielrosehill](https://github.com/danielrosehill)

**Endpoint:** `https://mcp.jlmshelters.com/mcp`

*Currently covers Jerusalem with 198 shelters. Runs on Cloudflare Workers. Data licensed under ODbL.*

---

## [Miklat MCP Data](https://github.com/danielrosehill/Miklat-MCP-Data)

![GitHub stars](https://img.shields.io/github/stars/danielrosehill/Miklat-MCP-Data?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/danielrosehill/Miklat-MCP-Data)

Community-maintained geodata repository and data pipeline for Israeli public shelters, upstream data source for Miklat MCP

**Features:**
- Three-stage data validation pipeline (raw → structured → validated → production)
- GeoJSON standard format for shelter data
- Tracking system for 199 Israeli administrative areas
- Community contribution support for both human and AI agents

**Data Sources:** JLM-Shelters-Dot-Com project, Community contributions

**Language:** Geojson

**Author:** [danielrosehill](https://github.com/danielrosehill)

*Data pipeline companion to Miklat MCP. Currently populated with Jerusalem shelter data.*

---

# Transportation

Routing, transit, and transportation data

## [Routes MCP Israel](https://github.com/yoni-j/routes-mcp-israel)

![GitHub stars](https://img.shields.io/github/stars/yoni-j/routes-mcp-israel?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/yoni-j/routes-mcp-israel)

Israeli transportation and routing data

**Data Sources:** Israeli transportation systems

**Author:** [yoni-j](https://github.com/yoni-j)

---

# Weather & Environment

Meteorological data and environmental information

## [IMS MCP (Israeli Meteorological Service)](https://github.com/GuyKh/ims-mcp)

![GitHub stars](https://img.shields.io/github/stars/GuyKh/ims-mcp?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/GuyKh/ims-mcp)

Access to Israeli Meteorological Service data

**Data Sources:** Israeli Meteorological Service

**Author:** [GuyKh](https://github.com/GuyKh)

---

# Other Projects

Projects that need categorization.

## [Asher MCP](https://github.com/shlomiuziel/asher-mcp)

![GitHub stars](https://img.shields.io/github/stars/shlomiuziel/asher-mcp?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/shlomiuziel/asher-mcp)

Unknown purpose - requires investigation

**Author:** [shlomiuziel](https://github.com/shlomiuziel)

---

# MCP Authors

Alphabetical list of contributors who have created Israel-related MCP servers:

- [DavidOsherdiagnostica](https://github.com/DavidOsherdiagnostica)
- [GuyKh](https://github.com/GuyKh)
- [MaorEi](https://github.com/MaorEi)
- [aviveldan](https://github.com/aviveldan)
- [barvhaim](https://github.com/barvhaim)
- [danielrosehill](https://github.com/danielrosehill)
- [david-aftergut](https://github.com/david-aftergut)
- [glekner](https://github.com/glekner)
- [mottibec](https://github.com/mottibec)
- [mula2812](https://github.com/mula2812)
- [nitzpo](https://github.com/nitzpo)
- [reuvenaor](https://github.com/reuvenaor)
- [shlomiuziel](https://github.com/shlomiuziel)
- [yoni-j](https://github.com/yoni-j)
- [LiorVainer](https://github.com/LiorVainer)
- [zohar](https://github.com/zohar)

# Contributing

Anyone is welcome to open a pull request to add an Israel-related MCP server to this list.

To add a new project:
1. Fork this repository
2. Add your project to `projects.json` using the update script:
   ```bash
   ./update-projects.py --add https://github.com/username/repo --category category-name
   ```
3. Run the README generator:
   ```bash
   ./generate-readme.py
   ```
4. Submit a pull request

Alternatively, drop me a line at public@danielrosehill.com if you'd like me to add it manually.

# Disclaimer

This resource is intended for those discovering MCP servers relevant to Israel. It is not exhaustive and is maintained on a best-effort basis.

The inclusion of a project in this list does not constitute an endorsement. Users should evaluate each project independently for their specific use cases.

---

*Last updated: 2026-03-18*

Maintained by [Daniel Rosehill](https://github.com/danielrosehill)