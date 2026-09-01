# RowsOne-Stage2

This project is designed to provide an example approach of validation & verification of
an [Employee API,](https://1385-api-dev.rowstest.com/api/documentation) for the RowsOne stage 2 SDET interview.

After careful consideration, I chose to use Python for this demo (as opposed to TypeScript), simply for simplicity's sake. The project was estimated at 60-90 minutes of effort, and Python would produce the results I wanted fastest. I decided to create working tests for this API, with an example layout of a service test framework.

## Requirements

- [uv](https://docs.astral.sh/uv/) (Python package manager)
- Python **3.12+** (pinned via `.python-version`; uv will install it if needed.

## Notes on IDE

If using VS Code or Cursor, you'll want the pytest-fixtures extension installed.

## Setup

From the repository root:

```bash
# Install runtime + dev dependencies into .venv/
uv sync --group dev
```

Create a local `.env` in the repo root (gitignored) with the variables below.


| Variable                   | Purpose                                                   |
| -------------------------- | --------------------------------------------------------- |
| `TEST_ENV`                 | Target environment: `dev` (default), `staging`, or `prod` |
| `SDET_EMAIL_<ENV>`         | SDET user email for that env (e.g. `SDET_EMAIL_DEV`)      |
| `SDET_PASSWORD_<ENV>`      | SDET user password                                        |
| `SDET_CLIENT_ID_<ENV>`     | Optional Passport OAuth client id                         |
| `SDET_CLIENT_SECRET_<ENV>` | Optional Passport OAuth client secret                     |


`<ENV>` is the uppercased `TEST_ENV` value (e.g. `dev` → `DEV`).

Example `.env` for local/dev:

```bash
TEST_ENV=dev
SDET_EMAIL_DEV=you@example.com
SDET_PASSWORD_DEV=your-password
# SDET_CLIENT_ID_DEV=
# SDET_CLIENT_SECRET_DEV=
```



## Running tests

Pytest is configured in `pyproject.toml` with:

- Integration / API tests under `tests/`
- Framework unit tests under `framework/unittest/`



### All tests

```bash
uv run pytest
```



### Integration / API tests only

These exercise the live (or configured) Employee Management API:

```bash
uv run pytest tests/
# or a subset:
uv run pytest tests/employee_mgmt/ -v
```



### Unit tests only

These mock HTTP and cover framework building blocks (`ApiClient`, `ApiConfig`, `PassportOAuth`, etc.):

```bash
uv run pytest framework/unittest/ -v
```



### Useful pytest options

```bash
uv run pytest -k passport          # filter by test name
uv run pytest -x                   # stop on first failure
uv run pytest --lf                 # re-run last failures
```



## Project layout (brief)


| Path                       | Role                                               |
| -------------------------- | -------------------------------------------------- |
| `framework/common/`        | Shared env, auth (Passport), HTTP client           |
| `framework/employee_mgmt/` | Employee API helpers + generated OpenAPI client    |
| `framework/unittest/`      | Fast, mocked unit tests for the framework          |
| `tests/`                   | Integration / API verification tests               |
| `.cursor/skills/`          | Agent skills (e.g. `create-client`, `update-docs`) |


