"""
Reporting module for Experiment 03: Smart Mobility Energy and Load Accumulation.

Generates summary reports of applied integration analyses and results.
"""

from datetime import datetime


class IntegrationReporter:
    """Generate summary reports for applied integration experiments."""
    
    def __init__(self):
        """Initialize the reporter."""
        self.timestamp = datetime.now()
    
    def generate_summary(self, results, output_file=None):
        """
        Generate a text summary of integration experiment results.
        
        Args:
            results: Dictionary containing experiment results
            output_file: Optional file path to save report
        
        Returns:
            str: Formatted report text
        """
        report = []
        report.append("=" * 80)
        report.append("EXPERIMENT 03: SMART MOBILITY ENERGY AND LOAD ACCUMULATION - SUMMARY REPORT")
        report.append("=" * 80)
        report.append(f"Generated: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Indefinite Integrals Section
        if 'indefinite_integrals' in results:
            report.append("\n" + "=" * 80)
            report.append("1. MODEL PRIMITIVES (ANTIDERIVATIVES)")
            report.append("=" * 80)
            
            for item in results['indefinite_integrals']:
                if item.get('success'):
                    report.append(f"\nFunction: f(x) = {item['expression']}")
                    report.append(f"Antiderivative: F(x) = {item['antiderivative']} + C")
                else:
                    report.append(f"\nError computing integral: {item.get('error', 'Unknown error')}")
        
        # Definite Integrals Section
        if 'definite_integrals' in results:
            report.append("\n" + "=" * 80)
            report.append("2. RATE-TO-TOTAL ACCUMULATION (FTC)")
            report.append("=" * 80)
            
            for item in results['definite_integrals']:
                if item.get('success'):
                    report.append(f"\nFunction: f(x) = {item['expression']}")
                    report.append(f"Bounds: [{item['lower_limit']}, {item['upper_limit']}]")
                    report.append(f"Antiderivative: F(x) = {item['antiderivative']}")
                    report.append(f"Result: ∫f(x)dx from {item['lower_limit']} to {item['upper_limit']} = {item['result']:.6f}")
                else:
                    report.append(f"\nError computing definite integral: {item.get('error', 'Unknown error')}")
        
        # Numerical Integration Section
        if 'numerical_methods' in results:
            report.append("\n" + "=" * 80)
            report.append("3. NUMERICAL ESTIMATION RELIABILITY")
            report.append("=" * 80)
            
            methods = results['numerical_methods']
            report.append(f"\nFunction: f(x) = {methods.get('expression', 'N/A')}")
            report.append(f"Bounds: [{methods.get('a', 'N/A')}, {methods.get('b', 'N/A')}]")
            report.append(f"Number of subintervals: {methods.get('n', 'N/A')}")
            report.append("\nApproximations:")
            
            for method, result in methods.get('results', {}).items():
                if isinstance(result, (int, float)):
                    report.append(f"  {method:20s}: {result:.6f}")
        
        # Applications Section
        if 'applications' in results:
            report.append("\n" + "=" * 80)
            report.append("4. APPLIED ACCUMULATION SCENARIOS")
            report.append("=" * 80)
            
            apps = results['applications']
            
            if 'area_between_curves' in apps:
                report.append("\n4.1 Area Between Curves")
                for item in apps['area_between_curves']:
                    if item.get('success'):
                        report.append(f"  f(x) = {item['f']}, g(x) = {item['g']}")
                        report.append(f"  Bounds: [{item['bounds'][0]}, {item['bounds'][1]}]")
                        report.append(f"  Area = {item['area']:.6f}")
            
            if 'volume_revolution' in apps:
                report.append("\n4.2 Volume of Revolution")
                for item in apps['volume_revolution']:
                    if item.get('success'):
                        report.append(f"  f(x) = {item['function']}")
                        report.append(f"  Bounds: [{item['bounds'][0]}, {item['bounds'][1]}]")
                        report.append(f"  Volume = {item['volume']:.6f}")
            
            if 'work_done' in apps:
                report.append("\n4.3 Work Done by Variable Force")
                for item in apps['work_done']:
                    if item.get('success'):
                        report.append(f"  Force: F(x) = {item['force']}")
                        report.append(f"  Distance: [{item['bounds'][0]}, {item['bounds'][1]}]")
                        report.append(f"  Work = {item['work']:.6f} J")
            
            if 'average_value' in apps:
                report.append("\n4.4 Average Value of Functions")
                for item in apps['average_value']:
                    if item.get('success'):
                        report.append(f"  f(x) = {item['function']}")
                        report.append(f"  Interval: [{item['bounds'][0]}, {item['bounds'][1]}]")
                        report.append(f"  Average Value = {item['average']:.6f}")
        
        # Techniques Section
        if 'techniques' in results:
            report.append("\n" + "=" * 80)
            report.append("5. METHODS DEMONSTRATED")
            report.append("=" * 80)
            
            for technique in results['techniques']:
                report.append(f"  • {technique}")
        
        # Summary Statistics
        report.append("\n" + "=" * 80)
        report.append("SUMMARY STATISTICS")
        report.append("=" * 80)
        
        total_functions = 0
        successful = 0
        
        for key in ['indefinite_integrals', 'definite_integrals']:
            if key in results:
                for item in results[key]:
                    total_functions += 1
                    if item.get('success'):
                        successful += 1
        
        report.append(f"Total functions analyzed: {total_functions}")
        report.append(f"Successfully computed: {successful}")
        if total_functions > 0:
            report.append(f"Success rate: {100 * successful / total_functions:.1f}%")
        
        report.append("\n" + "=" * 80)
        report.append("END OF REPORT")
        report.append("=" * 80)
        
        report_text = "\n".join(report)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report_text)
        
        return report_text
