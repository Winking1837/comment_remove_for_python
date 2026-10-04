# comment-cleaner

A small terminal tool that removes comments from Python source files. It uses the Python `tokenize` module, so `#` characters inside strings are left untouched and only comments are removed.

Heads up: the tool edits files in place. Commit your work or make a backup before running it.

## Features

- Strips all `#` comments from a Python file
- Safe for strings containing `#` (uses real tokenization, not regex)
- standard library only
- Usable as a CLI command or as a Python function

## Installation

### From GitHub

```bash
pip install git+https://github.com/<your-username>/comment-cleaner.git
```

### From a local clone (for development)

```bash
git clone https://github.com/<your-username>/comment-cleaner.git
cd comment-cleaner
pip install -e .
```

## Usage

### Command line

```bash
comment-cleaner path/to/your_file.py
```

Output:

```
Comments removed from 'path/to/your_file.py'.
```

If no file is given, or the file does not exist, an error message is printed.

## Project structure

```
comment-cleaner/
├── pyproject.toml          
├── README.md
└── comment_cleaner/        
    ├── __init__.py
    └── cleaner.py          
```

> The folder containing `__init__.py` and `cleaner.py` must be a package directory (e.g. `comment_cleaner/`). Put `pyproject.toml` one level above it, in the project root.

## pyproject.toml

Your `pyproject.toml` is currently empty, so `pip install` won't work yet. Here is a minimal working configuration:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "comment-cleaner"
version = "0.1.0"
description = "Remove comments from Python source files"
readme = "README.md"
requires-python = ">=3.8"
license = { text = "MIT" }
dependencies = []

[project.scripts]
comment-cleaner = "comment_cleaner.cleaner:main"

[tool.setuptools]
packages = ["comment_cleaner"]
```

The `[project.scripts]` section is what creates the `comment-cleaner` command after installation, which you can call using pip.
