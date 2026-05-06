import subprocess
import os

def run_workflow():
    print("--- Starting End-to-End Analysis Workflow ---")
    print("Step 1: Running Notebook (Data Cleaning & Merging)...")
    try:
        subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "islab.ipynb"], check=True)
        print("Success: Notebook executed and 'crime_with_ses.csv' generated.")
    except Exception as e:
        print(f"Error during Notebook execution: {e}")
        return
    print("Step 2: Running main.py (Generating Results)...")
    try:
        subprocess.run(["python", "main.py"], check=True)
        print("Success: Results generated.")
    except Exception as e:
        print(f"Error during main.py execution: {e}")
        return

    print("--- Workflow Complete! ---")

if __name__ == "__main__":
    run_workflow()