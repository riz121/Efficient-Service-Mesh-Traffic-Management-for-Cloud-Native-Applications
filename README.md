# Efficient Service Mesh Traffic Management for Cloud-Native Applications

Reference repository for the manuscript **"Efficient Service Mesh Traffic Management for Cloud-Native Applications"**.

## What this repository provides

This repository is intended for **(1) reproducibility of the paper’s figures** and **(2) inspection of a research prototype**.

It contains:
- **Raw evaluation datasets (CSV)** used to generate Figures 6–11 in the manuscript
- **Plotting + analysis scripts** to reproduce the performance graphs from the CSV files
- **Prototype Python modules** illustrating how we build an MCG snapshot and generate YAML-based traffic policies

✅ **You can reproduce the plots in the paper using the provided CSV data.**  
⚠️ **This repository is NOT a one-command framework for re-running the full live Kubernetes experiments end-to-end.**

---

## Important clarification (prototype scope)

The released code is a **research prototype** focusing on:
1) **MCG construction from telemetry snapshots** (represented as CSV in this artifact)  
2) **Graph-based scheduling decisions** (partitioning / placement logic)  
3) **Generating Istio traffic policy YAML** (e.g., DestinationRule / VirtualService)

The full live experiment pipeline in the paper additionally requires:
- A Kubernetes cluster and Istio service mesh installation
- Deployment of the Bookinfo / µBench workloads
- Prometheus metrics scraping + export from Envoy sidecars
- Fault injection / load generation (Locust / µBench)
- Capturing runtime metrics and exporting them to CSV for post-processing

To avoid confusion: the **Quick Start below demonstrates the offline prototype workflow** (MCG → YAML generation) and **figure reproduction**, not a fully automated “re-run all experiments” script.

---

## Quick start (offline reproducibility + prototype demo)

### 1) Create an environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Reproduce evaluation figures (Figures 6–11)
```bash
python scripts/plot_fig6_response_time.py
python scripts/plot_fig7_no_traffic_mgmt.py
python scripts/plot_fig8_mcg_enabled.py
python scripts/plot_fig9_traffic_load.py
python scripts/plot_fig10_retry_timeout.py
python scripts/plot_fig11_resource_usage.py
```

### 3) Demo: Build an MCG snapshot from sample metrics
```bash
python src/mcg_builder.py
```

### 4) Demo: Generate adaptive Istio config from sample edge metrics
```bash
python src/mcg_config_generator_simple.py --edge_csv data/sample_metrics/edge_metrics.csv --out adaptive_config.yaml
```

---

## High-level guide to re-running the live Kubernetes experiments (manual)

This section provides **high-level steps** describing how the experiments in the paper were executed.
Exact automation may vary depending on the cluster environment.

### A) Cluster prerequisites
- Kubernetes (tested with v1.20)
- Istio (tested with v1.8.x)
- Prometheus (scraping Envoy proxy metrics)
- (Optional) Grafana for dashboards

### B) Install Istio and enable sidecar injection
1. Install Istio into the cluster (default profile is sufficient for this prototype).
2. Enable automatic sidecar injection for your namespace:
```bash
kubectl label namespace default istio-injection=enabled
```

### C) Deploy the Bookinfo application
Bookinfo is the reference microservice workload used in Section 4.1:
```bash
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.8/samples/bookinfo/platform/kube/bookinfo.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.8/samples/bookinfo/networking/bookinfo-gateway.yaml
```
Then validate services/pods:
```bash
kubectl get pods
kubectl get svc
```

### D) Apply example traffic policies (Istio YAML)
Example templates are provided in `config/`. You can apply them using:
```bash
kubectl apply -f config/destination_rule.yaml
kubectl apply -f config/virtual_service.yaml
```

### E) Load generation and metrics capture
- Use **Locust** to generate workload traffic (Section 4.1).
- Use **Prometheus** to scrape Envoy telemetry (request rate, latency, error rate).
- Export the captured metrics into CSV files (response time / throughput / CPU & memory)
- The exported CSV files should match the schema of the datasets in `data/`.

### F) Reproduce plots from exported data
Once you export your own CSV data, you can regenerate plots using the scripts in `scripts/`.

---

## Repository structure
- `data/` – datasets used in the evaluation section
- `data/sample_metrics/` – small example metrics used for prototype demos
- `scripts/` – figure reproduction scripts
- `src/` – prototype implementation code
- `config/` – example Istio YAML templates (DestinationRule / VirtualService)

## License
MIT License.
