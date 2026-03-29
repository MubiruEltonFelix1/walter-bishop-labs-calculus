"""
Visualization module for Experiment 03: Integral Calculus

Provides plotting functions for:
- Functions and their antiderivatives
- Definite integrals (area under curve)
- Area between two curves
- Riemann sums and numerical approximations
- Volumes of revolution
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from sympy import lambdify, sympify, symbols
import sympy as sp

# Enable interactive mode for real-time display
plt.ion()

x = symbols('x')


class IntegrationVisualizer:
    """Visualize integration concepts and results."""
    
    def __init__(self, style='seaborn-v0_8', dpi=150, figsize=(12, 8)):
        """Initialize visualizer with matplotlib settings."""
        try:
            plt.style.use(style)
        except:
            pass
        self.dpi = dpi
        self.figsize = figsize
    
    def plot_function(self, expression_str, x_min=-2, x_max=5, title=None, filename=None):
        """Plot a single function."""
        try:
            expr = sympify(expression_str)
            f = lambdify(x, expr, 'numpy')
            
            x_vals = np.linspace(x_min, x_max, 1000)
            y_vals = f(x_vals)
            
            fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
            ax.plot(x_vals, y_vals, 'b-', linewidth=2.5, label=f'f(x) = {expression_str}')
            ax.axhline(y=0, color='k', linewidth=0.5)
            ax.axvline(x=0, color='k', linewidth=0.5)
            ax.grid(True, alpha=0.3)
            ax.legend(fontsize=11)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('f(x)', fontsize=12)
            ax.set_title(title or f'Graph of f(x) = {expression_str}', fontsize=13, fontweight='bold')
            
            if filename:
                plt.savefig(filename, dpi=self.dpi, bbox_inches='tight')
            
            return fig, ax
        except Exception as e:
            print(f"Error plotting function: {e}")
            return None, None
    
    def plot_definite_integral(self, expression_str, a, b, x_min=None, x_max=None, 
                               title=None, filename=None):
        """Plot function with shaded area representing definite integral."""
        try:
            expr = sympify(expression_str)
            f = lambdify(x, expr, 'numpy')
            
            if x_min is None:
                x_min = min(a - 1, -2)
            if x_max is None:
                x_max = max(b + 1, 5)
            
            x_vals = np.linspace(x_min, x_max, 1000)
            y_vals = f(x_vals)
            
            # Values for shading
            x_fill = np.linspace(a, b, 500)
            y_fill = f(x_fill)
            
            fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
            ax.plot(x_vals, y_vals, 'b-', linewidth=2.5, label=f'f(x) = {expression_str}')
            ax.fill_between(x_fill, 0, y_fill, alpha=0.4, color='#3498db', label=f'Area: ∫ from {a} to {b}')
            ax.axhline(y=0, color='k', linewidth=0.8)
            ax.axvline(x=0, color='k', linewidth=0.5)
            ax.axvline(x=a, color='r', linewidth=1.5, linestyle='--', alpha=0.7)
            ax.axvline(x=b, color='r', linewidth=1.5, linestyle='--', alpha=0.7)
            ax.grid(True, alpha=0.3)
            ax.legend(fontsize=11)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('f(x)', fontsize=12)
            ax.set_title(title or f'Definite Integral: ∫[{a}, {b}] f(x) dx', fontsize=13, fontweight='bold')
            ax.set_xlim(x_min, x_max)
            
            if filename:
                plt.savefig(filename, dpi=self.dpi, bbox_inches='tight')
            
            return fig, ax
        except Exception as e:
            print(f"Error plotting definite integral: {e}")
            return None, None
    
    def plot_area_between_curves(self, f_str, g_str, a, b, x_min=None, x_max=None,
                                 title=None, filename=None):
        """Plot two curves with shaded area between them."""
        try:
            f_expr = sympify(f_str)
            g_expr = sympify(g_str)
            f = lambdify(x, f_expr, 'numpy')
            g = lambdify(x, g_expr, 'numpy')
            
            if x_min is None:
                x_min = min(a - 1, -2)
            if x_max is None:
                x_max = max(b + 1, 5)
            
            x_vals = np.linspace(x_min, x_max, 1000)
            y_f = f(x_vals)
            y_g = g(x_vals)
            
            x_fill = np.linspace(a, b, 500)
            y_f_fill = f(x_fill)
            y_g_fill = g(x_fill)
            
            fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
            ax.plot(x_vals, y_f, 'b-', linewidth=2.5, label=f'f(x) = {f_str}')
            ax.plot(x_vals, y_g, 'g-', linewidth=2.5, label=f'g(x) = {g_str}')
            ax.fill_between(x_fill, y_g_fill, y_f_fill, alpha=0.4, color='#e74c3c', label='Area between curves')
            ax.axhline(y=0, color='k', linewidth=0.5)
            ax.axvline(x=0, color='k', linewidth=0.5)
            ax.axvline(x=a, color='r', linewidth=1.5, linestyle='--', alpha=0.7)
            ax.axvline(x=b, color='r', linewidth=1.5, linestyle='--', alpha=0.7)
            ax.grid(True, alpha=0.3)
            ax.legend(fontsize=11)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('y', fontsize=12)
            ax.set_title(title or f'Area Between Curves', fontsize=13, fontweight='bold')
            ax.set_xlim(x_min, x_max)
            
            if filename:
                plt.savefig(filename, dpi=self.dpi, bbox_inches='tight')
            
            return fig, ax
        except Exception as e:
            print(f"Error plotting area between curves: {e}")
            return None, None
    
    def plot_riemann_sum(self, expression_str, a, b, n, method='left', 
                        title=None, filename=None):
        """Visualize Riemann sum approximation."""
        try:
            expr = sympify(expression_str)
            f = lambdify(x, expr, 'numpy')
            
            x_min = min(a - 0.5, -1)
            x_max = max(b + 0.5, 3)
            
            x_vals = np.linspace(x_min, x_max, 1000)
            y_vals = f(x_vals)
            
            delta_x = (b - a) / n
            
            fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
            ax.plot(x_vals, y_vals, 'b-', linewidth=2.5, label=f'f(x) = {expression_str}')
            
            # Draw rectangles
            if method.lower() == 'left':
                x_rect = np.linspace(a, b - delta_x, n)
            elif method.lower() == 'right':
                x_rect = np.linspace(a + delta_x, b, n)
            else:  # midpoint
                x_rect = np.linspace(a + delta_x/2, b - delta_x/2, n)
            
            for x_i in x_rect:
                y_i = f(x_i)
                rect = Rectangle((x_i, 0), delta_x, y_i, 
                               linewidth=1, edgecolor='r', facecolor='#e74c3c', alpha=0.5)
                ax.add_patch(rect)
            
            ax.axhline(y=0, color='k', linewidth=0.8)
            ax.axvline(x=0, color='k', linewidth=0.5)
            ax.grid(True, alpha=0.3)
            ax.legend(fontsize=11)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('f(x)', fontsize=12)
            ax.set_title(title or f'{method.capitalize()} Riemann Sum (n={n})', 
                        fontsize=13, fontweight='bold')
            ax.set_xlim(x_min, x_max)
            
            if filename:
                plt.savefig(filename, dpi=self.dpi, bbox_inches='tight')
            
            return fig, ax
        except Exception as e:
            print(f"Error plotting Riemann sum: {e}")
            return None, None
    
    def plot_numerical_comparison(self, expression_str, a, b, exact_value=None,
                                 filename=None):
        """Compare different numerical integration methods."""
        try:
            expr = sympify(expression_str)
            f = lambdify(x, expr, 'numpy')
            
            n_values = np.arange(10, 201, 10)
            errors = {
                'Left': [],
                'Right': [],
                'Trapezoidal': [],
                "Simpson's": []
            }
            
            for n in n_values:
                delta_x = (b - a) / n
                x_vals = np.linspace(a, b, n + 1)
                y_vals = f(x_vals)
                
                # Left Riemann
                left = np.sum(y_vals[:-1]) * delta_x
                
                # Right Riemann
                right = np.sum(y_vals[1:]) * delta_x
                
                # Trapezoidal
                trap = (delta_x / 2) * (y_vals[0] + 2 * np.sum(y_vals[1:-1]) + y_vals[-1])
                
                # Simpson's (ensure n is even)
                n_even = n if n % 2 == 0 else n + 1
                delta_x_even = (b - a) / n_even
                x_vals_even = np.linspace(a, b, n_even + 1)
                y_vals_even = f(x_vals_even)
                simp = (delta_x_even / 3) * (
                    y_vals_even[0] +
                    4 * np.sum(y_vals_even[1:-1:2]) +
                    2 * np.sum(y_vals_even[2:-1:2]) +
                    y_vals_even[-1]
                )
                
                if exact_value is not None:
                    errors['Left'].append(abs(left - exact_value))
                    errors['Right'].append(abs(right - exact_value))
                    errors['Trapezoidal'].append(abs(trap - exact_value))
                    errors["Simpson's"].append(abs(simp - exact_value))
            
            if exact_value is not None:
                fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
                
                for method, errs in errors.items():
                    ax.semilogy(n_values, errs, marker='o', label=method, linewidth=2)
                
                ax.set_xlabel('Number of Subintervals (n)', fontsize=12)
                ax.set_ylabel('Absolute Error', fontsize=12)
                ax.set_title(f'Convergence of Numerical Integration Methods\nf(x) = {expression_str}',
                           fontsize=13, fontweight='bold')
                ax.grid(True, alpha=0.3)
                ax.legend(fontsize=11)
                
                if filename:
                    plt.savefig(filename, dpi=self.dpi, bbox_inches='tight')
                
                return fig, ax
            
            return None, None
        except Exception as e:
            print(f"Error plotting comparison: {e}")
            return None, None
