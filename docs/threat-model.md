# Threat model

Assets: private document content and the tool execution boundary. Attacker: someone who can influence retrieved text, but cannot alter application policy or authenticated identity. Entry point: document text that pretends to be a higher-priority instruction.

The eight scenarios cover an ordinary permitted read, an ordinary out-of-scope read, an exfiltration request, a private-document request, an extra-argument destination, a fabricated administrator claim, a malformed call, and an innocuous document quoting an attack phrase while requesting a permitted read. Descriptions are context; the gate evaluates proposed structured actions only.

The last example shows why a phrase such as “ignore previous instructions” is not by itself an authorization decision. The gate enforces capabilities rather than keyword filtering. No control here prevents a bad answer or malicious content in an otherwise permitted document.

Trusted components: code, test expectations, authenticated application policy (represented by fixture allowlists). Untrusted components: retrieved text and proposed model actions. If an attacker can modify the trusted allowlist, the demonstrated boundary no longer holds.
