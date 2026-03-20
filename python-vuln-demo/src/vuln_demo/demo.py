from __future__ import annotations

import json
from dataclasses import dataclass

import requests
import yaml
from jinja2 import Template


@dataclass(frozen=True)
class DemoResult:
    fetched_status: int
    parsed_yaml_keys: list[str]
    rendered: str


def run_demo() -> DemoResult:
    """
    Minimal code path that imports and uses third-party dependencies.

    This project intentionally pins old dependency versions in order to
    exercise vulnerability scanners against realistic usage.
    """

    resp = requests.get("https://example.com", timeout=5)

    data = yaml.safe_load(
        """
        app:
          name: vuln-demo
          enabled: true
        """
    )

    template = Template("name={{ name }}, enabled={{ enabled }}")
    rendered = template.render(**data["app"])

    # Ensure a tiny bit of structured output for sanity checks.
    _ = json.dumps({"status": resp.status_code, "rendered": rendered})

    return DemoResult(
        fetched_status=int(resp.status_code),
        parsed_yaml_keys=sorted(list(data["app"].keys())),
        rendered=rendered,
    )


if __name__ == "__main__":
    print(run_demo())
