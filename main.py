"""handles cli commands"""
import subprocess

if __name__ == "__main__":
    # Path to the notebook
    notebook_path = "EDA-Modeling.ipynb"

    subprocess.run(
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
    )
