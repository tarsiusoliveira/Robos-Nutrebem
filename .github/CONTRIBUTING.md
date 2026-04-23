# Contributing to This Project

## Before You Start

- Read [SECURITY.md](../SECURITY.md) - **Critical for this project**
- Never commit sensitive data (credentials, tokens, API keys)
- Never commit data files (CSV, databases, etc.)
- Use `.env` files for all configuration

## Getting Started

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create** a virtual environment: `python -m venv venv`
4. **Install** dependencies: `pip install -r requirements.txt`
5. **Create** a `.env` file from `.env.example`
6. **Add your changes** in a new branch

## Development Workflow

### Creating a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### Making Changes

- Keep changes focused and atomic
- Follow existing code style
- Add comments for complex logic
- Test thoroughly before committing

### Committing Changes

```bash
git add .
git commit -m "Brief description of changes"
```

**Commit Message Guidelines:**
- Start with a verb: "Add", "Fix", "Update", "Refactor"
- Be clear and descriptive
- Reference issues if applicable

## ⚠️ Sensitive Data Checklist

Before every commit, verify:

- [ ] No `.env` files (should be `.gitignore`d)
- [ ] No real credentials or passwords
- [ ] No API keys or tokens
- [ ] No personal data or sensitive CSVs
- [ ] No database backups
- [ ] All changes are in code files only

```bash
# Check what you're about to commit
git diff --cached

# Never commit sensitive files
git status | grep -E "\.env|\.csv|secrets"
```

## Testing

- Test your changes locally
- Verify with staging environment if available
- Document test steps in PR description

## Pull Request Process

1. **Push** your branch to your fork
2. **Create** a pull request with:
   - Clear title describing changes
   - Description of what changed and why
   - Steps to test the changes
   - Reference to any related issues
3. **Address** review comments
4. **Get approval** from maintainers
5. **Squash and merge** your changes

## Code Review

All contributions require review. Reviewers will check:

- ✅ No hardcoded credentials
- ✅ No sensitive data in files
- ✅ Proper use of environment variables
- ✅ Code quality and style
- ✅ Test coverage
- ✅ Documentation updates

## Common Mistakes to Avoid

❌ **DON'T:**
```python
# Never do this!
EMAIL = "my-email@example.com"
PASSWORD = "my-password"
api_key = "sk-1234567890abcdef"
database_url = "postgresql://user:pass@localhost/db"
```

✅ **DO THIS:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv('PROD_EMAIL')
password = os.getenv('PROD_PASSWORD')
api_key = os.getenv('API_KEY')
database_url = os.getenv('DATABASE_URL')
```

## Questions?

- Check existing issues and discussions
- Read the README.md for usage examples
- Review SECURITY.md for security practices
- Open an issue for questions

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing! 🙏
