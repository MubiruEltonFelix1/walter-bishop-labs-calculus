"""
Smoke tests for Experiment 03: Integral Calculus

Quick validation that core functionality works.
"""

import sys
from pathlib import Path

# Add experiment to path
exp_path = Path(__file__).parent.parent / 'experiments' / 'experiment_03_integral_calculus'
sys.path.insert(0, str(exp_path))

import pytest
from integration import IntegrationEngine
from visualization import IntegrationVisualizer
from reporting import IntegrationReporter
import settings


class TestIntegrationEngine:
    """Test the core integration engine."""
    
    def setup_method(self):
        """Initialize engine for each test."""
        self.engine = IntegrationEngine()
    
    def test_indefinite_integral_basic(self):
        """Test basic indefinite integral computation."""
        result = self.engine.indefinite_integral_symbolic("x**2")
        assert result['success'], f"Failed to compute: {result.get('error')}"
        assert "x**3" in result['antiderivative'] or "x³" in result['antiderivative']
    
    def test_indefinite_integral_sin(self):
        """Test trigonometric indefinite integral."""
        result = self.engine.indefinite_integral_symbolic("sin(x)")
        assert result['success'], f"Failed: {result.get('error')}"
        assert "cos" in result['antiderivative']
    
    def test_definite_integral_linear(self):
        """Test definite integral of linear function."""
        result = self.engine.definite_integral_ftc("2*x", 0, 2)
        assert result['success'], f"Failed: {result.get('error')}"
        assert abs(result['result'] - 4.0) < 0.01, f"Expected 4, got {result['result']}"
    
    def test_definite_integral_quadratic(self):
        """Test definite integral of quadratic function."""
        result = self.engine.definite_integral_ftc("x**2", 0, 2)
        assert result['success'], f"Failed: {result.get('error')}"
        # ∫₀² x² dx = [x³/3]₀² = 8/3 ≈ 2.667
        assert abs(result['result'] - 8/3) < 0.01
    
    def test_riemann_left(self):
        """Test left Riemann sum approximation."""
        result = self.engine.riemann_left("x**2", 0, 2, 10)
        assert result['success'], f"Failed: {result.get('error')}"
        assert isinstance(result['result'], float)
        assert 2.0 < result['result'] < 3.0  # Should be around 8/3 ≈ 2.67
    
    def test_trapezoidal_rule(self):
        """Test trapezoidal rule approximation."""
        result = self.engine.trapezoidal_rule("x**2", 0, 2, 100)
        assert result['success'], f"Failed: {result.get('error')}"
        assert abs(result['result'] - 8/3) < 0.1  # Should be close to exact value
    
    def test_simpson_rule(self):
        """Test Simpson's rule approximation."""
        result = self.engine.simpson_rule("x**2", 0, 2, 100)
        assert result['success'], f"Failed: {result.get('error')}"
        assert abs(result['result'] - 8/3) < 0.01  # Very accurate
    
    def test_area_between_curves(self):
        """Test area between two curves."""
        result = self.engine.area_between_curves("x", "x**2", 0, 1)
        assert result['success'], f"Failed: {result.get('error')}"
        # Area between y=x and y=x² from 0 to 1 is 1/2 - 1/3 = 1/6 ≈ 0.167
        assert abs(result['area'] - 1/6) < 0.01
    
    def test_average_value(self):
        """Test average value of function."""
        result = self.engine.average_value("x**2", 0, 2)
        assert result['success'], f"Failed: {result.get('error')}"
        # Average of x² on [0,2] is (1/3) * (8/3) = 8/9 ≈ 0.889
        assert 0.8 < result['average'] < 1.0


class TestIntegrationVisualizer:
    """Test visualization functions."""
    
    def setup_method(self):
        """Initialize visualizer for each test."""
        self.viz = IntegrationVisualizer()
    
    def test_visualizer_instantiation(self):
        """Test that visualizer can be created."""
        assert self.viz is not None
        assert self.viz.dpi == 150
    
    def test_plot_function_callable(self):
        """Test that plot_function runs without error."""
        # Just test that it doesn't crash; we won't display plots in tests
        result = self.viz.plot_function("x**2", x_min=-2, x_max=2)
        # Result is (fig, ax) tuple; fig might be None if plotting failed
        assert result is not None


class TestIntegrationReporter:
    """Test report generation."""
    
    def setup_method(self):
        """Initialize reporter for each test."""
        self.reporter = IntegrationReporter()
    
    def test_reporter_instantiation(self):
        """Test that reporter can be created."""
        assert self.reporter is not None
        assert self.reporter.timestamp is not None
    
    def test_generate_summary_basic(self):
        """Test basic summary generation."""
        results = {
            'indefinite_integrals': [],
            'definite_integrals': [],
            'techniques': ['substitution', 'integration_by_parts'],
        }
        report = self.reporter.generate_summary(results)
        assert report is not None
        assert isinstance(report, str)
        assert len(report) > 0
        assert 'INTEGRAL CALCULUS' in report


class TestSettings:
    """Test configuration settings."""
    
    def test_settings_exist(self):
        """Test that all required settings are defined."""
        assert hasattr(settings, 'TEST_FUNCTIONS')
        assert hasattr(settings, 'TECHNIQUES')
        assert hasattr(settings, 'DEFINITE_INTEGRALS')
        assert hasattr(settings, 'AREA_BETWEEN_CURVES')
    
    def test_numerical_settings(self):
        """Test numerical integration settings."""
        assert settings.NUMERICAL_SETTINGS['trapezoid_n'] > 0
        assert settings.NUMERICAL_SETTINGS['simpson_n'] % 2 == 0  # Must be even
    
    def test_test_functions_not_empty(self):
        """Test that test functions are provided."""
        assert len(settings.TEST_FUNCTIONS) > 0
        assert isinstance(settings.TEST_FUNCTIONS[0], str)


if __name__ == '__main__':
    # Run tests with pytest if available, otherwise try basic execution
    try:
        pytest.main([__file__, '-v'])
    except ImportError:
        print("Running basic tests without pytest...")
        engine = IntegrationEngine()
        
        # Quick smoke tests
        print("Testing indefinite integral...", end=' ')
        result = engine.indefinite_integral_symbolic("x**2")
        print("✓" if result['success'] else "✗")
        
        print("Testing definite integral...", end=' ')
        result = engine.definite_integral_ftc("x**2", 0, 2)
        print("✓" if result['success'] else "✗")
        
        print("Testing trapezoidal rule...", end=' ')
        result = engine.trapezoidal_rule("x**2", 0, 2, 100)
        print("✓" if result['success'] else "✗")
        
        print("\nBasic tests completed.")
