# AI Customer Support Automation Platform

## Overview

AI Customer Support Automation Platform is a scalable backend system designed to automate customer support workflows using Large Language Models (LLMs). The platform processes customer support tickets asynchronously, generates AI-powered responses, and stores ticket data for future analysis.

The project demonstrates modern backend engineering practices including distributed task processing, containerized infrastructure, REST API development, and local LLM integration.

---

## Features

- AI-powered support ticket response generation
- Asynchronous ticket processing using Celery
- Redis-based task queue management
- PostgreSQL database integration
- Local LLM inference using Ollama and Mistral
- RESTful API built with FastAPI
- Dockerized infrastructure
- Production-ready modular architecture
- Extensible design for future integrations

---

## System Architecture

Customer Request
↓
FastAPI Backend
↓
PostgreSQL Database
↓
Redis Queue
↓
Celery Worker
↓
Mistral LLM (Ollama)
↓
AI Generated Response
↓
Database Update

---

## Tech Stack

### Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis
- Celery
- Pydantic

### AI

- Ollama
- Mistral LLM

### DevOps

- Docker
- Docker Compose

### Frontend (In Progress)

- Next.js
- React
- TypeScript
- Tailwind CSS

---

## Project Structure

```text
AI-SUPPORT-PLATFORM
│
├── app
│   ├── api
│   ├── core
│   ├── db
│   ├── models
│   ├── schemas
│   ├── services
│   ├── workers
│   ├── __init__.py
│   └── main.py
│
├── frontend
│   ├── app
│   ├── public
│   ├── package.json
│   └── ...
│
├── .env
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI-SUPPORT-PLATFORM
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Infrastructure

Start PostgreSQL and Redis:

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Run Celery Worker

```bash
celery -A app.workers.worker worker --pool=solo --loglevel=info
```

---

## Install and Run Ollama

Pull Mistral model:

```bash
ollama pull mistral
```

Run model:

```bash
ollama run mistral
```

---

## API Workflow

### Create Ticket

Client sends support request.

```json
{
  "email": "user@example.com",
  "message": "Unable to login to my account."
}
```

### Ticket Processing

1. Ticket stored in PostgreSQL
2. Celery task added to Redis queue
3. Worker retrieves task
4. Mistral generates response
5. Database updated with AI reply

---

## Current Status

### Completed

- FastAPI Backend
- PostgreSQL Integration
- Redis Queue
- Celery Worker
- Ollama Integration
- Mistral Response Generation
- Docker Infrastructure

### Under Development

- Frontend Dashboard
- User Authentication
- Analytics Dashboard
- Slack Integration
- Zendesk Integration
- Multi-Tenant SaaS Support

---

## Future Enhancements

- JWT Authentication
- Role-Based Access Control
- Ticket Prioritization
- AI Escalation Logic
- Monitoring and Logging
- Kubernetes Deployment
- Multi-Model LLM Support
- Real-Time Notifications

---

## Learning Objectives

This project demonstrates:

- Backend API Development
- Distributed Systems
- Queue-Based Architecture
- AI Application Development
- Containerization
- Database Design
- Production-Oriented Software Engineering

---
