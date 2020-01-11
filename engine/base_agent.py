import abc
from typing import Any, Optional

from pydantic import BaseModel

from engine.settings import settings


class BaseAgent(BaseModel, abc.ABC):
    name: str
    channel_name: Optional[str]
    comm: Any

    def __init__(__pydantic_self__, **data: Any) -> None:
        if "name" not in data:
            if "name" in __pydantic_self__.__fields__ and __pydantic_self__.__fields__.get("name").default:
                data["name"] = __pydantic_self__.__fields__.get("name").default
            else:
                data["name"] = f"{__pydantic_self__.__class__.__name__}"

        if "channel_name" not in data:
            if "channel_name" in __pydantic_self__.__fields__ and __pydantic_self__.__fields__.get(
                    "channel_name").default:
                data["channel_name"] = __pydantic_self__.__fields__.get("channel_name").default
            else:
                data["channel_name"] = f"{settings.channel_prefix}{data['name']}"
        super().__init__(**data)

    @abc.abstractmethod
    async def run(self):
        pass

    async def subscribe(self, channel_name=None, agent=None):
        if agent:
            channel_name = f"{settings.channel_prefix}{agent.__fields__.get('name').default}"
        channel, = await self.comm.subscribe(channel_name)
        return channel

    async def publish(self, message):
        await self.comm.publish(self.channel_name, message)
