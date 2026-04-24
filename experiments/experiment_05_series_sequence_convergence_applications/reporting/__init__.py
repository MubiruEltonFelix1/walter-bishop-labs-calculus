"""
Reporting helpers for Experiment 05.
"""

from __future__ import annotations

from datetime import datetime


class ConvergenceReporter:
    """Generate text summary report for practical convergence/divergence outcomes."""

    def __init__(self):
        self.timestamp = datetime.now()

    def generate_summary(self, suggestions: list, sequence_results: list, series_results: list) -> str:
        lines = []
        lines.append("=" * 80)
        lines.append("EXPERIMENT 05: PRACTICAL CONVERGENCE AND DIVERGENCE - SUMMARY REPORT")
        lines.append("=" * 80)
        lines.append(f"Generated: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

        lines.append("\nSuggested practical mini-experiments considered:")
        for item in suggestions:
            lines.append(f"  {item['id']}. {item['title']}")
            lines.append(f"     Question: {item['question']}")

        lines.append("\n" + "=" * 80)
        lines.append("SEQUENCE CASES")
        lines.append("=" * 80)
        for item in sequence_results:
            lines.append(f"\nCase: {item['title']}")
            lines.append(f"  Application: {item['application']}")
            lines.append(f"  Expected behavior: {item['expected_behavior']}")
            lines.append(f"  Detected behavior: {item['detected_behavior']}")
            lines.append(f"  Initial term: {item['initial']:.6f}")
            lines.append(f"  Final term:   {item['final']:.6f}")
            if item.get('reference_value') is not None:
                lines.append(f"  Reference value: {item['reference_value']:.6f}")

        lines.append("\n" + "=" * 80)
        lines.append("SERIES CASES")
        lines.append("=" * 80)
        for item in series_results:
            lines.append(f"\nCase: {item['title']}")
            lines.append(f"  Application: {item['application']}")
            lines.append(f"  Expected behavior: {item['expected_behavior']}")
            lines.append(f"  Detected behavior: {item['detected_behavior']}")
            lines.append(f"  Last term magnitude: {item['last_term_abs']:.6f}")
            lines.append(f"  Final partial sum:   {item['final_partial_sum']:.6f}")
            if item.get('reference_value') is not None:
                lines.append(f"  Reference value:     {item['reference_value']:.6f}")

        lines.append("\n" + "=" * 80)
        lines.append("END OF REPORT")
        lines.append("=" * 80)

        return "\n".join(lines)
