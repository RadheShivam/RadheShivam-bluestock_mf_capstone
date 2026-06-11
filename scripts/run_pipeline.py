"""
Script Name: run_pipeline.py

Description:
Master execution script to run all stages of the
Mutual Fund Analytics project pipeline.

Author: Shivam Kumar Mehta
"""

import subprocess

scripts = [
    "scripts/etl_pipeline.py",
    "scripts/live_nav_fetch.py",
    "scripts/explore_fund_master.py",
    "scripts/validate_amfi_codes.py"
]

for script in scripts:
    print(f"\nRunning {script}...")

    result = subprocess.run(
        ["python", script]
    )

    if result.returncode == 0:
        print(f"{script} completed successfully.")

    else:
        print(f"Error while running {script}.")
        break

print("\nPipeline execution finished.")