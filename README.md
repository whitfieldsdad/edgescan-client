# Edgescan API client

This is a Python client for the Edgescan API.

## Features

- Lookup, list, count, and export metadata related to assets, hosts, vulnerabilities, and services.
- Command line interface provides output in JSONL format for easy parsing.

## Usage

### Command line interface

To export all assets to a file named `data/assets.jsonl`

```bash
poetry run edgescan export assets data/assets.jsonl
```

To export all hosts to a file named `data/hosts.jsonl`

```bash
poetry run edgescan export hosts data/hosts.jsonl
```

To export all vulnerabilities to a file named `data/vulnerabilities.jsonl`

```bash
poetry run edgescan export vulnerabilities data/vulnerabilities.jsonl
```

To export all services to a file named `data/services.jsonl`

```bash
poetry run edgescan export services data/services.jsonl
```

To export all assets, hosts, vulnerabilities, services to a directory named `data/`:

```bash
poetry run edgescan export all data/
```
