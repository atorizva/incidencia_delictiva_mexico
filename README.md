# python-project-template
Python project starter template made with uv and other goodies.

## Tools
This templates comes bundled with:
1. Pre-commit config.
2. Ruff config for linting and formatting.
3. Mypy config for static type checking.
4. Pytest config for testing.

## How to use this template
1. Create a repository using this template.
2. Create the virtual environment: `uv sync`.
3. Activate the virtual environment: `source .venv/bin/activate`.
4. Install the pre-commit hook: `pre-commit install`. This will create the corresponding git hook that will trigger itself before each commit attempt.
5. Build your project! Remember to commit often 😊.

> [!TIP]
> To test your project don't forget to call `pytest`. The configuration in [`pytest.ini`](pytest.ini) should take care of everything.
