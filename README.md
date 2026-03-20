# test-repo-1

This repo contains a small Python subproject (`python-vuln-demo/`) with intentionally old dependency pins to help test vulnerability scanners.

## Python vuln demo

- **Location**: `python-vuln-demo/`
- **Dependencies**: `python-vuln-demo/requirements.txt` and `python-vuln-demo/pyproject.toml`

Run the demo (optional):

```bash
cd python-vuln-demo
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m vuln_demo.demo
```