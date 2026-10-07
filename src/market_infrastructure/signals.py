class MomentumSignal:
    def __init__(self, lookback=3):
        if lookback < 2:
            raise ValueError("lookback must be at least 2")
        self.lookback=lookback
        self._prices={}

    def evaluate(self,event):
        if getattr(event,"stale",False) or getattr(event,"gap_detected",False):
            return "HOLD"
        prices=self._prices.setdefault(event.symbol,[])
        prices.append(event.price)
        del prices[:-self.lookback]
        if len(prices)<self.lookback:
            return "HOLD"
        if prices[-1]>prices[0]: return "BUY"
        if prices[-1]<prices[0]: return "SELL"
        return "HOLD"
