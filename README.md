# Agent-Vocabulary

Agent-Vocabulary is the machine-loadable list of words an AGenNext agent can understand.

It stores vocabulary as Schema.org `DefinedTermSet` and `DefinedTerm` seed data.

## Responsibility

```text
Agent-Vocabulary
  = words / terms
  = schema:DefinedTermSet
  = schema:DefinedTerm
```

## Not Owned Here

```text
Agent-Graph
  = relationships between words

Agent-Grammar
  = validation rules for CreativeWork artifacts

Prompt-Library
  = accepted prompt CreativeWork artifacts
```

## Current Seed Data

```text
seed/schemaorg/agent-vocabulary.jsonld
```

## Core Rule

A vocabulary word is represented as `schema:DefinedTerm`.

A vocabulary collection is represented as `schema:DefinedTermSet`.

Actual artifacts such as prompts, skills, API docs, blogs, and READMEs are not vocabulary words. They are `schema:CreativeWork` instances and must be validated by Agent-Grammar before being accepted into their target repository.

## Validate

```bash
python scripts/validate_jsonld.py
```
