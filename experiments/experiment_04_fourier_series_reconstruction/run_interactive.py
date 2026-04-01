"""Interactive launcher for Experiment 04.

Run with: python run_interactive.py
This prompts for a single waveform or all waveforms, then shows plots one at a time.
"""

from main import run_experiment
import settings


def prompt_for_functions():
    print("=" * 80)
    print("INTERACTIVE MODE: Fourier series reconstruction")
    print("=" * 80)
    print("Choose a waveform to explore:")
    for index, function_name in enumerate(settings.FUNCTIONS, start=1):
        print(f"  {index}. {function_name}")
    print(f"  {len(settings.FUNCTIONS) + 1}. all functions")

    choice = input(f"Selection [1-{len(settings.FUNCTIONS) + 1}]: ").strip()
    mapping = {str(index): [function_name] for index, function_name in enumerate(settings.FUNCTIONS, start=1)}
    mapping[str(len(settings.FUNCTIONS) + 1)] = settings.FUNCTIONS
    return mapping.get(choice, settings.FUNCTIONS)


if __name__ == "__main__":
    selected_functions = prompt_for_functions()
    print("\nRunning analysis. Close each plot window to continue.")
    run_experiment(show_progress=True, selected_functions=selected_functions)
