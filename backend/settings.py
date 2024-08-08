from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database and test settings
    library_database_url: str = 'postgresql+asyncpg://dev-user:password@localhost:[same_as_defined_in_docker]/[service_name]_dev_db'
    test_database_url: str = 'sqlite+aiosqlite:///library_test.sqlite3'
    echo_sql: bool = False
    echo_test_sql: bool = True
    test: bool = False

    # Project description
    project_name: str = "[Service] Service Microservice"
    project_description: str = "Service description"
    project_version: str = "0.0.1"


settings = Settings()
