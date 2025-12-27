import subprocess
import sys
import os


def run_coverage(test_path: str, output_name: str):
    """
    Runs coverage for a specific test package.
    """
    if not os.path.exists(test_path):
        print(f"[ERROR] Test path not found: {test_path}")
        sys.exit(1)

    print(f"\nRunning coverage for: {test_path}")

    subprocess.run(
        [
            "coverage", "run",
            "--source=src",
            "-m", "pytest",
            test_path
        ],
        check=True
    )

    subprocess.run(
        [
            "coverage", "html",
            "-d", f"htmlcov_{output_name}"
        ],
        check=True
    )

    subprocess.run(["coverage", "erase"], check=True)

    print(f"[OK] Coverage report generated in htmlcov_{output_name}/")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python coverage_runner.py <test_path> <output_name>")
        sys.exit(1)

    run_coverage(sys.argv[1], sys.argv[2])
