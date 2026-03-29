"""
Interactive runner for Experiment 03: Smart Mobility Energy and Load Accumulation

Run with: python run_interactive.py
This will display all matplotlib plots ONE AT A TIME as they're generated.
"""

import sys
from pathlib import Path
import matplotlib.pyplot as plt

# Configure matplotlib for interactive display
plt.ion()  # Turn on interactive mode
plt.rcParams['figure.dpi'] = 100

# Run the main experiment
if __name__ == '__main__':
    from main import main
    
    print("=" * 80)
    print("INTERACTIVE MODE: Plots will display ONE AT A TIME")
    print("=" * 80)
    print("\nInstructions:")
    print("  • Each plot will appear one after another")
    print("  • CLOSE the plot window to continue to the next visualization")
    print("  • 5 plots total will be displayed in sequence")
    print("  • Plots are also saved to outputs/plots/ for later review")
    print("  • A summary report is saved to outputs/reports/")
    print("\n" + "=" * 80 + "\n")
    
    try:
        main()
        print("\n" + "=" * 80)
        print("✓ Experiment Complete!")
        print("=" * 80)
        print("All 5 plots have been displayed and saved!")
        print("\nOutputs saved to:")
        print("  📊 Visualizations: outputs/plots/")
        print("  📄 Summary Report: outputs/reports/summary_report.txt")
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
