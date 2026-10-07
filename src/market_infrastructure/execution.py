from .models import Execution, Order

class SimulatedExecutionAdapter:
    def submit(self, order: Order) -> Execution:
        if order.quantity <= 0:
            return Execution(order, False, "invalid quantity")
        if order.price <= 0:
            return Execution(order, False, "invalid price")
        return Execution(order, True, "accepted by simulation")
