import os
from pathlib import Path

# Read file utils
def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file at '{filepath}' was not found."
    except PermissionError:
        return f"Error: Permission denied when trying to read '{filepath}'."
    except IOError as e:
        return f"Error: An I/O error occurred when reading '{filepath}': {str(e)}"
