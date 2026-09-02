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
# or a marker:
uv run pytest -m api
# with a results report:
uv run pytest --html=results/report.html
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




## Framework description

This is a quick and dirty test framework based on [pytest](https://docs.pytest.org/en/stable/), that should give you an idea of how I work.

### Why Python/Pytest

[Python]([https://www.python.org/](https://www.python.org/)): speed, familiarity, readability. I won't say there are no drawbacks to using Python, but it's been a standard in the testing space for a reason. For example, it would be no sweat to build and publish the framework code in this project for use in other repos (I've done previously, for a [locust](https://locust.io/)-based performance test repo.)

I chose [pytest](https://docs.pytest.org/en/stable/) framework because it's simple and powerful. Test [fixtures](tests/employee_mgmt/conftest.py) are clean and easily scoped to test, module, or session. Adding workers is simple via [pytest-xdist](https://pypi.org/project/pytest-xdist/) and useful packages like [faker](https://faker.readthedocs.io/en/master/) make generating test data a breeze (see [employee.py](framework/employee_mgmt/helpers/employee.py)).

### Environment management

The [Environment](framework/common/env/env.py) class helps to wrangle environment-specific data, like [URLs](framework/common/env/urls.py) and [Users](framework/common/env/users.py). For now, secrets are stored in an .env file locally - pulling them from a keyvault is an obvious potential future enhancement.

### API access strategy

All code relating to API access lives in the framework. There is a standard [config](/framework/common/api/config.py) class and a potential [PassportOAuth](framework/common/api/passport.py) class (not needed for these tests but I wanted to explore the concept). 

The client strategy starts with a cursor skill, [create-client](.cursor/skills/create-client/), which is expecting a path to a service directory with a swagger definition in it. This skill uses [openapi_python_client](https://pypi.org/project/openapi-python-client/0.6.0a4/) to generate [APIs](framework/employee_mgmt/generated/api/) and [models](framework/employee_mgmt/generated/models/) from the swagger documentation, and handles some cleanup. I gather these generated inputs into a handwritten [client wrapper](framework/employee_mgmt/client.py) which manages all calls to a particular service. 

This wrapper [client](framework/employee_mgmt/client.py) provides logging and automatic response validation for all calls to that service, keeping the tests lean and clean for validation of real functionality. If a response cannot be serialized into the expected response model, an error is thrown and we know an API contract may have changed - this saves the tedium of writing separate contract tests. A potential future enhancement is beefing up the cursor [skill](.cursor/skills/create-client/) so that it automatically creates or updates the client wrapper as well.

## Tests description

[Tests](tests/) live in a separate top-level directory. A top-level session-scoped [fixture](tests/conftest.py) provides the environment, which will automatically be available to all service subdirectories. In the service directory other [fixtures](tests/employee_mgmt/conftest.py) provide a User and the API client. Test modules are flexibly named for the functionality being tested, eg: [test_auth.py](tests/employee_mgmt/test_auth.py). 

Each test a given module should target one aspect of the functionality to validate, for example, API filters, or negative-path inputs and the resulting error-codes. Parameterization is preferred. Test data is consciously scoped and cleaned up whenever possible so that downstream tests are not impacted by existing data. Logging should provide all data necessary for debugging pipeline failures. 

Please reference this results [README.md](results/README.md) for more.

# Soapbox stuff!

![Soapbox](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTOJjRk1un2aG_d7-Nr0p0MZPw3kHdBnZPxOd3X5a9yg&s=10)

### Code Approach

> [!NOTE]
> I try to keep a DRY and tidy repo. I've read *Clean Code* several times — some principles I work to adhere to are:


|                                   |                                                              |
| --------------------------------- | ------------------------------------------------------------ |
| **Small & focused**               | Small classes & methods; SRP wherever possible.              |
| **Naming**                        | Short, precise, consistent variable names.                   |
| **Composition over inheritance**  | Favor building behavior from parts, not deep hierarchies.    |
| **Value objects**                 | Favor value objects over primitives.                         |
| **Readable code**                 | Prefer self-explanatory code over static or noise comments.  |
| **Comments that earn their keep** | Comment important context and unintuitive choices.           |
| **No dead code**                  | Never leave behind commented-out or abandoned code.          |
| **Coupling with intent**          | Avoid over-coupling, but keep related things close together. |
| **White space**                   | Liberal use of white space for readability.                  |
| **Automate the boring stuff**     | Type-checkers, auto-formatters, linters — FTW.               |


---



### Test Philosophy

> [!IMPORTANT]
> Years of experience, distilled into test values I actually live by.


|                         |                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| **Testing pyramid**     | Test as close to the code as meaningfully possible.                                                       |
| **Isolation**           | Test a service or component's functionality in isolation as much as possible.                             |
| **DRY test code**       | Keep tests short; use parameterization whenever possible.                                                 |
| **Meaningful coverage** | Avoid overtesting — scenarios should be meaningfully different and ideally run only against changed code. |
| **No flaky tests**      | Flaky tests are the devil. Don't mark them — fix or delete them.                                          |
| **Tests gate releases** | Failures get triaged immediately; defects get elevated.                                                   |
| **Scoped test data**    | Properly scope test data and delete it when the test is over (unless the env is ephemeral).               |


---



### Frozen Dessert Philosophy

> [!TIP]
> Years of being a human with senses, distilled into dessert values I would take to court.


|                      |                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------- |
| **The hierarchy**    | Gelato > ice cream > fro-yo > sherbet. More creamy calories == better flavor.       |
| **Whipped cream**    | Eaten on its own, on a dessert, or on coffee — all valid life choices.              |
| **Bulletin**         | Adults can purchase whipped cream with or without permission.                       |
| **Chocolate caveat** | Chocolate ice cream is delicious but makes you hella thirsty — hydrate accordingly. |


