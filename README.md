# ≯ Splunk SLA Tracker — MTTD / MTTR / Incident SLA DAstboard

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)

[![Splunk](https://img.shields.io/badge/Splunk-Enterprise%208%2B-green.svg)](https://splunk.com)

> **Automated SLA tracking and reporting system** that calculates real-time MTTD, MTTR, and SLA breach metrics from Splunk incident logs - generates weekly HTML/PDF reports and Splunk dashboards for management visibility.

## 🌯 Problem Statement

Production support teams struggle to prove SLA	�compliance without manual spreadsheet tracking. This tool automates:
- **MTTD** (Mean Time to Detect) per incident severity
- **MTTR** (Mean Time to Resolve) by team and service
- **SLA breach detection** - which incidents breached contractual windows
- **Weekly trend reports** - exportable to PDF/HTML for management

## 🔍 Key SPL Queries

```spl
index=incidents sourcetype=incident_log earliest=-30d status=resolved
| eval mttr_minutes=round((strptime(resolved_at, "%Y-%m-%dT%H:%M:%S") - strptime(detected_at, "%Y-%m-%dT%H:%M:%S")) / 60, 1)
| stats avg(mttr_minutes) as avg_mttr, max(mttr_minutes) as max_mttr, count as total by severity
```

## 🚀 Quick Start

```bash
git clone https://github.com/PraveenKumarSStefan/splunk-sla-tracker.git
cd splunk-sla-tracker
pip install -r requirements.txt
python src/sla_tracker.py
```

## 👨‍💻 Author
**Praveenkumar S** | [GitHub](https://github.com/PraveenKumarSStefan)
