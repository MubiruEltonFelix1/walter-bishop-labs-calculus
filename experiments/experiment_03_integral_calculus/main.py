"""
Experiment 03: Smart Mobility Energy and Load Accumulation
Main experiment script that orchestrates applied integration analyses.

This script demonstrates:
- Rate-to-total accumulation with definite integrals
- Numerical method comparison (Riemann, Trapezoidal, Simpson's)
- Practical applied outputs (area, volume, work, average value)
"""

import os
import sys
from pathlib import Path
import matplotlib.pyplot as plt

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from integration import IntegrationEngine
from visualization import IntegrationVisualizer
from reporting import IntegrationReporter
import settings


def setup_output_directories():
    """Create output directories if they don't exist."""
    plots_dir = Path(__file__).parent / 'outputs' / 'plots'
    reports_dir = Path(__file__).parent / 'outputs' / 'reports'
    
    plots_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    return plots_dir, reports_dir


def run_indefinite_integrals(engine):
    """Compute indefinite integrals for test functions."""
    print("\n" + "="*80)
    print("1. MODEL PRIMITIVES (ANTIDERIVATIVES)")
    print("="*80)
    
    results = []
    for func_str in settings.TEST_FUNCTIONS[:4]:  # Run first 4 for demo
        print(f"\nComputing: ∫ ({func_str}) dx")
        result = engine.indefinite_integral_symbolic(func_str)
        
        if result['success']:
            print(f"  Antiderivative: {result['antiderivative']} + C")
        else:
            print(f"  Error: {result['error']}")
        
        results.append(result)
    
    return results


def run_definite_integrals(engine):
    """Compute definite integrals using FTC."""
    print("\n" + "="*80)
    print("2. RATE-TO-TOTAL ACCUMULATION (FTC)")
    print("="*80)
    
    results = []
    for integral in settings.DEFINITE_INTEGRALS[:3]:  # Run first 3 for demo
        func = integral['function']
        a, b = integral['a'], integral['b']
        
        print(f"\nComputing: ∫({func}) dx from {a} to {b}")
        result = engine.definite_integral_ftc(func, a, b)
        
        if result['success']:
            print(f"  Antiderivative: {result['antiderivative']}")
            print(f"  Result: {result['result']:.6f}")
        else:
            print(f"  Error: {result['error']}")
        
        results.append(result)
    
    return results


def run_numerical_integration(engine, plots_dir):
    """Compare numerical integration methods."""
    print("\n" + "="*80)
    print("3. NUMERICAL ESTIMATION RELIABILITY")
    print("="*80)
    
    test_func = "x**2 + 1"
    a, b = 0, 2
    n = 50
    
    print(f"\nFunction: f(x) = {test_func}")
    print(f"Bounds: [{a}, {b}], Subintervals: {n}")
    
    # Symbolic result for comparison
    engine_sym = IntegrationEngine()
    sym_result = engine_sym.definite_integral_ftc(test_func, a, b)
    exact = sym_result.get('result') if sym_result.get('success') else None
    print(f"Exact (symbolic): {exact:.6f}")
    
    # Numerical methods
    results = {}
    
    left = engine.riemann_left(test_func, a, b, n)
    results['Left Riemann'] = left['result']
    print(f"Left Riemann:     {left['result']:.6f}")
    
    right = engine.riemann_right(test_func, a, b, n)
    results['Right Riemann'] = right['result']
    print(f"Right Riemann:    {right['result']:.6f}")
    
    trap = engine.trapezoidal_rule(test_func, a, b, n)
    results['Trapezoidal'] = trap['result']
    print(f"Trapezoidal:      {trap['result']:.6f}")
    
    simp = engine.simpson_rule(test_func, a, b, n)
    results['Simpson\'s'] = simp['result']
    print(f"Simpson's:        {simp['result']:.6f}")
    
    return {
        'expression': test_func,
        'a': a,
        'b': b,
        'n': n,
        'exact': exact,
        'results': results
    }


def run_applications(engine, plots_dir):
    """Demonstrate integration applications."""
    print("\n" + "="*80)
    print("4. APPLIED ACCUMULATION SCENARIOS")
    print("="*80)
    
    results = {'area': [], 'volume': [], 'work': [], 'average': []}
    
    # Area between curves
    print("\nArea Between Curves:")
    for curves in settings.AREA_BETWEEN_CURVES:
        f, g, a, b = curves['f'], curves['g'], curves['a'], curves['b']
        result = engine.area_between_curves(f, g, a, b)
        
        if result['success']:
            print(f"  Area between y={f} and y={g} from x={a} to x={b}")
            print(f"  Result: {result['area']:.6f}")
            results['area'].append(result)
    
    # Volume of revolution
    print("\nVolume of Revolution (Disk Method):")
    for vol in settings.VOLUME_REVOLUTION:
        func, a, b = vol['function'], vol['a'], vol['b']
        result = engine.volume_disk_method(func, a, b)
        
        if result['success']:
            print(f"  Rotate y={func} around x-axis from x={a} to x={b}")
            print(f"  Volume: {result['volume']:.6f}")
            results['volume'].append(result)
    
    # Work done
    print("\nWork Done by Variable Force:")
    for work in settings.WORK_EXAMPLES:
        force, a, b = work['force'], work['a'], work['b']
        result = engine.work_done(force, a, b)
        
        if result['success']:
            print(f"  Force F(x) = {force} from x={a} to x={b}")
            print(f"  Work: {result['work']:.6f} J")
            results['work'].append(result)
    
    # Average value
    print("\nAverage Value of Functions:")
    for curves in settings.AREA_BETWEEN_CURVES:
        f, a, b = curves['f'], curves['a'], curves['b']
        result = engine.average_value(f, a, b)
        
        if result['success']:
            print(f"  Average of f(x) = {f} on [{a}, {b}]")
            print(f"  f_avg: {result['average']:.6f}")
            results['average'].append(result)
    
    return results


