# Conda Environment Registry
*PetroLuminary — petro-explo-flow*
*Last updated: 2026-04-24*

---

## Active Environments

### `petro-explo-flow`
| Field | Value |
|---|---|
| **Status** | Active |
| **Python** | 3.12 |
| **Purpose** | Petroleum exploration workflow — LAS/DLIS/SEG-Y ingest, facies/classification, notebook-driven analysis |
| **Spec file** | `environment.yml` |

**Key packages:**
| Package | Role |
|---|---|
| pandas, polars | Tabular data (polars for large-scale column work) |
| geopandas | Spatial data |
| lasio, welly | LAS parsing + well-centric log handling |
| scikit-learn | Classification / clustering for facies work |
| jupyter, notebook | Notebook runtime |
| pytest, ruff | Dev tooling |
| dlisio (pip) | DLIS log parsing |
| striplog (pip) | Stratigraphic intervals |
| segyio (pip) | SEG-Y seismic I/O |

**Create / activate:**
```bash
conda env create -f environment.yml
conda activate petro-explo-flow
```

---

## Notes

- **Never use the base conda environment.** Always create and activate the named env.
