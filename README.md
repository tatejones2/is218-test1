Running lint/tests
```
# Lint (must be clean)
pylint --errors-only src

# Run tests
PYTHONPATH=src pytest tests -v
PYTHONPATH=src pytest --pylint src -v

# Coverage (must be 100%)
PYTHONPATH=src coverage run -m pytest tests
coverage report --fail-under=100
```