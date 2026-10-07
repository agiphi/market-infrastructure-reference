from .models import MarketEvent

class MarketNormalizer:
    def __init__(self):
        self._last_sequence={}

    def normalize(self,event:MarketEvent)->MarketEvent:
        if event.price<=0:
            raise ValueError("price must be positive")
        previous=self._last_sequence.get(event.symbol)
        if previous is not None and event.sequence<=previous:
            raise ValueError("sequence must increase")
        self._last_sequence[event.symbol]=event.sequence
        return event
