# Next experiments

To evaluate a real model, add a separate adapter that supplies a fixed user task and retrieved document, captures the model's proposed action, and submits it to the same gate. Keep API use opt-in and never execute the proposed action as part of evaluation.

Record model/version, prompt template, parameters, dataset version, raw proposed action, parsing failures, authorization decision, and expected outcome. Keep model attack-following rates separate from gate correctness. Include benign cases to measure unnecessary denials. Repeat trials to expose variation and report sample size and uncertainty.

The current eight cases are illustrative and hand-authored. There are no model inference results. Do not report their pass count as an injection-defense success rate.

Practice now: add a new tool and define its schema and permissions before implementing it; add tests for unknown fields and resource boundaries. Explain why a deny-by-default tool gate does not establish end-to-end security.