def generate_visualizations(engine, viz, plots_dir):
    """Create plots for key concepts."""
    print("\n" + "="*80)
    print("5. VISUAL EVIDENCE AND INTERPRETATION")
    print("="*80)
    print("Close each plot window to see the next one...\n")
    
    # Plot 1: Function with definite integral
    print("[1/5] Plotting definite integral...")
    viz.plot_definite_integral(
        "x**2",
        a=0,
        b=2,
        x_min=-0.5,
        x_max=2.5,
        title="Definite Integral: Area under y = x²",
        filename=str(plots_dir / "01_definite_integral.png")
    )
    plt.show(block=True)
    plt.close('all')
    print("     ✓ Closed. Moving to next plot...\n")
    
    # Plot 2: Area between curves
    print("[2/5] Plotting area between curves...")
    viz.plot_area_between_curves(
        "x",
        "x**2",
        a=0,
        b=1,
        x_min=-0.1,
        x_max=1.1,
        title="Area Between y = x and y = x²",
        filename=str(plots_dir / "02_area_between_curves.png")
    )
    plt.show(block=True)
    plt.close('all')
    print("     ✓ Closed. Moving to next plot...\n")
    
    # Plot 3: Riemann sum
    print("[3/5] Plotting Riemann sum approximation (Left)...")
    viz.plot_riemann_sum(
        "x**2 + 1",
        a=0,
        b=2,
        n=8,
        method='left',
        title="Left Riemann Sum (n=8)",
        filename=str(plots_dir / "03_riemann_sum_left.png")
    )
    plt.show(block=True)
    plt.close('all')
    print("     ✓ Closed. Moving to next plot...\n")
    
    # Plot 4: Riemann sum right
    print("[4/5] Plotting Riemann sum approximation (Right)...")
    viz.plot_riemann_sum(
        "x**2 + 1",
        a=0,
        b=2,
        n=8,
        method='right',
        title="Right Riemann Sum (n=8)",
        filename=str(plots_dir / "04_riemann_sum_right.png")
    )
    plt.show(block=True)
    plt.close('all')
    print("     ✓ Closed. Moving to next plot...\n")
    
    # Plot 5: Numerical method comparison
    print("[5/5] Plotting numerical method convergence...")
    viz.plot_numerical_comparison(
        "x**2 + 1",
        a=0,
        b=2,
        exact_value=8.666667,  # Symbolic result: 8 + 2/3
        filename=str(plots_dir / "05_numerical_convergence.png")
    )
    plt.show(block=True)
    plt.close('all')
    print("     ✓ Closed.\n")
    
    print("="*80)
    print("✓ All visualizations saved to", plots_dir)
    print("="*80)


def main():
    """Run the complete applied integration experiment."""
    print("\n" + "="*80)
    print("EXPERIMENT 03: SMART MOBILITY ENERGY AND LOAD ACCUMULATION")
    print("="*80)
    print("Using integration to convert rate signals into operational totals")
    
    # Setup
    plots_dir, reports_dir = setup_output_directories()
    engine = IntegrationEngine()
    viz = IntegrationVisualizer()
    reporter = IntegrationReporter()
    
    # Run analyses
    indefinite = run_indefinite_integrals(engine)
    definite = run_definite_integrals(engine)
    numerical = run_numerical_integration(engine, plots_dir)
    applications = run_applications(engine, plots_dir)
    
    # Generate visualizations
    generate_visualizations(engine, viz, plots_dir)
    
    # Generate report
    print("\n" + "="*80)
    print("GENERATING APPLIED SUMMARY REPORT")
    print("="*80)
    
    report_data = {
        'indefinite_integrals': indefinite,
        'definite_integrals': definite,
        'numerical_methods': numerical,
        'applications': applications,
        'techniques': settings.TECHNIQUES,
    }
    
    report_text = reporter.generate_summary(report_data)
    
    report_file = reports_dir / 'summary_report.txt'
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report_text)
    
    print(f"\n✓ Report saved to {report_file}")
    
    # Print summary
    print("\n" + "="*80)
    print("EXPERIMENT COMPLETE")
    print("="*80)
    print(f"📊 Plots saved to:    {plots_dir}")
    print(f"📄 Reports saved to:  {reports_dir}")
    print("\nKey Results:")
    print(f"  • Computed {len(indefinite)} indefinite integrals")
    print(f"  • Computed {len(definite)} definite integrals")
    print(f"  • Compared {len(numerical['results'])} numerical methods")
    print(f"  • Demonstrated {len(applications['area']) + len(applications['volume'])} applications")
    print("\nNext Steps:")
    print("  1. Open outputs/plots/ to review visualizations")
    print("  2. Read outputs/reports/summary_report.txt for detailed results")
    print("  3. Modify settings.py to run custom variations")
    print("  4. Explore the integration module for more techniques")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error running experiment: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
