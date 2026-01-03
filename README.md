# 🏗️ ArchGen Pro: AI Solutions Architect

> **Turn vague business ideas into production-ready technical specifications in seconds.**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red.svg)
![AI](https://img.shields.io/badge/AI-Llama--3-purple.svg)
![Status](https://img.shields.io/badge/Status-Prototype-success.svg)

**ArchGen Pro** is an AI-powered automation tool designed to bridge the gap between high-level business requirements and low-level engineering tasks. It simulates a **Software Architect's workflow** by decomposing simple text inputs into structured modular breakdowns, database schemas, and API contracts.

---

## 🎯 Objective (The Problem)
In software development, translating a non-technical client's request (e.g., *"I want an Uber for lawn mowing"*) into actionable developer tasks takes hours of planning. This tool automates the **Requirement Analysis** and **System Design** phases.

## 🚀 Key Features

*   **🤖 Agentic Workflow:** Uses a multi-step AI pipeline (Analyst Agent → Architect Agent) to ensure logical consistency.
*   **🧠 Context-Aware Refinement:** The *Analyst Agent* first expands vague inputs into concrete functional requirements before engineering begins.
*   **🛡️ Hybrid Logic Engine:** Combines LLM reasoning with **deterministic rules**. (e.g., If "subscription" is mentioned, a *Payment Gateway* module is strictly enforced for security compliance).
*   **📄 JSON & SQL Ready:** Outputs strict JSON structures for Database Schemas and API Endpoints, ready for backend implementation.
*   **⚡ Speed:** Powered by Groq (Llama-3.3-70b) for sub-second inference speeds.

---

## 🛠️ Tech Stack

*   **Language:** Python
*   **LLM Engine:** Groq API (Llama-3.3-70b-versatile)
*   **Interface:** Streamlit (Web UI)
*   **Architecture:** Modular Service-Oriented Architecture (SOA)
*   **Data Validation:** Pydantic / JSON Mode enforcement

---

## 📂 Project Structure

This project follows a production-grade modular structure, separating the UI (View) from the Logic (Controller/Services).

```text
archgen-pro/
├── app/
│   ├── __init__.py
│   ├── ui.py              # Frontend logic (Streamlit)
│   ├── services.py        # AI Agents & Business Logic
│   └── config.py          # Configuration management
├── main.py                # Application Entry Point
├── .env                   # API Keys (GitIgnored)
├── requirements.txt       # Dependencies
└── README.md              # Documentation
