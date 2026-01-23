# RoleFit AI  
### Resume–Job Description Matching using Retrieval-Augmented Generation (RAG)

🚧 **Work in Progress (Actively Evolving)**

**RoleFit AI** is a practical AI system that analyzes **resumes and job descriptions** to explain **how well a candidate fits a role**, using **semantic retrieval and controlled LLM reasoning**.

The project focuses on **meaning-based understanding**, not keyword matching, and is built step by step to mirror how **real-world GenAI systems** are designed, debugged, and made reliable.

---

## 📌 Overview

Traditional resume screening relies heavily on keywords and rigid rules, which often miss context and intent.

RoleFit AI addresses this by:
- semantically understanding resumes and job descriptions
- retrieving only the most relevant context
- reasoning over that context to explain *why* a candidate fits (or doesn’t)

The system is intentionally built with:
- clean modular architecture
- explainability at every step
- safeguards to prevent hallucinated answers

---

## 🎯 End Goal

The final goal of RoleFit AI is to:
- evaluate **resume ↔ JD alignment**
- explain **skill and experience relevance**
- support **transparent, reasoned hiring decisions**

This is not just a matcher — it is designed to be a **reasoning-first fit analysis system**.

---

## 🧱 Architecture

The system follows a modular RAG pipeline:
Resume / JD (PDF or Text)
↓
Text Ingestion
↓
Chunking
↓
Embeddings
↓
Vector Retrieval (FAISS)
↓
Retrieval Confidence Check (Guardrails)
↓
LLM Reasoning (only if context is relevant)
↓
Final Structured Insights

A key design principle is that **LLM reasoning is conditional**, not automatic.

---

## 🚦 Guardrails & Reliability (Important)

RoleFit AI includes **retrieval-based guardrails** to prevent hallucinations.

- FAISS similarity scores are inspected
- If the retrieved context is weak or irrelevant:
  - the LLM is **not called**
  - the system returns a low-confidence, honest response

This ensures the system:
- answers only when documents support the query
- avoids confident but incorrect outputs

---

## 🚧 Project Status

### ✅ Implemented
- PDF ingestion with clean text extraction
- Safe handling of empty pages and multi-page documents
- Overlapping text chunking for context preservation
- Embedding generation for semantic representation
- FAISS-based vector storage and retrieval
- Retrieval ranking with similarity scores
- Retrieval debugging and inspection
- LLM reasoning layer with structured prompts
- Score-based guardrails to prevent hallucinations
- End-to-end RAG pipeline orchestration

### 🔜 Planned
- Real LLM integration (Gemini Pro / OpenAI)
- Resume–JD fit scoring
- Comparative candidate analysis
- UI layer (Streamlit / Gradio)
- Production-ready evaluation and logging

---

## 🛠️ Tech Stack

### Current
- Python
- PyPDF2 (PDF ingestion)
- SentenceTransformers (embeddings)
- FAISS (vector retrieval)
- Modular pipeline-based architecture

### Planned
- Gemini Pro / OpenAI (LLM reasoning)
- Streamlit / Gradio (UI)
- Advanced scoring & evaluation layers

---

## 📂 Project Structure
RoleFit-AI/
 ├── app/
 │ ├── ingestion.py
 │ ├── chunking.py
 │ ├── embeddings.py
 │ ├── vector_storage.py
 │ ├── retrieval.py
 │ ├── llm_reasoning.py
 │ └── llm_client.py # Mocked LLM client
 ├── main.py # Pipeline orchestrator
 ├── README.md
 ├── requirements.txt
 └── test_st.py # Experimental / test file
---

## ⚠️ Note on LLM Usage

The LLM layer is **currently mocked** to validate:
- pipeline correctness
- retrieval → reasoning flow
- prompt structure
- guardrail behavior

This is an intentional design choice.  
Real LLM integration is planned as the next phase.

---

## 🧠 Design Philosophy

- Retrieval decides *what is relevant*
- LLM decides *what it means*
- The system must be allowed to say **“I don’t know”**
- Explainability > blind confidence
- Architecture before intelligence

---

## 📌 Why this project matters

RoleFit AI is designed to demonstrate:
- real-world GenAI system design
- responsible use of LLMs
- practical RAG implementation
- interview-ready engineering decisions

---

## 📎 Status

This project is actively evolving as part of a structured learning journey in **Generative AI and RAG systems**.

Contributions, feedback, and discussions are welcome.
