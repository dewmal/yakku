import asyncio

from app.data.CandleData import BasicCandleData
from engine.base_agent import BaseAgent
import logging


class ReadingAgent(BaseAgent):
    name = "Reading_Agent"
    stream_type: str
    symbols: str

    async def process_symbol(self, symbol):
        while True:
            msg = f"Hi Hi {self.stream_type}-{symbol}"
            candle = BasicCandleData(open=1.45, high=1.455, low=1.255, close=1.255, epoch=7825255)
            await self.publish(candle.json())
            logging.info(msg)

    async def run(self):
        processors = [self.process_symbol(symbol=symbol) for symbol in self.symbols.split(",")]
        res = await asyncio.wait(processors, return_when=asyncio.ALL_COMPLETED)
