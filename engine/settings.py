import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    redis_host: str
    single_agent: bool = True
    channel_prefix: str = "Fx_Agent_"

    def __init__(self, **data):
        # Add env vars to **data
        for var_name in self.__fields__:
            var_value = os.getenv(var_name)
            if var_value is not None:
                data[var_name] = var_value

        super().__init__(**data)

    class Config:
        env_prefix = "FX_AGENT_PLATFORM_"


load_dotenv()
load_dotenv(verbose=True)

env_path = Path('.') / f'{sys.argv[1].replace("--env=", "")}'
res = load_dotenv(dotenv_path=env_path)

settings = Settings()
