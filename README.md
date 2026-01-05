# Agentic AI Industrial Orchestrator

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.10-blue) ![UiPath](https://img.shields.io/badge/UiPath-RPA-orange) ![Copilot](https://img.shields.io/badge/Microsoft-Copilot%20Studio-purple)

## 🚀 Executive Summary
This project demonstrates a **Multi-Agent Orchestration System** designed for Industry 4.0 environments. It bridges the gap between **Generative AI** and **Operational Technology (OT)**, allowing plant managers to query real-time production metrics and trigger physical remediation workflows using natural language.

The system uses a **Hub-and-Spoke Agentic Architecture** where **Microsoft Copilot Studio** acts as the central reasoning engine, coordinating specialized sub-agents for data analysis, compliance retrieval (RAG), and autonomous action (RPA).

---

## 🏗️ System Architecture
![System Architecture](architecture/system_diagram.png)

The architecture follows a closed-loop control pattern:
1.  **Sense:** The Python Agent fetches live telemetry (Defect Rates, Yield).
2.  **Think:** The Orchestrator (Copilot) evaluates data against policy documents (RAG).
3.  **Act:** The UiPath Robot executes remediation workflows (SharePoint Logging, Machine Adjustment).

---

## 📂 Repository Structure

```text
agentic-industrial-orchestrator/
├── 📂 backend_api/           # Agent 2: Python/FastAPI Data Intelligence Service
│   ├── agents/               # Logic for statistical analysis
│   ├── data/                 # Local datasets (production_logs.csv)
│   ├── agent2_api.py         # Main entry point for REST API
│   └── requirements.txt      # Python dependencies
│
├── 📂 copilot_config/        # Agent 1: Microsoft Copilot Studio Configuration
│   └── defect_retrieval_topic.yaml  # YAML definition of the conversation logic
│
├── 📂 uipath_robot/          # Agent 4: Autonomous Action Bot
│   ├── Main.xaml             # The actual UiPath workflow source code
│   └── remediation_workflow.md  # Detailed functional specification
│
├── 📂 architecture/          # System Design Assets
│   └── system_diagram.png    # High-level architectural view
│
└── README.md                 # Project Documentation
