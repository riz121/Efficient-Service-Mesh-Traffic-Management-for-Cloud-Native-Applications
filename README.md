# Efficient Service Mesh Traffic Management for Cloud-Native Applications

Reference repository for the manuscript **"Efficient Service Mesh Traffic Management for Cloud-Native Applications"**.

This repo contains:
- **Raw evaluation datasets** (CSV) to reproduce Figures 6–11
- **Reproducibility scripts** to regenerate plots
- **Sample metrics** and a small **MCG builder** example
- **Prototype code** for adaptive configuration generation

> **Note (prototype status):** This repository provides a research prototype and reproducibility artifacts.
> Deployment to Kubernetes/Istio is performed by generating YAML manifests and applying them using `kubectl apply`,
> or by integrating the deploy adapter with your control-plane workflow.

## Quick start

### 1) Install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Reproduce figures
```bash
python scripts/plot_fig6_response_time.py
python scripts/plot_fig7_no_traffic_mgmt.py
python scripts/plot_fig8_mcg_enabled.py
python scripts/plot_fig9_traffic_load.py
python scripts/plot_fig10_retry_timeout.py
python scripts/plot_fig11_resource_usage.py
```

### 3) Build a sample Microservice Communication Graph (MCG)
```bash
python src/mcg_builder.py
```

### 4) Generate adaptive configs from sample edge metrics
```bash
python src/mcg_config_generator_simple.py --edge_csv data/sample_metrics/edge_metrics.csv --out adaptive_config.yaml
```

## Repository structure
- `data/` – datasets used in the evaluation
- `data/sample_metrics/` – small example metrics to demo the MCG builder/config generator
- `scripts/` – figure reproduction scripts
- `src/` – prototype implementation code
- `config/` – example Istio YAML templates (DestinationRule / VirtualService)
