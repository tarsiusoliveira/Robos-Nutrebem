# Security Policy

## Reporting Vulnerabilities

⚠️ **Do not open public issues for security vulnerabilities!**

If you discover a security vulnerability, please email us with:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

We will respond within 48 hours.

## Secure Usage Guidelines

### Credentials & Environment Variables

1. **Never hardcode credentials** in source files
2. **Always use `.env` files** for sensitive data
3. **Keep `.env` local** - it's in `.gitignore`
4. **Use strong passwords** for all accounts
5. **Rotate credentials regularly**

### Before Public Publishing

- [ ] No credentials in git history
- [ ] All sensitive config in `.env` files
- [ ] `.env` file is in `.gitignore`
- [ ] `.env.example` has placeholder values only
- [ ] Data files (CSVs) are in `.gitignore`
- [ ] No API keys, tokens, or passwords in code
- [ ] All imports are in `requirements.txt`

### Dependencies

- Keep dependencies up to date
- Review `requirements.txt` for security advisories
- Use `pip audit` to check for known vulnerabilities:
  ```bash
  pip install pip-audit
  pip-audit
  ```

### Data Protection

- **CSV files**: Not tracked in git (prevent data leaks)
- **Browser automation**: Headless mode for CI/CD
- **Logs**: Don't log sensitive information
- **Database connections**: Use environment variables only

### Access Control

- Restrict `.env` file permissions:
  ```bash
  chmod 600 .env  # Linux/Mac only
  ```
- Keep credentials separate for prod/staging
- Never share credentials via email or chat
- Use separate accounts for testing environments

## Security Best Practices

### Development

```python
# ❌ BAD
password = "my_password_123"
db.connect(user="admin", password="secret")

# ✅ GOOD
import os
from dotenv import load_dotenv

load_dotenv()
password = os.getenv('DB_PASSWORD')
db.connect(
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD')
)
```

### .env File Template

```
# Never commit this file!
PROD_EMAIL=secure_value
PROD_PASSWORD=secure_value
STAGING_EMAIL=secure_value
STAGING_PASSWORD=secure_value
```

## Incident Response

If you believe sensitive data has been exposed:

1. **Immediately revoke** the compromised credentials
2. **Update** all `.env` files with new credentials
3. **Rotate passwords** in all affected systems
4. **Check git history** for any accidental commits
5. **Contact** relevant parties if credentials were exposed

## Regular Audits

- Monthly dependency updates
- Quarterly credential rotation
- Annual security review

---

**Last Updated:** 2026-04-23
