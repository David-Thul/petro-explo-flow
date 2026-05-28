# petro-explo-flow — Claude Context
**Company:** PetroLuminary
**Repo:** `/Users/davidthul/Documents/github/petro-explo-flow`
**Last updated:** 2026-04-07

---

## What This Is

**PetroExploFlow** is a petroleum exploration workflow reference implementation for PetroLuminary. It demonstrates best practices for subsurface data science — data extraction, structuring, and analysis for industry-standard workflows. Serves as an educational and standards reference that other PetroLuminary projects are expected to align with.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Environment | Conda (required, per environment.yml) |
| Data | Pandas, Polars |
| Geospatial | GeoPandas, PROJ |
| Well Logs | lasio, welly, dlisio, striplog, segyio |
| ML | scikit-learn |
| Dev | Jupyter, Pytest, Ruff |

---

## Architecture

```
data/           # Raw and processed data
  notebooks/    # Data used by notebooks
notebooks/      # Jupyter exploration notebooks
src/            # Reusable Python modules
tests/          # Pytest suite
```

---

## PetroLuminary Style Guide

This repo **is** the reference implementation of the PetroLuminary Style Guide. All patterns here are canonical:
- Python 3.12, conda environments
- pathlib for paths, Parquet for data storage
- Pandas (<1M rows) / Polars (>1M rows)
- Ruff linting, Pytest testing
- Type hints, reproducibility-first

---

## Current Status

Active. Used as educational reference and standards baseline for all PetroLuminary Python projects.

---

## Related Projects

- `regional-petrophysics` — Production workflow that follows this repo's patterns
- `well-analysis` — Modular well analysis utilities
- `facies-normalization` — Normalization utilities
- `loop-forward` — Python backend follows these standards

---

## Conventions

- Follow the PetroLuminary Style Guide to the letter
- Conda environment required — confirm naming with Dave
- snake_case, rev# versioning
