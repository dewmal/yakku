from agents.reading_agent.agent import ReadingAgent
from app.data.CandleData import BasicCandleData
from engine.base_agent import BaseAgent


class AnalysingAgent(BaseAgent):
    name = "Analysing_Agent"

    async def run(self):
        channel = await self.subscribe(agent=ReadingAgent)
        print(channel)
        while await channel.wait_message():
            msg = await channel.get(encoding='utf-8')
            ca = BasicCandleData.parse_raw(msg)
            print(ca)
