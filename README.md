# Israeli AI Ecosystem

![Banner](images/banner.png)

A curated map of the Israeli AI ecosystem: AI agents, agent skills, MCP servers, Hebrew language resources, communities, meetups, government bodies, conferences, and domain-specific tools — covering finance, healthcare, government data, real estate, safety, and more.

Projects are presented as compact tables; ecosystem and community sections use grouped lists. See [SCOPE.md](SCOPE.md) for inclusion criteria and [pending.md](pending.md) for planned sections awaiting entries.

> **Note:** This repo is **not** intended to be a collection of every AI company in Israel — that would be an impossible task, and not particularly useful. Rather, it's a thoughtful organisation of links outlining useful directions for those professionally involved in AI in Israel to find community, organisations, and practical tools.

*Last updated: 2026-04-09*

## Contents

<table>
<tr>
<td valign="top" width="25%">

### 🤖 Projects

- [AI Agents](#ai-agents)
- [Agent Skills →](agent-skills.md)
- [MCP Servers →](mcps.md)
- [Skills & Frameworks](#agent-skills--frameworks)
- [Curated Lists](#curated-lists)

</td>
<td valign="top" width="25%">

### 🌐 Ecosystem

- [Communities](#communities--organizations)
- [Government Bodies](#government-bodies)
- [Centers of Excellence](#centers-of-excellence)
- [Conferences](#conferences--events)
- [Inference Providers](#inference-providers--local-clouds)
- [Startups](#startup-ecosystem)

</td>
<td valign="top" width="25%">

### 🇮🇱 Hebrew & Language

- [Overview](#hebrew-language-resources)
- [Hebrew AI Models](https://github.com/danielrosehill/Hebrew-AI-Models)
- [Hebrew Language Projects Index](https://github.com/danielrosehill/Hebrew-Language-Projects-Index)
- [Hebrew TTS Providers](https://github.com/danielrosehill/Hebrew-TTS-Providers)
- [English ↔ Hebrew Translation](https://github.com/danielrosehill/English-Hebrew-Translation)
- [Hebrew Calendar Resources](https://github.com/danielrosehill/Hebrew-Calendar-Resources)
- [Hebrew Image Generation Eval](https://github.com/danielrosehill/Hebrew-Image-Generation-Eval)

</td>
<td valign="top" width="25%">

### 🧰 By Domain

Domain-specific MCP servers and tools are listed in [**mcps.md**](mcps.md):

- [Finance & Banking](mcps.md#finance--banking)
- [Government Data](mcps.md#government--open-data)
- [Government Services](mcps.md#government-services)
- [Healthcare](mcps.md#healthcare--medical)
- [Legal](mcps.md#legal) · [Insurance](mcps.md#insurance)
- [Real Estate](mcps.md#real-estate--land)
- [Safety & Emergency](mcps.md#safety--emergency)
- [Shopping](mcps.md#shopping--retail) · [Transport](mcps.md#transportation)
- [Weather](mcps.md#weather--environment)
- [Economics](mcps.md#economics--statistics)
- [Library](mcps.md#library--archives)
- [Careers](mcps.md#careers--jobs) · [Dashboards](mcps.md#dashboards)
- [Plugins](mcps.md#plugins) · [Voice](mcps.md#voice-agents)
- [Other](mcps.md#other-projects)

</td>
</tr>
</table>

# AI Agents

Autonomous AI agents built for Israeli use cases.

| Project | Description | Stars |
|---|---|---|
| [Claudi](https://github.com/itaisabi-collab/claudi) | ClaudioSabi — Israeli AI agent on Moltbook | ![](https://img.shields.io/github/stars/itaisabi-collab/claudi?style=social) |
| [Nachla Agent](https://github.com/Ofir-Metis/nachla-agent) | AI agent for בדיקת התכנות נחלות — feasibility studies for Israeli agricultural settlements | ![](https://img.shields.io/github/stars/Ofir-Metis/nachla-agent?style=social) |
| [News Agent](https://github.com/eyalban/News-Agent) | Daily Hebrew security briefing agent for the Iran-Israel conflict, automated via GitHub Actions | ![](https://img.shields.io/github/stars/eyalban/News-Agent?style=social) |
| [OlehAssist Agent](https://github.com/abernatkunin/OlehAssistAgent) | Chatbot to assist new Israeli immigrants (olim) with bureaucratic issues after making Aliyah | ![](https://img.shields.io/github/stars/abernatkunin/OlehAssistAgent?style=social) |



# Agent Skills & Frameworks

Organizations and projects providing collections of Israel-focused AI agent skills and MCP servers

## [Skills IL](https://github.com/skills-il)

![Skills](https://img.shields.io/badge/skills-127-blue) ![Categories](https://img.shields.io/badge/categories-12-green) ![Website](https://img.shields.io/badge/website-agentskills.co.il-orange)

Curated AI agent skills for Israeli developers — an open-source collection of [Agent Skills](https://docs.anthropic.com/en/docs/build-with-claude/skills) built for Israeli-specific needs (tax compliance, Hebrew localization, government APIs, and more). Each skill follows the open Agent Skills standard and works across Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex, and other AI coding agents.

| Category | Skills | Description | Repo |
|----------|--------|-------------|------|
| Tax & Finance | 19 | Invoices, income tax, VAT, payments, stock analysis, startup finance | [tax-and-finance](https://github.com/skills-il/tax-and-finance) |
| Government Services | 18 | Population Authority, National Insurance, Knesset, gov APIs | [government-services](https://github.com/skills-il/government-services) |
| Localization | 17 | Hebrew RTL, i18n, accessibility, document generation, design systems | [localization](https://github.com/skills-il/localization) |
| Developer Tools | 15 | ID validation, date conversion, Israeli dev utilities | [developer-tools](https://github.com/skills-il/developer-tools) |
| Accounting | 14 | Bookkeeping, bank reconciliation, expense management, financial reporting | [accounting](https://github.com/skills-il/accounting) |
| Marketing & Growth | 9 | Hebrew SEO, product launch, LinkedIn strategy, content marketing | [marketing-growth](https://github.com/skills-il/marketing-growth) |
| Communication | 8 | SMS, email, WhatsApp automation, Monday.com workflows | [communication](https://github.com/skills-il/communication) |
| Health Services | 7 | HMO navigation, patient rights, health insurance, telemedicine | [health-services](https://github.com/skills-il/health-services) |
| Security & Compliance | 7 | Privacy law, cyber regulations, e-commerce compliance | [security-compliance](https://github.com/skills-il/security-compliance) |
| Food & Dining | 6 | Kashrut, supermarket prices, restaurant operations, food compliance | [food-and-dining](https://github.com/skills-il/food-and-dining) |
| Education | 4 | Bagrut exams, academia, online learning | [education](https://github.com/skills-il/education) |
| Legal Tech | 3 | Employment contracts, labor law, regulatory compliance | [legal-tech](https://github.com/skills-il/legal-tech) |

**Website:** [agentskills.co.il](https://agentskills.co.il) · **Built by:** [YooTech](https://yootech.io/) · **CLI:** `npx skills` via [skills-il-cli](https://github.com/skills-il/skills-il-cli)

**Author:** [skills-il](https://github.com/skills-il)

---

# Curated Lists

Community-maintained collections of Israeli AI agent resources.

**External ecosystem maps:**

- [The Israeli Agentic AI Landscape (Twine Security)](https://www.twinesecurity.com/resource/the-israeli-agentic-ai-landscape) — Market map of Israeli companies building in the agentic AI space.

| Project | Description | Stars |
|---|---|---|
| [Claude Israel](https://github.com/danielrosehill/Claude-Israel) | Index of Claude / Claude Code projects with an Israel focus. | ![](https://img.shields.io/github/stars/danielrosehill/Claude-Israel?style=social) |
| [Awesome Open Source Israel](https://github.com/lirantal/awesome-opensource-israel) | Awesome list of open source projects created by Israeli developers — broader than AI, but includes many AI-adjacent projects. | ![](https://img.shields.io/github/stars/lirantal/awesome-opensource-israel?style=social) |
| [Awesome Agent Skills Israel](https://github.com/alexpolonsky/awesome-agent-skills-israel) | A curated list of Agent Skills for navigating life in Israel | ![](https://img.shields.io/github/stars/alexpolonsky/awesome-agent-skills-israel?style=social) |
| [Useful AI Agent Skills — Israel-Specific](https://github.com/danielrosehill/Useful-AI-Agent-Skills#13-israel-specific) | A broader catalogue of useful AI agent skills with a dedicated Israel-specific section. | ![](https://img.shields.io/github/stars/danielrosehill/Useful-AI-Agent-Skills?style=social) |


# Communities & Organizations

Israeli AI communities, professional associations, and organizations supporting the local AI ecosystem.

- [AI Israel (aiisrael.org.il)](https://aiisrael.org.il/) — Israeli AI community organization.
- [The Institute AI (theinstituteai.org.il)](https://www.theinstituteai.org.il/en/) — Israeli institute for AI research and policy.
- [Agent Skills IL (agentskills.co.il)](https://agentskills.co.il/en) — Companion website to the Skills IL open-source project.
- [Machine Learning Israel (machinelearning.co.il)](https://machinelearning.co.il/) — Israeli machine learning community.
- [Israeli Association for Artificial Intelligence (iaai.org.il)](https://iaai.org.il/) — Professional association for AI practitioners and researchers in Israel.
- [Ivrit.ai](https://www.ivrit.ai/en/ivrit-ai-2/) — Open Hebrew speech and language datasets for AI research.
- [Dicta / DictaLM](https://dicta.org.il/dicta-lm) — Hebrew NLP research center and open-source Hebrew LLMs.
- [Data-IL](https://data-il.org/en/) — Israeli data science and AI community.

## Meetups

In-person and hybrid AI/ML meetup groups across Israel.

- [Artificial Intelligence Israel](https://www.meetup.com/artificial-intelligence-israel/) — General AI meetup group in Israel.
- [Generative AI Israel](https://www.meetup.com/generative-ai-israel/) — Meetup focused on generative AI.
- [Tel Aviv-Yafo Agentic AI Meetup Group](https://www.meetup.com/tel-aviv-yafo-agentic-ai-meetup-group/) — Tel Aviv meetup on agentic AI.
- [DataTalks JLM — Machine & Deep Learning in the Holy City](https://www.meetup.com/datatalks-jlm-machine-and-deep-learning-in-the-holy-city/) — Jerusalem-based ML/DL meetup. ([LinkedIn](https://il.linkedin.com/company/datatalks-jlm))
- [Prompt Practices TLV](https://www.meetup.com/prompt-practices-tlv) — Tel Aviv meetup on prompt engineering practices.
- [Computer Vision Israel Meetup](https://www.meetup.com/Computer-Vision-Israel-Meetup) — Computer vision community meetup.
- [Responsible AI TLV](https://www.meetup.com/responsible-ai-tlv) — Tel Aviv meetup on responsible and ethical AI.

## Facebook Groups

- [AI JLM](https://www.facebook.com/groups/aijlm/) — Jerusalem AI Facebook group.
- [AI Israel](https://www.facebook.com/groups/aisrael/) — General Israeli AI Facebook group.
- [MCP Israel](https://www.facebook.com/groups/mcpisrael/) — Israeli community Facebook group for Model Context Protocol. ([mcpisrael.com](https://mcpisrael.com/))

---

# Government Bodies

Israeli government agencies and national programs relevant to AI.

- [Israel Innovation Authority (innovationisrael.org.il)](https://innovationisrael.org.il/) — Government agency supporting Israeli innovation and R&D, including AI initiatives.
- [National AI Program (aiisrael.org.il)](https://aiisrael.org.il/) — Israel's national program for AI.
- [The Institute for AI (theinstituteai.org.il)](https://www.theinstituteai.org.il/en/) — National institute for AI research and policy.

---

# Centers of Excellence

Academic and research centers focused on AI and data science in Israel.

- [Israel Data Science & AI Initiative — Technion (idsai.net.technion.ac.il)](https://idsai.net.technion.ac.il/) — Technion's interdisciplinary data science and AI research center.

---

# Conferences & Events

AI, ML, and tech conferences and event aggregators in Israel.

- [AI Week](https://ai-week.com/) — Annual AI conference in Israel.
- [IMVC — Israel Machine Vision Conference](https://www.imvc.co.il/) — Annual machine vision and deep learning conference.
- [AI Dev TLV](https://aidevtlv.com/) — Tel Aviv AI developer conference.
- [Tech1](https://tech1.co.il/) — Israeli tech conference.
- [Cyber Week TAU](https://cyberweektau.com/) — Tel Aviv University's annual cybersecurity conference (AI/ML tracks).
- [Dev.Events — Israel AI](https://dev.events/AS/IL/ai) — Aggregated listing of AI events in Israel.
- [Events.co.il](https://events.co.il/) — General Israeli events directory.
- [Science.co.il — AI Conferences](https://www.science.co.il/ai/Conferences.php) — Directory of AI-related conferences in Israel.
- [Machine Learning Israel — Events](https://machinelearning.co.il/events/) — Events calendar from the Machine Learning Israel community.

---

# Inference Providers & Local Clouds

Cloud and inference providers with a presence relevant to Israeli AI workloads.

- [Nebius](https://nebius.com/) — AI-focused cloud and GPU inference provider.

---

# Startup Ecosystem

Directories and databases tracking the Israeli AI startup ecosystem.

- [Startup Nation Finder](https://finder.startupnationcentral.org/) — Searchable database of Israeli startups maintained by Start-Up Nation Central.

---

# Hebrew Language Resources

Indexes and resource lists focused on Hebrew-language AI models, tooling, and evaluations — adjacent to the Israel-specific agent and MCP ecosystem.

## External Resources

- [Dicta (dicta.org.il)](https://dicta.org.il/) — Israeli center for the analysis of Hebrew texts; open-source Hebrew NLP models, datasets, and tools (including DictaLM and OCR for Hebrew).
- [Open Hebrew LLM Leaderboard (Hugging Face)](https://huggingface.co/blog/leaderboard-hebrew) — Community leaderboard evaluating LLMs on Hebrew language tasks.
- [RubyBot (rubybot.co.il)](https://rubybot.co.il/) — Hebrew-native AI chatbot.
- [PolyLM (polylm.com)](https://www.polylm.com/) — Hebrew-native AI assistant / LLM product.

## Indexes

| Project | Description | Stars |
|---|---|---|
| [Hebrew AI Models](https://github.com/danielrosehill/Hebrew-AI-Models) | Index of AI/LLM models with Hebrew language support. | ![](https://img.shields.io/github/stars/danielrosehill/Hebrew-AI-Models?style=social) |
| [Hebrew Language Projects Index](https://github.com/danielrosehill/Hebrew-Language-Projects-Index) | A broad index of Hebrew language projects across the AI/NLP ecosystem. | ![](https://img.shields.io/github/stars/danielrosehill/Hebrew-Language-Projects-Index?style=social) |
| [English ↔ Hebrew Translation](https://github.com/danielrosehill/English-Hebrew-Translation) | Resources, tools, and notes on English ↔ Hebrew translation workflows. | ![](https://img.shields.io/github/stars/danielrosehill/English-Hebrew-Translation?style=social) |
| [Hebrew Calendar Resources](https://github.com/danielrosehill/Hebrew-Calendar-Resources) | Resources for working with the Hebrew calendar (Jewish/Israeli date systems). | ![](https://img.shields.io/github/stars/danielrosehill/Hebrew-Calendar-Resources?style=social) |
| [Hebrew TTS Providers](https://github.com/danielrosehill/Hebrew-TTS-Providers) | Index of text-to-speech providers and engines supporting Hebrew. | ![](https://img.shields.io/github/stars/danielrosehill/Hebrew-TTS-Providers?style=social) |
| [Hebrew Image Generation Eval](https://github.com/danielrosehill/Hebrew-Image-Generation-Eval) | Evaluation of image generation models on their ability to render Hebrew text. | ![](https://img.shields.io/github/stars/danielrosehill/Hebrew-Image-Generation-Eval?style=social) |


# Contributing

Anyone is welcome to open a pull request to add an Israel-related AI agent, skill, or MCP server to this list.

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

This resource is intended for those discovering AI agents, skills, and MCP servers relevant to Israel. It is not exhaustive and is maintained on a best-effort basis.

The inclusion of a project in this list does not constitute an endorsement. Users should evaluate each project independently for their specific use cases.

---

*Last updated: 2026-04-05*

Maintained by [Daniel Rosehill](https://github.com/danielrosehill)