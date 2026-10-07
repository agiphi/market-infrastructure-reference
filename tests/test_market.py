from datetime import datetime, timezone
import pytest

from market_infrastructure import MarketEvent, MarketNormalizer, MomentumSignal, Order, RiskGate, SimulatedExecutionAdapter


def event(price, sequence=1):
    return MarketEvent("SYNTH", price, datetime.now(timezone.utc), sequence)


def test_normalizer_rejects_bad_sequence():
    n=MarketNormalizer()
    n.normalize(event(10,1))
    with pytest.raises(ValueError):
        n.normalize(event(11,1))


def test_signal_detects_momentum():
    s=MomentumSignal(lookback=3)
    assert s.evaluate(event(10,1)) == "HOLD"
    assert s.evaluate(event(11,2)) == "HOLD"
    assert s.evaluate(event(12,3)) == "BUY"


def test_risk_gate_limits_order_and_position():
    gate=RiskGate(max_position=10,max_order=5)
    assert gate.check("BUY",5,0).allowed
    assert not gate.check("BUY",6,0).allowed
    assert not gate.check("BUY",5,6).allowed


def test_execution_boundary_rejects_invalid_order():
    result=SimulatedExecutionAdapter().submit(Order("SYNTH","BUY",0,10))
    assert not result.accepted
