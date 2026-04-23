# Testes_python

A Python project for automating product restrictions management in Nutrebem environments.

## ⚠️ Security & Privacy

This project uses browser automation to manage restricted data. **Never commit sensitive data to version control:**

- ✅ `.gitignore` excludes:
  - `.env` files containing credentials
  - All `.csv` data files
  - Virtual environment files
  - IDE configuration

- ✅ Use environment variables for credentials (never hardcode)
- ✅ Use `.env.example` as a template for configuration
- ✅ Keep your `.env` file local and never share it

## Project Structure

```
.
├── .github/
│   └── copilot-instructions.md
├── .env.example           (Template for environment variables)
├── .gitignore            (Prevents accidental commits of sensitive data)
├── venv/                 (Virtual environment - created by setup)
├── requirements.txt      (Project dependencies)
├── robo_nutrebem_prod.py  (Production automation script)
├── robo_nutrebem_staging.py (Staging automation script)
├── README.md             (This file)
└── dados_exec_prod.csv   (Data file - NOT committed to git)
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Testes_python
```

### 2. Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

**Create a `.env` file** (copy from `.env.example` and add your credentials):

```bash
cp .env.example .env
```

**Edit `.env` with your credentials:**
```
PROD_EMAIL=your_email@example.com
PROD_PASSWORD=your_password
STAGING_EMAIL=your_staging_email@example.com
STAGING_PASSWORD=your_staging_password
```

⚠️ **Never commit your `.env` file!** It's in `.gitignore` and should only exist locally.

### 5. Add Your Data Files

Place your CSV data files in the project root:
- `dados_exec_prod.csv` (for production)
- `dados_teste_staging.csv` (for staging)

Or specify custom paths in your `.env` file:
```
PROD_CSV_FILE=path/to/your/prod_data.csv
STAGING_CSV_FILE=path/to/your/staging_data.csv
```

## Usage

### Run Production Script
```bash
python robo_nutrebem_prod.py
```

### Run Staging Script
```bash
python robo_nutrebem_staging.py
```

## Dependencies

- **playwright** (v1.40+) - Browser automation
- **pandas** (v2.0+) - Data handling
- **python-dotenv** (v1.0+) - Environment variable management

See `requirements.txt` for specific versions.

## Requirements

- Python 3.7+
- Internet connection (to access web applications)

## Security Checklist Before Publishing

- [ ] `.env` file is in `.gitignore` (never committed)
- [ ] `.csv` files are in `.gitignore` (never committed)
- [ ] `requirements.txt` contains all dependencies with pinned versions
- [ ] `.env.example` contains placeholder values (no real credentials)
- [ ] No hardcoded passwords, tokens, or API keys in Python files
- [ ] All sensitive data is loaded from environment variables
- [ ] README.md documents security practices

## Troubleshooting

### "PROD_EMAIL and PROD_PASSWORD environment variables are required"
- Ensure your `.env` file exists and contains valid credentials
- Check that `.env` is in the project root directory
- Verify environment variables are properly formatted

### "CSV file not found"
- Ensure your CSV files are in the project root or path specified in `.env`
- Check file names match exactly (case-sensitive on Linux/Mac)

### Import errors
- Activate your virtual environment: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
- Reinstall dependencies: `pip install -r requirements.txt`

## Development

For local development, follow the setup instructions above. All configuration is environment-based, making it safe for collaborative development without sharing credentials.

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]


To add new dependencies, update `requirements.txt` and reinstall:
```bash
pip install -r requirements.txt
```
