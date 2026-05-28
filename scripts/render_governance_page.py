#!/usr/bin/env python3
"""Generate a governance page for ciris.ai mapping controls to frameworks and vice versa.

Reads SEED_DIMENSIONS.yaml and produces a markdown page formatted for Fumadocs.
"""

import sys
import yaml
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SEED = REPO_ROOT / "SEED_DIMENSIONS.yaml"
DEFAULT_OUTPUT = REPO_ROOT / "governance.mdx"

def load_seed(path: Path) -> dict:
    with path.open() as f:
        return yaml.safe_load(f)

def safe_str(text) -> str:
    if text is None:
        return ""
    text_str = str(text)
    return text_str.replace('{', '&#123;').replace('}', '&#125;')

def render(seed_path: Path, output_path: Path) -> None:
    seed = load_seed(seed_path)

    batches_by_id = {b["id"]: b for b in seed["batches"]}
    dimensions = seed["dimensions"]

    out = []

    out.append("---")
    out.append("title: Governance Mapping")
    out.append("description: Mapping of CIRIS controls to senior governance frameworks and vice versa.")
    out.append("---")
    out.append("")
    out.append("# Governance Framework Mapping")
    out.append("")
    out.append("This page maps CIRIS controls (dimensions) to senior governance frameworks (batches) and vice versa, using our epistemic language (`wire_form`, primitives, and modalities).")
    out.append("")

    out.append("## Controls to Frameworks")
    out.append("")

    for dim in dimensions:
        out.append(f"### {dim['id']} — `{safe_str(dim['prefix'])}` ({dim['tier']})")
        out.append(f"*{safe_str(dim['gloss'])}*")
        out.append("")
        if 'wire_primitives' in dim and dim['wire_primitives']:
            out.append(f"**Wire Primitives**: {', '.join(f'`{safe_str(p)}`' for p in dim['wire_primitives'])}")
            out.append("")

        out.append("**Attesting Frameworks**:")
        out.append("")
        for ra in dim.get("regulatory_attestations", []):
            batch = batches_by_id.get(ra["batch_id"], {})
            bshort = batch.get("short", ra["batch_id"])
            btitle = batch.get("title", ra["batch_id"])
            out.append(f"- **{bshort}** ({btitle})")
            out.append(f"  - *Citation*: {safe_str(ra['citation'])}")
            out.append(f"  - *Language*: \"{safe_str(ra['language'])}\"")
            out.append(f"  - *Wire Form (Epistemic Language)*: `{safe_str(ra['wire_form'])}`")
        out.append("")

    out.append("## Frameworks to Controls")
    out.append("")

    for batch in seed["batches"]:
        out.append(f"### {batch['short']} — {batch['title']}")
        out.append(f"- **Authority**: {batch['authority']}")
        out.append(f"- **Publication Date**: {batch['publication_date']}")
        out.append(f"- **Institutional Shape**: {batch['institutional_shape']}")
        out.append("")
        out.append("**Attested Controls**:")
        out.append("")

        # Find dimensions attested by this batch
        attested_dims = []
        for dim in dimensions:
            for ra in dim.get("regulatory_attestations", []):
                if ra["batch_id"] == batch["id"]:
                    attested_dims.append((dim, ra))

        for dim, ra in attested_dims:
            out.append(f"- **{dim['id']}** (`{safe_str(dim['prefix'])}`)")
            out.append(f"  - *Wire Form*: `{safe_str(ra['wire_form'])}`")
        out.append("")

    output_path.write_text("\n".join(out) + "\n")
    print(f"Wrote {output_path}")

if __name__ == "__main__":
    seed_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SEED
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT
    render(seed_path, output_path)
