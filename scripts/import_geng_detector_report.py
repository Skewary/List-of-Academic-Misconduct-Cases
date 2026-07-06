#!/usr/bin/env python3
"""Import a geng-academic-fraud-detector Markdown report as evidence drafts."""
from __future__ import annotations

import argparse
import csv
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL_NAME = "geng-academic-fraud-detector"
TOOL_REPO = "https://github.com/wooly99/geng-academic-fraud-detector"
REPORTS_CSV = ROOT / "data" / "tool_reports.csv"


def slugify(text: str) -> str:
    text = re.sub(r"[`*_：:，,。/\\]+", "-", text.strip().lower())
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "finding"


def extract_section(text: str, heading: str) -> str:
    pattern = rf"^##\s+{re.escape(heading)}\s*(.*?)(?=^##\s+|\Z)"
    match = re.search(pattern, text, flags=re.M | re.S)
    return match.group(1).strip() if match else ""


def extract_verdict(text: str) -> str:
    match = re.search(r"^##\s+综合评定[：:]?\s*(.*)$", text, flags=re.M)
    return match.group(1).strip() if match else "待人工确认"


def parse_findings(text: str) -> list[dict[str, str]]:
    detail = extract_section(text, "详细发现")
    if not detail:
        return []
    chunks = re.split(r"(?=^###\s+发现\s*\d+)", detail, flags=re.M)
    findings = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk.startswith("###"):
            continue
        title = re.sub(r"^###\s*", "", chunk.splitlines()[0]).strip()
        body = "\n".join(chunk.splitlines()[1:]).strip()
        fields = {}
        for key in ["位置", "描述", "证据", "判断逻辑", "严重程度"]:
            match = re.search(rf"^-\s*\*\*{key}\*\*[：:]\s*(.*)$", body, flags=re.M)
            fields[key] = match.group(1).strip() if match else "待人工补充"
        fields["title"] = title
        fields["body"] = body
        findings.append(fields)
    return findings


def append_report_row(row: dict[str, str]) -> None:
    exists = REPORTS_CSV.exists()
    with REPORTS_CSV.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "report_id", "tool_name", "tool_repo", "source_report_path", "person_id",
            "paper_id", "overall_verdict", "imported_evidence_path", "imported_at", "notes",
        ])
        if not exists or REPORTS_CSV.stat().st_size == 0:
            writer.writeheader()
        writer.writerow(row)


def write_evidence(person_id: str, paper_id: str, report_path: Path, verdict: str, findings: list[dict[str, str]]) -> Path:
    out_dir = ROOT / "people" / person_id / "evidence" / "geng-detector"
    out_dir.mkdir(parents=True, exist_ok=True)
    report_rel = report_path.resolve().relative_to(ROOT) if report_path.resolve().is_relative_to(ROOT) else report_path
    out_file = out_dir / f"{paper_id}-tool-report.md"
    lines = [
        f"# geng-academic-fraud-detector 导入报告：{paper_id}",
        "",
        f"- 工具：[{TOOL_NAME}]({TOOL_REPO})",
        f"- 原始报告：`{report_rel}`",
        f"- 关联人物：`{person_id}`",
        f"- 关联论文：`{paper_id}`",
        f"- 工具综合评定：{verdict}",
        "- 人工复核状态：待复核",
        "",
        "> 说明：本页是外部 AI 工具报告的兼容导入草稿，不等同于最终证据。每个发现仍需回到论文正文、补充材料或原始数据截图核对。",
        "",
        "## 发现列表",
        "",
    ]
    if not findings:
        lines.append("- 未解析到 `### 发现 N` 结构，请人工整理原始报告。")
    for idx, finding in enumerate(findings, 1):
        anchor = slugify(finding["title"])
        lines.extend([
            f"### {idx}. {finding['title']}",
            "",
            f"- 位置：{finding['位置']}",
            f"- 描述：{finding['描述']}",
            f"- 证据：{finding['证据']}",
            f"- 判断逻辑：{finding['判断逻辑']}",
            f"- 严重程度：{finding['严重程度']}",
            f"- 本地锚点：`#{anchor}`",
            "- 待补充：论文截图、补充材料文件名、原始数据定位、人工复核结论。",
            "",
        ])
    out_file.write_text("\n".join(lines), encoding="utf-8")
    return out_file


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="Path to geng-academic-fraud-detector Markdown report")
    parser.add_argument("--person-id", required=True)
    parser.add_argument("--paper-id", required=True)
    args = parser.parse_args()

    report_path = args.report
    text = report_path.read_text(encoding="utf-8")
    verdict = extract_verdict(text)
    findings = parse_findings(text)
    evidence_path = write_evidence(args.person_id, args.paper_id, report_path, verdict, findings)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    append_report_row({
        "report_id": f"{args.person_id}-{args.paper_id}-{now}",
        "tool_name": TOOL_NAME,
        "tool_repo": TOOL_REPO,
        "source_report_path": str(report_path),
        "person_id": args.person_id,
        "paper_id": args.paper_id,
        "overall_verdict": verdict,
        "imported_evidence_path": str(evidence_path.relative_to(ROOT)),
        "imported_at": now,
        "notes": f"parsed_findings={len(findings)}; requires manual paper-level verification",
    })
    print(f"Imported {len(findings)} findings to {evidence_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
