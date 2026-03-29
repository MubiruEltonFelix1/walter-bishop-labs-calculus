"""
Configuration settings for Experiment 03: Integral Calculus

This module defines all configurable parameters for exploring integration
techniques, definite integrals, and applications of integration.
"""

# Integration Methods
INTEGRATION_METHODS = {
    'symbolic': True,       # Use symbolic integration (SymPy)
    'numerical': True,      # Use numerical approximation
}

# Numerical Integration Parameters
NUMERICAL_SETTINGS = {
    'trapezoid_n': 100,     # Number of subintervals for trapezoidal rule
    'simpson_n': 100,       # Number of subintervals for Simpson's rule (must be even)
    'left_riemann_n': 100,
    'right_riemann_n': 100,
}

# Function Exploration Parameters
FUNCTION_SETTINGS = {
    'x_min': -2.0,
    'x_max': 5.0,
    'x_points': 1000,       # Points for plotting smooth curves
    'a': 0.0,               # Lower integration limit (default)
    'b': 2.0,               # Upper integration limit (default)
}

# Visualization Settings
VISUALIZATION = {
    'plot_style': 'seaborn-v0_8',    # Matplotlib style
    'figure_dpi': 150,
    'figure_size': (12, 8),
    'show_grid': True,
    'color_under_curve': '#3498db',   # Blue
    'color_between_curves': '#e74c3c',  # Red
}

# Applications to Explore
APPLICATIONS = {
    'area_between_curves': True,
    'volume_of_revolution': True,
    'work_and_force': True,
    'average_value': True,
}

# Report Settings
REPORTING = {
    'generate_summary': True,
    'save_plots': True,
    'output_format': 'txt',  # 'txt' or 'pdf'
}

# Tests and Exercises
TEST_FUNCTIONS = [
    '3*x**2 + 2*x + 1',           # Polynomial
    'sin(x)',                       # Trigonometric
    'x*exp(x)',                     # Product - integration by parts
    'x**2 * cos(x)',                # Integration by parts
    '1/(x**2 - 1)',                 # Partial fractions
    'sqrt(1 - x**2)',               # Trig substitution
    'x / (x**2 + 1)',               # Substitution
    'exp(-x**2)',                   # Improper integral (no elementary antiderivative)
]

# Techniques to Demonstrate
TECHNIQUES = [
    'basic_rules',
    'substitution',
    'integration_by_parts',
    'trigonometric_integrals',
    'trigonometric_substitution',
    'partial_fractions',
    'improper_integrals',
    'numerical_methods',
]

# Definite Integral Test Cases
DEFINITE_INTEGRALS = [
    {'function': '2*x + 1', 'a': 1, 'b': 3},
    {'function': 'x**3', 'a': 0, 'b': 2},
    {'function': '1/x', 'a': 1, 'b': 2.718},  # e ≈ 2.718
    {'function': 'sin(x)', 'a': 0, 'b': 3.14159},  # π
    {'function': 'exp(2*x)', 'a': 0, 'b': 1},
]

# FTC (Fundamental Theorem of Calculus) Examples
FTC_EXAMPLES = [
    {'function': 'x**2 + 1', 'a': 0, 'b': 2},
    {'function': 'cos(x)', 'a': 0, 'b': 1.5708},  # π/2
    {'function': '1/(1 + x**2)', 'a': 0, 'b': 1},
]

# Application Examples
AREA_BETWEEN_CURVES = [
    {'f': 'x', 'g': 'x**2', 'a': 0, 'b': 1},      # Area between y=x and y=x^2
    {'f': 'sin(x)', 'g': 'cos(x)', 'a': 0, 'b': 0.7854},  # π/4
]

VOLUME_REVOLUTION = [
    {'function': 'x', 'a': 0, 'b': 2, 'axis': 'x'},  # Rotate y=x around x-axis
    {'function': 'sqrt(x)', 'a': 0, 'b': 1, 'axis': 'x'},
]

WORK_EXAMPLES = [
    {'force': '5*x', 'a': 0, 'b': 4},              # F(x) = 5x
    {'force': '10*x', 'a': 0, 'b': 0.3},           # Hooke's law: spring force
]
