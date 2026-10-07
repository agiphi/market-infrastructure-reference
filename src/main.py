from dataclasses import dataclass
from time import time


@dataclass(frozen=True)
class MarketEvent:
    symbol: str
    bid: float
    ask: float
    sequence: int


class MarketNormalizer:
    def normalize(self, event: MarketEvent) -> dict:
        if event.bid <= 0 or event.ask <= 0 or event.ask < event.bid:
            raise ValueError("invalid market event")
        return {
            "symbol": event.symbol,
            "mid": round((event.bid + event.ask) / 2, 6),
            "spread": round(event.ask - event.bid, 6),
            "sequence": event.sequence,
        }


class SignalEngine:
    def evaluate(self, current: float, reference: float) -> str:
        if current > reference:
            return "UP"
        if current < reference:
            return "DOWN"
        return "FLAT"


class RiskGate:
    def __init__(self, max_notional: float = 1000.0):
        self.max_notional = max_notional

    def approve(self, price: float, quantity: int) -> bool:
        return price > 0 and quantity > 0 and price * quantity <= self.max_notional


class ExecutionAdapter:
    def submit(self, symbol: str, side: str, quantity: int) -> dict:
        return {
            "status": "SIMULATED",
            "symbol": symbol,
            "side": side,
            "quantity": quantity,
            "timestamp": time(),
        }


def main() -> None:
    event = MarketEvent("SYNTH", 0.59, 0.61, 1)
    normalized = MarketNormalizer().normalize(event)
    signal = SignalEngine().evaluate(normalized["mid"], 0.50)
    approved = RiskGate().approve(normalized["mid"], 10)

    print({"market": normalized, "signal": signal, "risk_approved": approved})

    if approved:
        print(ExecutionAdapter().submit("SYNTH", signal, 10))


if __name__ == "__main__":
    main()
