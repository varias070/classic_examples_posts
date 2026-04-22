from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str
    QUERY_REPO_PATH: str

    @property
    def DB_URL(self):
        return (
            f"postgresql+psycopg2://"
            f"{self.DB_USER}:"
            f"{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:"
            f"{self.DB_PORT}/"
            f"{self.DB_NAME}"
        )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = 'allow'


class TestSetting(BaseSettings):
    TEST_DB_USER: str
    TEST_DB_PASSWORD: str
    TEST_DB_NAME: str
    TEST_DB_HOST: str
    TEST_DB_PORT: str
    QUERY_REPO_PATH: str

    @property
    def TEST_DB_URL(self):
        return (
            f"postgresql+psycopg2://"
            f"{self.TEST_DB_USER}:"
            f"{self.TEST_DB_PASSWORD}@"
            f"{self.TEST_DB_HOST}:"
            f"{self.TEST_DB_PORT}/"
            f"{self.TEST_DB_NAME}"
        )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = 'allow'
