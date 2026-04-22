# Testes_python

A Python project initialized with a virtual environment setup.

## Project Structure

```
.
├── .github/
│   └── copilot-instructions.md
├── venv/              (Virtual environment - created by setup)
├── main.py            (Entry point)
├── requirements.txt   (Project dependencies)
└── README.md          (This file)
```

## Setup Instructions

### 1. Create Virtual Environment

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Project

```bash
python main.py
```

## Requirements

- Python 3.7+

## Development

To add new dependencies, update `requirements.txt` and reinstall:
```bash
pip install -r requirements.txt
```
