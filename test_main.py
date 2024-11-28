import subprocess
import os


def test_notebook():
    """tests notebook()"""
    notebook_path = "EDA-Modeling.ipynb"

    result = subprocess.run(
        [
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            "--output",
            "executed_notebook.ipynb",
            notebook_path,
        ],
        check=True,
        capture_output=True,  # Capture stdout and stderr
        text=True,  # Decode output as a string
    )
    assert result.returncode == 0


def test_model_output_exists():
    # Construct the full file path
    file_path = "model_output.csv"

    # Check if the file exists
    assert os.path.isfile(file_path)


if __name__ == "__main__":
    test_notebook()
    test_model_output_exists()
