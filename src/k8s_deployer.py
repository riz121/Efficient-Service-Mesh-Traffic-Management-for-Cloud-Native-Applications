"""
k8s_deployer.py
---------------
Example deploy adapter that applies YAML manifests to a Kubernetes cluster using kubectl.

Usage:
  python src/k8s_deployer.py --file config/virtual_service.yaml
"""

import argparse
import subprocess
from pathlib import Path


def kubectl_apply(yaml_text: str) -> None:
    proc = subprocess.run(
        ["kubectl", "apply", "-f", "-"],
        input=yaml_text.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8"))
    print(proc.stdout.decode("utf-8"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--file", required=True, help="Path to YAML to apply")
    args = p.parse_args()
    text = Path(args.file).read_text(encoding="utf-8")
    kubectl_apply(text)


if __name__ == "__main__":
    main()
