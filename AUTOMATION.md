# automation-laravel — Feature Scopes Document

**Stack:** Laravel 13 · PHP 8.5 · Filament 5 · Livewire 4
**Status:** Draft v0.1
**Owner:** Liberu Group Engineering

---

## 1. Purpose

`automation-laravel` is a lean, shared **AI services package** that plugs into the other Liberu repositories ([`cms-laravel`](https://github.com/liberusoftware/cms-laravel), [`crm-laravel`](https://github.com/liberusoftware/crm-laravel), [`billing-laravel`](https://github.com/liberusoftware/billing-laravel), [`accounting-laravel`](https://github.com/liberusoftware/accounting-laravel), [`control-panel-laravel`](https://github.com/liberusoftware/control-panel-laravel)) and gives them a single, consistent way to call AI.

It is **not** a full platform — no CRM, billing, or telephony logic lives here. Its only job is: receive an AI task from a consuming app, route it to the right provider/model, run it, and return a structured result. Everything domain-specific (leads, tickets, invoices, content) stays in the app that owns that domain.

---

## 2. Design Principles

- **Provider-agnostic:** consuming apps ask for a *capability* ("summarise", "transcribe", "generate image"), not a specific vendor.
- **Composable package, not a platform:** installable via Composer into any Liberu app; ships a small Filament panel for configuration/monitoring only.
- **Modular, not monolithic:** the core package only provides the provider contract, queue/callback plumbing, and config/monitoring UI. Each capability (thinking, data processing, voice, imagery, video) and each provider driver (OpenAI, Claude, Gemini) ships as its **own sub-package/module**, installed and enabled independently. A consuming app that only needs text/thinking capability shouldn't have to pull in voice or video dependencies, and a new capability or provider should be addable without touching existing modules.
- **Stateless core:** no business data stored long-term — jobs, inputs, and outputs pass through, with only logs/usage metadata retained.
- **Queue-first:** every AI call runs as a queued job so slow/voice/video tasks never block the calling app's request cycle.
- **Fail safe:** provider errors, timeouts, and rate limits degrade gracefully (retry, fallback provider, or clear failure callback) rather than silently hanging.

---

## 3. Supported AI Providers

| Provider | Used for |
|---|---|
| **OpenAI / ChatGPT** | Text/chat, function calling, image generation, transcription |
| **Anthropic Claude** | Text/chat, reasoning/thinking tasks, long-document analysis |
| **Google Gemini** | Text/chat, multimodal (image/video understanding), transcription |

- Common `AiProvider` contract; each vendor is a **separate driver module** behind it, published/enabled independently (e.g., `liberu/automation-openai`, `liberu/automation-claude`, `liberu/automation-gemini`) rather than bundled into the core.
- Per-capability default provider, configurable in Filament, with automatic fallback to a secondary provider on failure — fallback only engages providers that are actually installed/enabled.
- API keys and per-provider rate/cost limits managed centrally so every consuming app benefits without re-implementing it.
- Adding a fourth provider in future means adding a new driver module, not modifying the core or existing drivers.

---

## 4. Core Capabilities

Kept intentionally broad-but-shallow — a small, well-defined set of task types rather than dozens of bespoke endpoints. Each capability below is its **own module**, installed only where needed, so a consuming app's dependency footprint matches what it actually uses:

### 4.1 Thinking / Reasoning Tasks
- Summarisation, classification, extraction (e.g., "what's this support ticket about?")
- Structured-output generation (JSON) for the calling app to consume directly
- Multi-step reasoning chains for tasks like lead scoring or ticket triage, with the *decision logic* owned by the calling app and the *reasoning* delegated here

### 4.2 Data Processing
- Cleaning, tagging, and enriching structured or semi-structured data passed in from a consuming app (e.g., CRM contact enrichment, CMS content tagging)
- Batch mode for bulk jobs (e.g., re-tag all existing records) alongside single-record calls

### 4.3 Voice
- Speech-to-text (calls, voicemail, voice notes)
- Text-to-speech for AI-driven replies (e.g., an AI receptionist in another app)
- Designed to accept an audio stream/file reference and return transcript + optional synthesized audio, so calling apps don't need their own voice pipeline

### 4.4 Imagery
- Image generation from a text prompt
- Image understanding/description (e.g., "what's in this uploaded photo?")

### 4.5 Video
- Short video generation from a prompt/brief, where the selected provider supports it
- Video understanding (summarise/describe a video clip) where supported

---

## 5. Integration Model

- **Package install:** consuming apps `composer require liberu/automation-laravel` for the core, then add only the capability and provider modules they need (e.g., a CMS site might install `automation-laravel` + `automation-openai` + `automation-imagery` only).
- **Module registration:** each capability/provider module self-registers with the core on boot (service provider), so the core never needs to know in advance which modules exist — new modules plug in without core changes.
- **Dispatch:** calling app dispatches an `AiTaskRequest` (capability + payload + callback) to the shared queue; the core routes it to whichever capability/provider modules are installed and configured.
- **Callback/event:** on completion, an event/webhook fires back to the calling app with the result, so the calling app decides what to do with it (save to CRM, attach to a CMS post, etc.).
- **Filament panel (this repo only):** provider configuration, per-capability routing rules, job monitoring/retry, and usage/cost dashboards — no domain-specific UI. The panel lists only the modules currently installed/enabled.

---

## 6. Cross-Cutting

- **Usage tracking:** per app, per capability, per provider — token/cost counts surfaced for Finance without needing access to Accounting internals.
- **Guardrails:** basic content-safety checks and optional human-approval flag on a task (calling app can mark a task as "requires review before use").
- **Privacy:** configurable redaction/minimisation step before payloads leave for an external provider, and no persistent storage of raw inputs/outputs beyond a short retention window for debugging.
- **Observability:** logging and basic metrics (latency, error rate, fallback rate) per provider/capability.

---

## 7. Explicit Non-Goals

To keep this package lean, it deliberately does **not** include:

- CRM, billing, accounting, or provisioning logic (lives in the respective repos)
- Telephony/switchboard, social media scheduling, or marketplace integrations (belong in whichever app owns those channels)
- Long-term storage of business data — this is a processing layer, not a system of record

---

## 8. Suggested Phasing

1. Core package scaffold + `AiProvider` contract + OpenAI driver
2. Add Claude and Gemini drivers + fallback routing
3. Thinking/data-processing capability + queue/callback pattern proven with one consuming app (e.g., CRM lead enrichment)
4. Voice capability (speech-to-text/text-to-speech)
5. Imagery capability (generation + understanding)
6. Video capability (generation + understanding, provider-dependent)
7. Usage/cost dashboard and guardrail/approval flag polish

---

## 9. Open Questions

- Sync vs. async API surface for consuming apps — always queue, or allow a fast synchronous path for short "thinking" calls?
- Where does redaction policy live — centrally in `automation-laravel`, or configured per calling app?
- Which providers support video generation/understanding well enough today, and should that capability start as an OpenAI/Gemini-only feature until parity improves?
