from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class MarketEvent:
    symbol: str
    price: float
    timestamp: datetime
    sequence: int

@dataclass(frozen=True)
class NormalizedEvent:
    symbol: str
    price: float
    timestamp: datetime
    sequence: int
    stale: bool = False
    gap_detected: bool = False

@dataclass(frozen=True)
class Order:
    symbol: str
    side: str
    quantity: int
    price: float

@dataclass(frozen=True)
class Execution:
    order: Order
    accepted: bool
    reason: str
