# import libs

import aiodine
import aioredis
import click

import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

from engine.engine import run_agent
# create settings
from engine.settings import settings


# Setup communication service
@aiodine.provider(lazy=True)
async def redis_instance():
    redis = await aioredis.create_redis_pool(settings.redis_host)
    return redis


@click.group()
@click.pass_context
@click.option("--env", default="")
def main(ctx, env):
    pass


@main.command()
@click.option('--symbols', default="", help='Assets Reading list.')
@click.option('--streamtype', default="live", help='Stream Type')
def reading(symbols, streamtype):
    from agents.reading_agent.agent import ReadingAgent
    run_agent(ReadingAgent, stream_type=streamtype, symbols=symbols)


@main.command()
@click.option('--symbols', default="", help='Assets Reading list.')
def analysing(symbols):
    from agents.analysing_agent.agent import AnalysingAgent
    run_agent(AnalysingAgent)


def start():
    main(obj={})


if __name__ == '__main__':
    start()
