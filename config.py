from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    imap_server: str
    imap_port: int

    email: str
    password: str

    discord_webhook: str


    class Config:
        env_file = ".env"


settings = Settings()



