# Israel Data

Datasets and reference material about Israel, published in a form intended to be read by AI agents.

Not servers and not agents — the material an agent grounds itself on. Machine-readable classification codes, lookup tables, official guidance restructured for retrieval, and field-level notes on Israeli data feeds. The distinguishing test is that the repo ships data or documented facts rather than something you run: MCP servers live in [mcps.md](mcps.md), and the agents that consume this material live in [agents.md](agents.md).

| Project | Description | Stars |
|---|---|---|
| [Israel MNOs Ref](https://github.com/danielrosehill/Israel-MNOs-Ref) | Israeli mobile network operators and MVNOs as hierarchical JSON with a schema — operator type, 4G and 5G bands held, host network, PLMN carrier IDs and subscriber estimates, each value carrying its own confidence level and source references | ![](https://img.shields.io/github/stars/danielrosehill/Israel-MNOs-Ref?style=social) |
| [Israel Expense Classification Codes](https://github.com/danielrosehill/israel-expense-classification-codes) | Israel Tax Authority Form 6111 expense classification codes as machine-readable JSON, plus the separate income tax and VAT deduction rules — reference data for agents and accounting integrations | ![](https://img.shields.io/github/stars/danielrosehill/israel-expense-classification-codes?style=social) |
| [Israel Open Data Catalogue Translations](https://github.com/danielrosehill/Israel-Open-Data-Catalogue-Translations) | Hebrew → English translation mapping for every dataset on data.gov.il — a drop-in lookup layer for tools and agents working against the Hebrew-only catalogue | ![](https://img.shields.io/github/stars/danielrosehill/Israel-Open-Data-Catalogue-Translations?style=social) |
| [Israel Open Data Changelog](https://github.com/danielrosehill/Israel-Open-Data-Changelog) | Unofficial month-by-month changelog of what appeared on data.gov.il, reconstructed from the CKAN API — lets an agent see what datasets exist and when they landed | ![](https://img.shields.io/github/stars/danielrosehill/Israel-Open-Data-Changelog?style=social) |
| [Pikud HaOref Guidelines (03/26)](https://github.com/danielrosehill/Pikud-Haoref-Guidelines-0326) | Home Front Command civil defence guidelines in a structured form, for use as ground truth by AI agents | ![](https://img.shields.io/github/stars/danielrosehill/Pikud-Haoref-Guidelines-0326?style=social) |
| [Israel Red Alert Syntax Notes](https://github.com/danielrosehill/Israel-Red-Alert-Syntax-Notes) | Syntax notes for the IDF Home Front Command alert feed — field shapes and quirks for anyone automating on top of it | ![](https://img.shields.io/github/stars/danielrosehill/Israel-Red-Alert-Syntax-Notes?style=social) |

## Related

Datasets that sit inside a working system are listed with that system rather than here — [JLM Shelters Data](mcps.md#safety--emergency) and [Miklat MCP Data](mcps.md#safety--emergency) back a site and an MCP server, [Israel Online Stores](mcps.md#shopping--retail) backs product search, and [Hebrew Tech Vocab](hebrew.md#hebrew-resources) belongs with the Hebrew language material.

For reference material that is not AI-specific, see [Israel Reference Repos](https://github.com/danielrosehill/Israel-Reference-Repos) and [Israel Open Data Resources](https://github.com/danielrosehill/Israel-Open-Data-Resources), both listed under [Related Indexes](README.md#related-indexes).
