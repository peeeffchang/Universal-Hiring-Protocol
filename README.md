# Universal Hiring Protocol (UHP)

**The common language for AI agents, talent platforms, employers, and recruiters.**

UHP is an open-source protocol that standardizes how AI agents and systems interoperate to enable discovery, application, screening, interviewing, and hiring workflows — with **privacy first**, **intent-based actions**, and **secure consent mechanisms** built into the core.

---

## 🚀 Why UHP?

Hiring today is fragmented across job boards, ATS systems, HR APIs, and recruiter tools. This creates friction for AI assistants, multiplatform agents, and integrated workflows.

**UHP provides a shared protocol** that:

- Enables AI agents (e.g., chatbot assistants, LLM-based job search copilots) to discover roles, apply, schedule interviews, and negotiate offers using a common interface
- Embeds privacy controls and **progressive disclosure** by default
- Reduces custom point-to-point integrations between candidate systems and employer systems
- Supports **intent-based actions**, *not* just CRUD APIs
- Allows systems to interoperate without exposing unnecessary personal data

---

## 📘 Learn

Explore the **Protocol Overview**, **Privacy Model**, and **Specification** to understand:

- Core concepts: Actors, intents, states
- Canonical JSON schemas for jobs, candidates, applications, and consent
- How visibility levels and purpose-bound access govern data exposure
- Agent-native workflows for application and interview lifecycle

---

## 🧠 Design Principles

UHP is inspired by open standards like the Universal Commerce Protocol (UCP) — designed for agentic interoperability in commerce — but built for **hiring and recruitment with privacy as a first-class citizen**.

Key principles include:

- **Standardized Interoperability:** Uniform way for platforms, agents, and systems to interact, regardless of backend systems
- **Privacy-Native:** Strong visibility levels, consent lifecycles, and purpose-bound data access
- **Agentic Hiring:** Intent-driven actions and state machines make it easy for autonomous AI agents to drive workflows
- **Extensible:** Schema and capabilities can be extended for industry-specific or advanced use cases

---

## 🛠️ Implement

This repository contains:

- The UHP **protocol specification**
- JSON Schemas for core objects (Job, Candidate, Application, Consent)
- Reference definitions for intent actions and state machines
- Examples and best practices for integrating UHP with AI agents

See the `/specification` directory for full details.

---

## 🔐 Privacy & Consent

UHP treats privacy as a core building block, not an afterthought:

- **Visibility levels** (Public, Anonymized, Restricted, Sensitive) govern what data can be exposed at each stage of the hiring workflow
- **Consent objects** encode state and purpose bindings
- Data access is **purpose-bound** — agents must declare *why* they need access to specific fields
- Designed to be compatible with real-world privacy regulations

---

## 🤖 Built for AI Agents

Unlike traditional HR APIs, UHP is designed to be *interpretable and reasoned over by AI agents*:

- Intent-based action envelope (`ApplyForJob`, `ScheduleInterview`, etc.)
- Explicit state machines for tracking workflow progression
- Machine-readable capability discovery
- Privacy-aware consensual access patterns

---

## 📦 Getting Started

1. Clone the repository
2. Review the JSON Schema definitions in `/schemas`
3. Read the protocol overview in `/docs`
4. Use intent action examples in `/examples` to simulate agent workflows
5. Integrate with your platform or agent implementation

---

## 🧩 Contributing

We actively welcome contributions — from schema improvements to implementation examples:

- Found a bug? Raise an issue.
- Want to propose a new capability? Write a proposal in `/proposals`.
- Interested in governance or extensions? Join the discussion.

Together, we can build the *standard protocol for the future of hiring interoperability*.

---

## 📖 License

UHP is released under the **Apache License 2.0**.

---

## 📍 See Also

For inspiration and background on agent-centric protocols in adjacent domains, see:

- **Universal Commerce Protocol (UCP)** — an open standard for agentic commerce interoperability, enabling discovery and transactions across platforms and AI assistants. :contentReference[oaicite:0]{index=0}


