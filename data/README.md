# Experimental Dataset Description

This folder contains all CSV datasets used to generate the evaluation plots (Figures 6–11).

See `DATASET_INDEX.csv` for a mapping from paper figures to dataset files.

## Files (high level)
- `bookinfo_response_time.csv` — Fig. 6 average response time (Istio vs MCG) under 1/5/10 ms latency
- `bookinfo_latency_variation.csv` — per-run samples used to compute variability/error bars
- `ubbench_fault_injection.csv` — Fig. 7 default behavior under fault injection (no traffic mgmt)
- `circuit_breaker_results.csv` — Fig. 8 MCG + circuit breaking performance
- `traffic_load_results.csv` — Fig. 9 impact of inbound traffic (80/100/120%)
- `workload_spike_results.csv` — Fig. 10 workload spike and circuit breaker behavior
- `resource_efficiency_scalability.csv` — Fig. 11 CPU/memory/p95 comparison
