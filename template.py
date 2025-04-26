import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Corrected the missing comma
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    "env",
    "scrpt.py",
    "app.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)  # convert to a Path object

    # If it's a file (has a suffix) -> create parent folders and file
    if filepath.suffix:
        filepath.parent.mkdir(parents=True, exist_ok=True)  # create directory if not exists
        if not filepath.exists():
            filepath.touch()
            logging.info(f"Created file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")
    else:
        # If no suffix, it's a directory (like env)
        filepath.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created folder: {filepath}")
