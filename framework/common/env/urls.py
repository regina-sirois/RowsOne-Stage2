# Common URLs for the RowsOne platform, by environment
# NOTE:
# - Please keep methods in alphabetical order, for ease of maintenance
# - URLs should NOT include trailing slashes.


class Urls:
    environment: str

    def __init__(self, environment: str) -> None:
        # Keep lowercase for URL host segments (e.g. 1385-api-dev.rowstest.com).
        self.environment = environment.lower()

    def get_employee_mgmt_base_url(self) -> str:
        return f"https://1385-api-{self.environment}.rowstest.com"

    def get_oauth_url(self) -> str:
        # NOTE: example - when the URL doesn't follow a simple pattern.
        if self.environment == "dev":
            return "https://one-example.rowsone.com/oauth"
        elif self.environment == "qa":
            return "https://another-example.rowsone.com/oauth"
        elif self.environment == "prod":
            raise NotImplementedError("Production environment not supported for OAuth")
        else:
            raise ValueError(f"Invalid environment: {self.environment}")

    def get_rowsone_ui_base_url(self) -> str:
        # NOTE: example - don't know internal UI URL for each environment.
        # I've found this type of class useful with many environments & services.
        return f"https://{self.environment}.rowsone.com"
