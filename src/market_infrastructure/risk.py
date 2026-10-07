from dataclasses import dataclass

@dataclass(frozen=True)
class RiskDecision:
    allowed: bool
    reason: str

class RiskGate:
    def __init__(self, max_position=500, max_order=100):
        self.max_position=max_position
        self.max_order=max_order

    def check(self, side, quantity, current_position):
        if quantity<=0 or quantity>self.max_order:
            return RiskDecision(False,"order_size_limit")
        projected=current_position+quantity if side=="BUY" else current_position-quantity
        if abs(projected)>self.max_position:
            return RiskDecision(False,"position_limit")
        return RiskDecision(True,"allowed")
