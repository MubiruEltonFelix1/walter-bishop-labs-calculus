"""
Integration module for Experiment 03: Integral Calculus

Provides symbolic and numerical integration methods:
- Indefinite integrals (antiderivatives)
- Definite integrals (with Fundamental Theorem of Calculus)
- Numerical approximation methods (Riemann, Trapezoidal, Simpson's)
"""

import numpy as np
from sympy import symbols, integrate as symbolic_integrate, sympify
from sympy import limit, oo
import sympy as sp

x = symbols('x')


class IntegrationEngine:
    """Core integration engine with symbolic and numerical methods."""
    
    def __init__(self):
        """Initialize the integration engine."""
        self.x = x
    
    # ========== INDEFINITE INTEGRALS (Antiderivatives) ==========
    
    def indefinite_integral_symbolic(self, expression_str):
        """
        Find indefinite integral using SymPy.
        
        Args:
            expression_str: String representation of f(x)
        
        Returns:
            dict: {
                'expression': original expression,
                'antiderivative': F(x) + C,
                'latex': LaTeX representation
            }
        """
        try:
            expr = sympify(expression_str)
            antiderivative = symbolic_integrate(expr, self.x)
            
            return {
                'success': True,
                'expression': str(expr),
                'antiderivative': str(antiderivative),
                'latex_integrand': sp.latex(expr),
                'latex_antiderivative': sp.latex(antiderivative),
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    # ========== DEFINITE INTEGRALS ==========
    
    def definite_integral_ftc(self, expression_str, a, b):
        """
        Evaluate definite integral using Fundamental Theorem of Calculus.
        
        Args:
            expression_str: String representation of f(x)
            a: Lower limit
            b: Upper limit
        
        Returns:
            dict: {
                'result': numerical value,
                'antiderivative': F(x),
                'evaluation': F(b) - F(a),
                ...
            }
        """
        try:
            expr = sympify(expression_str)
            antiderivative = symbolic_integrate(expr, self.x)
            
            # Evaluate at bounds
            F = sp.lambdify(self.x, antiderivative, 'numpy')
            result = float(F(b) - F(a))
            
            return {
                'success': True,
                'expression': str(expr),
                'antiderivative': str(antiderivative),
                'lower_limit': a,
                'upper_limit': b,
                'result': result,
                'evaluation': f"F({b}) - F({a}) = {result}",
                'latex_antiderivative': sp.latex(antiderivative),
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    # ========== NUMERICAL INTEGRATION METHODS ==========
    
    def riemann_left(self, expression_str, a, b, n):
        """
        Approximate integral using left Riemann sum.
        
        Args:
            expression_str: String representation of f(x)
            a: Lower limit
            b: Upper limit
            n: Number of subintervals
        
        Returns:
            dict: {
                'method': 'Left Riemann Sum',
                'result': approximation,
                'n': n,
                'delta_x': width of each subinterval
            }
        """
        try:
            f = sp.lambdify(self.x, sympify(expression_str), 'numpy')
            delta_x = (b - a) / n
            x_values = np.linspace(a, b - delta_x, n)
            result = np.sum(f(x_values)) * delta_x
            
            return {
                'success': True,
                'method': 'Left Riemann Sum',
                'result': result,
                'n': n,
                'delta_x': delta_x,
                'bounds': (a, b),
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def riemann_right(self, expression_str, a, b, n):
        """Approximate integral using right Riemann sum."""
        try:
            f = sp.lambdify(self.x, sympify(expression_str), 'numpy')
            delta_x = (b - a) / n
            x_values = np.linspace(a + delta_x, b, n)
            result = np.sum(f(x_values)) * delta_x
            
            return {
                'success': True,
                'method': 'Right Riemann Sum',
                'result': result,
                'n': n,
                'delta_x': delta_x,
                'bounds': (a, b),
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def trapezoidal_rule(self, expression_str, a, b, n):
        """
        Approximate integral using trapezoidal rule.
        
        Formula: (Δx/2) * [f(x₀) + 2f(x₁) + 2f(x₂) + ... + 2f(xₙ₋₁) + f(xₙ)]
        """
        try:
            f = sp.lambdify(self.x, sympify(expression_str), 'numpy')
            delta_x = (b - a) / n
            x_values = np.linspace(a, b, n + 1)
            y_values = f(x_values)
            
            # Trapezoidal formula
            result = (delta_x / 2) * (y_values[0] + 2 * np.sum(y_values[1:-1]) + y_values[-1])
            
            return {
                'success': True,
                'method': 'Trapezoidal Rule',
                'result': result,
                'n': n,
                'delta_x': delta_x,
                'bounds': (a, b),
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def simpson_rule(self, expression_str, a, b, n):
        """
        Approximate integral using Simpson's rule.
        
        Requires n to be even.
        Formula: (Δx/3) * [f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ... + 4f(xₙ₋₁) + f(xₙ)]
        """
        try:
            if n % 2 != 0:
                n += 1  # Make it even
            
            f = sp.lambdify(self.x, sympify(expression_str), 'numpy')
            delta_x = (b - a) / n
            x_values = np.linspace(a, b, n + 1)
            y_values = f(x_values)
            
            # Simpson's formula: sum of odd indices * 4, even (interior) indices * 2
            result = (delta_x / 3) * (
                y_values[0] +
                4 * np.sum(y_values[1:-1:2]) +
                2 * np.sum(y_values[2:-1:2]) +
                y_values[-1]
            )
            
            return {
                'success': True,
                'method': "Simpson's Rule",
                'result': result,
                'n': n,
                'delta_x': delta_x,
                'bounds': (a, b),
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    # ========== APPLICATIONS ==========
    
    def area_between_curves(self, f_str, g_str, a, b):
        """
        Calculate area between two curves where f(x) >= g(x).
        
        A = ∫[a,b] [f(x) - g(x)] dx
        """
        try:
            f = sympify(f_str)
            g = sympify(g_str)
            difference = f - g
            result_integral = symbolic_integrate(difference, (self.x, a, b))
            result = float(result_integral)
            
            return {
                'success': True,
                'method': 'Area Between Curves',
                'f': str(f),
                'g': str(g),
                'bounds': (a, b),
                'area': result,
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def volume_disk_method(self, expression_str, a, b):
        """
        Volume by rotating around x-axis using disk method.
        
        V = π ∫[a,b] [f(x)]² dx
        """
        try:
            f = sympify(expression_str)
            integrand = sp.pi * f**2
            result_integral = symbolic_integrate(integrand, (self.x, a, b))
            result = float(result_integral)
            
            return {
                'success': True,
                'method': 'Volume (Disk Method)',
                'function': str(f),
                'bounds': (a, b),
                'volume': result,
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def work_done(self, force_str, a, b):
        """
        Work done by variable force.
        
        W = ∫[a,b] F(x) dx
        """
        try:
            f = sympify(force_str)
            result_integral = symbolic_integrate(f, (self.x, a, b))
            result = float(result_integral)
            
            return {
                'success': True,
                'method': 'Work Done',
                'force': str(f),
                'bounds': (a, b),
                'work': result,
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def average_value(self, expression_str, a, b):
        """
        Average value of function over interval.
        
        f_avg = (1/(b-a)) * ∫[a,b] f(x) dx
        """
        try:
            f = sympify(expression_str)
            integral = symbolic_integrate(f, (self.x, a, b))
            result = float(integral) / (b - a)
            
            return {
                'success': True,
                'method': 'Average Value',
                'function': str(f),
                'bounds': (a, b),
                'average': result,
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
