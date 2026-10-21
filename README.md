# AI Tool Boundary Evaluation Lab

A small offline lab for one security boundary in an AI application: proposed tool actions must pass application-owned authorization before execution. Synthetic prompt-injection scenarios illustrate why document text must not grant permissions.

**This version does not call an LLM, detect prompt injection, or measure model robustness.** Proposed actions are hand-authored fixtures. The code tests a deterministic authorization gate; it never executes tools, emails, shell commands, or network requests.

## Run

Python 3.10+, standard library only. From this repository directory:

```sh
python evaluate.py
python -m unittest discover -s tests -v
```

Use `python3` if necessary. No API keys, inference charges, or model downloads. The demo prints a report for eight cases matching `examples/expected.json`. Exit 0 means all expected decisions matched; 1 means a mismatch; 2 means invalid input.

## Threat model and control

A document-answering assistant receives untrusted retrieved text. A malicious document may instruct it to send data, read another account's documents, or claim administrator authority. The fixtures pair such text with illustrative proposed tool calls.

The gate accepts only an exact two-field object: `tool` equal to `read_document` and `document_id` present in a trusted application-provided allowlist. Unknown tools, extra fields, malformed actions, and inaccessible document IDs are denied. The untrusted document text is intentionally not consulted for authorization.

In a real system, the allowlist must come from authenticated server-side access checks and must not be editable by the model or retrieved content. The evaluator treats each fixture's allowlist as trusted test setup, not as a safe production permissions source. This lab does not implement authentication, retrieval, tenant isolation, or a tool executor.

## What the results mean

Eight matching decisions show that this gate follows its specified policy on these examples. They do not show that an LLM resisted injection or that an application is secure. An allowed read can still expose malicious content, and harmful instructions could still affect the final answer. Content safety, answer integrity, output handling, and data leakage through permitted channels remain separate concerns.

See `docs/threat-model.md` for assumptions and `docs/experiments.md` for a path toward actual model evaluations. AI-assisted educational starter with invented documents and identifiers. No real-world exploitation, production deployment, or research achievement is claimed. MIT licensed.
