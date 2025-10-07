# my-new-app

A minimal Flask web API that returns a simple greeting.

## Requirements

- Python 3.10+
- pip

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\\Scripts\\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the app

With the virtual environment activated, start the development server:

```bash
python app.py
```

The API will be available at http://localhost:5000/. Accessing the root endpoint returns a JSON payload with the message "Hello, world!".

## Regenerating dependencies

If you add or remove dependencies, regenerate `requirements.txt`:

```bash
pip freeze > requirements.txt
```
