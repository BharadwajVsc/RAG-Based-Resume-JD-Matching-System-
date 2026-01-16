# Resume–JD Matching using RAG

🚧 **Work in Progress**

A practical RAG-based project that matches resumes to job descriptions using semantic search and LLM reasoning, built with a clean and modular pipeline.

---

## 📌 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline to evaluate how well a resume matches a given job description.

Instead of relying on simple keyword matching, the system is designed to use semantic search and LLM-based reasoning to better understand candidate skills, experience, and relevance to a role.

The project is intentionally built **step by step**, mirroring how real-world GenAI systems are developed, with a strong focus on clean architecture, explainability, and interview-safe design decisions.

---

## 🧱 Architecture

The system follows a modular pipeline:
PDF Ingestion → Text Chunking → Embeddings → Vector Retrieval → LLM Reasoning

### 🚧 Project Status

**Implemented**
- PDF ingestion with clean text extraction
- Safe handling of empty pages and multi-page documents
- Overlapping character-based chunking for context preservation

**Planned**
- Embedding generation for semantic representation
- Vector database integration (FAISS / Chroma)
- Semantic resume–JD retrieval
- LLM-based reasoning and explanation of candidate fit

## 🛠️ Tech Stack

**Current**
- Python
- PyPDF2 (PDF ingestion)
- Modular, pipeline-based architecture

**Planned**
- Embedding models
- Vector databases (FAISS / Chroma)
- Large Language Models (LLMs)

## 📂 Project Structure:
resume-jd-rag/
 ├── app/
 │   ├── ingestion.py
 │   ├── chunking.py
 │   └── retrieval.py
 ├── main.py
 ├── requirements.txt
 └── README.md
