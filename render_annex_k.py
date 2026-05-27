#!/usr/bin/env python3
"""Deterministic render of SEED_DIMENSIONS.yaml -> ANNEX_K.md.

The output is committed alongside the seed so reviewers see the rendered
Annex K text without running the script. The script is the source of
truth for the render; do not hand-edit ANNEX_K.md.

Usage: python3 render_annex_k.py [seed_path] [output_path]
"""

from __future__ import annotations

import hashlib
import sys
from datetime import date
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent
DEFAULT_SEED = REPO_ROOT / "SEED_DIMENSIONS.yaml"
DEFAULT_OUTPUT = REPO_ROOT / "ANNEX_K.md"

PRINCIPLE_ORDER = ["beneficence", "non_maleficence", "integrity", "fidelity", "autonomy", "justice"]
PRINCIPLE_TITLE = {
    "beneficence": "Beneficence",
    "non_maleficence": "Non-Maleficence",
    "integrity": "Integrity",
    "fidelity": "Fidelity",
    "autonomy": "Autonomy",
    "justice": "Justice",
}


def load_seed(path: Path) -> dict:
    with path.open() as f:
        return yaml.safe_load(f)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def conflicts_for_dimension(seed: dict, dim_id: str) -> list[dict]:
    return [c for c in seed["aggregate_indices"]["conflicts_surfaced"] if dim_id in c.get("dimensions", [])]


def t3_candidates_for_dimension(seed: dict, dim_id: str) -> list[dict]:
    return [t for t in seed["aggregate_indices"]["t3_candidates_v1_5"] if t.get("affects_dimension") == dim_id]


def render_dimension(dim: dict, batches_by_id: dict, seed: dict) -> list[str]:
    lines: list[str] = []
    lines.append(f"#### {dim['id']} — `{dim['prefix']}` ({dim['tier']})")
    lines.append("")
    lines.append(f"*{dim['gloss']}*")
    lines.append("")
    counts = dim["attestations"]
    lines.append(
        f"**Attestation density**: MH={counts['MH']} · EU={counts['EU']} · "
        f"IEEE={counts['IEEE']} · ASEAN={counts['ASEAN']} · "
        f"total={counts['total']}"
    )
    lines.append("")
    absent_blocks = dim.get("absent_batch") or []
    if absent_blocks:
        for ab in absent_blocks:
            bshort = batches_by_id.get(ab["batch_id"], {}).get("short", ab["batch_id"])
            lines.append(f"**Absent from**: {bshort} — {ab['absence_note']}")
            if ab.get("functional_analogue"):
                lines.append(f"  *Functional analogue*: {ab['functional_analogue']}")
            lines.append("")

    lines.append("**Regulatory attestations**:")
    lines.append("")
    for ra in dim["regulatory_attestations"]:
        b = batches_by_id.get(ra["batch_id"], {})
        bshort = b.get("short", ra["batch_id"])
        btitle = b.get("title", ra["batch_id"])
        lines.append(f"- **{bshort}** ({btitle}) — *{ra['citation']}*")
        lines.append(f'    > "{ra["language"]}"')
        lines.append(f"    Wire form: `{ra['wire_form']}`")
    lines.append("")

    lines.append("**Wire primitives**: " + ", ".join(f"`{p}`" for p in dim["wire_primitives"]))
    lines.append("")

    note = dim.get("convergence_note")
    if note:
        lines.append(f"**Convergence note**: {note}")
        lines.append("")

    conflicts = conflicts_for_dimension(seed, dim["id"])
    if conflicts:
        lines.append("**Conflicts involving this dimension**:")
        for c in conflicts:
            lines.append(
                f"- *{c['id']}* ({c['type']}, severity {c['severity']}): {c['claim']}"
            )
            if c.get("disposition"):
                lines.append(f"    Disposition: {c['disposition']}")
        lines.append("")

    t3s = t3_candidates_for_dimension(seed, dim["id"])
    if t3s:
        lines.append("**v1.5+ T-3 candidates affecting this dimension**:")
        for t in t3s:
            lines.append(
                f"- *{t['id']}* `{t['proposed_prefix']}` (priority {t['priority']})"
            )
        lines.append("")

    return lines


def render_principle_section(
    principle_key: str, dim_ids: list[str], dimensions_by_id: dict, batches_by_id: dict, seed: dict
) -> list[str]:
    lines: list[str] = []
    lines.append(f"### K.{PRINCIPLE_ORDER.index(principle_key) + 1} — {PRINCIPLE_TITLE[principle_key]}")
    lines.append("")
    lines.append(f"**Operative dimensions**: {', '.join(dim_ids)}")
    lines.append("")
    for dim_id in dim_ids:
        dim = dimensions_by_id[dim_id]
        lines.extend(render_dimension(dim, batches_by_id, seed))
    return lines


