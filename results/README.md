# RowsOne-Stage2

## Testing results, issues found

Click [here](results/report.html) for an HTML test report.

The following issues were found and observations were made in the course of this testing:

### Naming

Swagger endpoints with names that should be fixed:

| Endpoint                   | Correct Name                                                   |
| -------------------------- | --------------------------------------------------------- |
| `TEST_ENV`                 | Target environment: `dev` (default), `staging`, or `prod` |
| `SDET_EMAIL_<ENV>`         | SDET user email for that env (e.g. `SDET_EMAIL_DEV`)      |
| `SDET_PASSWORD_<ENV>`      | SDET user password                                        |
| `SDET_CLIENT_ID_<ENV>`     | Optional Passport OAuth client id                         |
| `SDET_CLIENT_SECRET_<ENV>` | Optional Passport OAuth client secret                     |

### Naming