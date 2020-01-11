from asyncio import run

import aiodine

from engine.base_agent import BaseAgent


@aiodine.consumer
async def __run_agent__(redis_instance, agent: BaseAgent = None, data=None):
    agent = agent(comm=await redis_instance, **data)
    await agent.run()


def run_agent(agent=None, **data):
    run(__run_agent__(agent=agent, data=data))