def render(seed_path: Path, output_path: Path) -> None:
    seed = load_seed(seed_path)
    seed_sha = file_sha256(seed_path)
    seed_version = seed["metadata"]["seed_version"]

    batches_by_id = {b["id"]: b for b in seed["batches"]}
    dimensions_by_id = {d["id"]: d for d in seed["dimensions"]}
    by_principle = seed["aggregate_indices"]["by_accord_principle"]

    out: list[str] = []
    out.append(f"# Annex K — Regulatory Cross-Walk")
    out.append("")
    out.append(
        f"> Auto-generated from `SEED_DIMENSIONS.yaml` "
        f"(seed_version {seed_version}, sha256 `{seed_sha[:16]}...`) "
        f"by `render_annex_k.py` on {date.today().isoformat()}. "
        "Do not hand-edit; regenerate from the seed instead."
    )
    out.append("")
    out.append("---")
    out.append("")

    out.append("## Preamble")
    out.append("")
    out.append(
        "The Accord is one expression of principles that are independently "
        "articulated by senior secular and religious governance frameworks. "
        "Annex K catalogs this convergence: for each of the six Accord "
        "principles, the operative dimensions through which the principle "
        "is implemented in the federation, and the parent regulatory "
        "frameworks that independently attest each dimension."
    )
    out.append("")
    out.append(
        "**What Annex K is**: structural evidence that the Accord's principle "
        "scaffolding is not an artifact of any one tradition."
    )
    out.append("")
    out.append("**What Annex K is NOT**:")
    out.append(
        "- It does NOT bind the Accord to external regulatory frameworks. "
        "The Accord's principles are CIRIS's own; the cross-walk is "
        "structural evidence of convergence, not delegation of authority."
    )
    out.append(
        "- It does NOT silently average the parent sources. Per Phase 4 "
        "translation-quality calibration (`TRANSLATION_QUALITY_AUDIT_SYNTHESIS.md`), "
        "modal-strength compression and softness-erosion are real translation "
        "costs; Annex K names the convergence on *structural concern*, not "
        "propositional equivalence."
    )
    out.append(
        "- It does NOT supersede the operative Accord principles. The "
        "principles remain the load-bearing claim; the cross-walk is "
        "supporting structural evidence."
    )
    out.append("")

    out.append("## Corpus")
    out.append("")
    out.append("| Batch | Shape | Jurisdiction | Date | Title |")
    out.append("|---|---|---|---|---|")
    for b in seed["batches"]:
        out.append(
            f"| `{b['id']}` | {b['institutional_shape']} | "
            f"{b['geographic_scope']} | {b['publication_date']} | {b['title']} |"
        )
    out.append("")

    totals = seed["metadata"]["totals"]
    out.append(
        f"**Totals**: {totals['dimensions']} dimensions "
        f"({totals['strong_4']} STRONG-4 + {totals['strong_3']} STRONG-3) · "
        f"{totals['total_attestations']} attestations · "
        f"{totals['batches_in_corpus']} batches in corpus."
    )
    out.append("")

    out.append("---")
    out.append("")
    out.append("## K — Cross-walk by Accord principle")
    out.append("")

    for principle_key in PRINCIPLE_ORDER:
        dim_ids = sorted(by_principle.get(principle_key, []))
        out.extend(
            render_principle_section(
                principle_key, dim_ids, dimensions_by_id, batches_by_id, seed
            )
        )

    out.append("---")
    out.append("")
    out.append("## Cross-source conflicts surfaced")
    out.append("")
    out.append(
        "All cross-source conflicts catalogued during the trio mapping. "
        "Per `GOVERNANCE_FABRIC_MAPPING_STANDARD §5`, the wire format does "
        "not silently average; conflicts are surfaced explicitly with "
        "documented disposition."
    )
    out.append("")
    out.append("| ID | Type | Severity | Sources | Dimensions | Claim |")
    out.append("|---|---|---|---|---|---|")
    for c in seed["aggregate_indices"]["conflicts_surfaced"]:
        srcs = ", ".join(c.get("sources") or [])
        dims = ", ".join(c.get("dimensions") or []) or "—"
        out.append(
            f"| {c['id']} | {c['type']} | {c['severity']} | {srcs} | {dims} | {c['claim']} |"
        )
    out.append("")

    out.append("## v1.5+ T-3 candidates surfaced")
    out.append("")
    out.append(
        "Per `GOVERNANCE_FABRIC_MAPPING_STANDARD §7.5 + §6`. Filed at "
        "[CIRISRegistry#20](https://github.com/CIRISAI/CIRISRegistry/issues/20)."
    )
    out.append("")
    out.append("| ID | Proposed prefix | Priority | Sources |")
    out.append("|---|---|---|---|")
    for t in seed["aggregate_indices"]["t3_candidates_v1_5"]:
        srcs = ", ".join(t.get("source") or [])
        out.append(
            f"| {t['id']} | `{t['proposed_prefix']}` | {t['priority']} | {srcs} |"
        )
    out.append("")

    out.append("---")
    out.append("")
    out.append("## Update discipline")
    out.append("")
    out.append(
        "When a new senior governance framework is mapped per "
        "`GOVERNANCE_FABRIC_MAPPING_STANDARD.md`:"
    )
    out.append("")
    out.append("1. Run Phase 1–4 per the standard.")
    out.append("2. Update `SEED_DIMENSIONS.yaml` (add to `batches[]`, update affected dimensions' `regulatory_attestations[]`, promote tier where applicable, allocate D28+ for any newly surfaced dimensions).")
    out.append("3. Re-run `render_annex_k.py` to regenerate this file.")
    out.append("4. Stable IDs (D01-D27, D28+) ensure runtime evidence_refs and Accord citations remain valid across seed revisions.")
    out.append("")

    output_path.write_text("\n".join(out) + "\n")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    seed_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SEED
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT
    render(seed_path, output_path)
