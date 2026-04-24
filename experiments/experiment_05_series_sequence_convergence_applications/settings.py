"""
Configuration for Experiment 05: practical convergence and divergence of
sequences and series.
"""

# Suggested practical mini-experiments shown before execution.
SUGGESTED_EXPERIMENTS = [
    {
        "id": "A",
        "title": "Thermal stabilization in a cooling pipeline",
        "question": "Does the recursive temperature model settle to ambient?",
    },
    {
        "id": "B",
        "title": "Compound debt growth under monthly interest",
        "question": "How quickly does repeated multiplicative growth diverge?",
    },
    {
        "id": "C",
        "title": "Infinite discounted cash-flow valuation",
        "question": "When does a geometric cash-flow series converge to a finite value?",
    },
    {
        "id": "D",
        "title": "Accumulated overhead from repeated retries",
        "question": "Why can a harmonic-type accumulation diverge even with shrinking terms?",
    },
    {
        "id": "E",
        "title": "Alternating correction updates",
        "question": "How can alternating updates converge conditionally?",
    },
]

SEQUENCE_CASES = [
    {
        "key": "temperature_relaxation",
        "title": "Temperature stabilization sequence",
        "steps": 50,
        "initial": 95.0,
        "ambient": 22.0,
        "alpha": 0.82,
        "expected_behavior": "convergent",
        "application": "Cooling unit trend toward room temperature",
    },
    {
        "key": "compound_debt_growth",
        "title": "Compound debt growth sequence",
        "steps": 50,
        "initial": 1200.0,
        "growth_factor": 1.08,
        "expected_behavior": "divergent",
        "application": "Outstanding balance without repayment",
    },
]

SERIES_CASES = [
    {
        "key": "discounted_cashflow",
        "title": "Discounted cash-flow geometric series",
        "terms": 120,
        "payment": 1200.0,
        "discount_rate": 0.06,
        "expected_behavior": "convergent",
        "application": "Present value for perpetual annual cash flow",
    },
    {
        "key": "maintenance_backlog",
        "title": "Maintenance backlog harmonic series",
        "terms": 120,
        "base_cost": 100.0,
        "expected_behavior": "divergent",
        "application": "Cumulative overhead from repeated micro-fixes",
    },
    {
        "key": "alternating_correction",
        "title": "Alternating correction series",
        "terms": 120,
        "scale": 100.0,
        "expected_behavior": "convergent",
        "application": "Alternating over/under correction in control tuning",
    },
]

VISUALIZATION = {
    "plot_style": "seaborn-v0_8",
    "figure_dpi": 150,
    "figure_size": (12, 7),
    "animation_fps": 20,
}

REPORTING = {
    "summary_filename": "summary_report.txt",
}
