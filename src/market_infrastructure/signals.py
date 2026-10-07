from .models import NormalizedEvent
class MomentumSignal:
 def __init__(self,lookback=3): self.lookback=lookback; self._prices={}
 def evaluate(self,event):
  if event.stale or event.gap_detected:return "HOLD"
  prices=self._prices.setdefault(event.symbol,[]); prices.append(event.price); del prices[:-self.lookback]
  if len(prices)<self.lookback:return "HOLD"
  return "BUY" if prices[-1]>prices[0] else "SELL" if prices[-1]<prices[0] else "HOLD"