from pydantic import BaseModel


class BasicCandleData(BaseModel):
    open: float
    high: float
    low: float
    close: float
    epoch: int
    symbol: str
    # id: str
    # open_time: int
    # pip_size: int
    # granularity: int
    # volume: int = 0
    # type: str = "CandleData"
