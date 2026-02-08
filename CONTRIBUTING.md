# Contributing to Universal Hiring Protocol (UHP)

Thank you for your interest in contributing to the **Universal Hiring Protocol (UHP)**.  
UHP is an open, agent-native protocol for interoperable, privacy-preserving hiring workflows.

This document explains **how to contribute**, **what kinds of contributions we are looking for**, and **how protocol decisions are made**.

---

## 🧭 Project Philosophy

UHP is a **protocol**, not an application or product.

This means:
- We prioritize **interoperability** over features
- We favor **clear semantics** over implementation convenience
- We design for **AI agents first**, humans second
- We treat **privacy as a protocol primitive**, not an optional add-on

If a proposal does not meaningfully improve interoperability, agent safety, or privacy guarantees, it is unlikely to be accepted.

---

## 🧩 What You Can Contribute

We welcome contributions in the following areas:

### 1. Protocol Specification
- Clarifications or improvements to the core protocol
- Formalization of state machines
- Improvements to intent/action definitions
- Privacy and consent semantics

### 2. Schemas
- JSON Schema improvements
- Validation rules
- Backward-compatible schema evolution proposals

### 3. Examples
- Minimal examples of agent workflows
- Cross-platform interoperability examples
- Privacy-safe interaction patterns

### 4. Proposals (Extensions)
- Optional capabilities (e.g., interviews, offers)
- Industry-specific extensions
- Experimental features (must be clearly marked)

### 5. Documentation
- Clarifying ambiguous sections
- Improving onboarding or explanations
- Diagrams and conceptual documentation

---

## 🚫 What We Are *Not* Looking For (Yet)

To keep the protocol focused, we are **not currently accepting**:

- Product-specific integrations
- UI / frontend components
- Vendor-specific APIs
- Proprietary formats
- Non-essential features that expand scope prematurely

These may be appropriate **after the core protocol stabilizes**.

---

## 🛠️ Contribution Process

### Step 1: Open an Issue
Before submitting a major change:
- Open an issue describing the problem or proposal
- Explain *why* it improves interoperability or agent safety
- Reference relevant parts of the existing spec

### Step 2: Discuss & Refine
Maintainers and community members will discuss:
- Scope
- Backward compatibility
- Privacy implications
- Agent-friendliness

### Step 3: Submit a Pull Request
When ready:
- Fork the repository
- Create a focused PR (small and reviewable)
- Update relevant documentation
- Clearly state whether the change is **breaking** or **non-breaking**

---

## 📐 Design Guidelines (Very Important)

All contributions **must** adhere to these rules:

### 1. Agent-First Design
Assume:
- The primary consumer is an **AI agent**
- The agent may act autonomously
- The agent must be able to reason about correctness and safety

If an LLM cannot easily reason about your change, it needs refinement.

---

### 2. Privacy by Default
- No proposal may weaken privacy guarantees
- New fields must declare a **visibility level**
- Access must be **purpose-bound**
- Consent must be explicit and revocable

When in doubt, choose **less data exposure**.

---

### 3. Minimalism
- Prefer small, composable primitives
- Avoid feature creep
- If something can be an extension, it probably should be

---

### 4. Backward Compatibility
Breaking changes must:
- Be clearly marked
- Include a migration strategy
- Be justified as unavoidable

---

## 🧪 Experimental Features

Experimental features:
- Must live in `/proposals` or `/extensions`
- Must be clearly labeled `EXPERIMENTAL`
- Must not be required for core compliance

---

## 🏷️ Versioning & Stability

UHP follows semantic versioning:

- **MAJOR**: breaking protocol changes
- **MINOR**: backward-compatible additions
- **PATCH**: clarifications or non-semantic fixes

The core protocol aims for **slow, deliberate evolution**.

---

## 🧑‍⚖️ Governance (Early Stage)

At this stage:
- Maintainers act as provisional stewards
- Decisions are made by consensus where possible
- The long-term goal is **open, multi-stakeholder governance**

As adoption grows, governance will evolve transparently.

---

## 📜 Code of Conduct

We expect contributors to:
- Be respectful and constructive
- Assume good faith
- Focus on technical merit
- Avoid personal or commercial attacks

Harassment or hostile behavior will not be tolerated.

---

## 📄 License

By contributing to UHP, you agree that your contributions will be licensed under the **Apache License 2.0**, consistent with the rest of the project.

---

## 🙌 Thank You

Protocols succeed only through **careful collaboration**.

Your contributions help shape a safer, more interoperable future for **AI-driven hiring**.
