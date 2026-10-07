from datetime import datetime, timezone
import pytest

from market_infrastructure import MarketEvent, MarketNormalizer, MomentumSignal, Order, RiskGate, SimulatedExecutionAdapter


def event(price, sequence=1):
    return MarketEvent("SYNTH", price, sequence, datetime.now(timezone.utc))


def test_normalizer_rejects_bad_sequence():
    n=MarketNormalizer()
    n.normalize(event(10,1))
    with pytest.raises(ValueError):
        n.normalize(event(11,1))


def test_signal_detects_momentum():
    s=MomentumSignal(window=3)
    assert s.evaluate(event(10,1)) is None
    assert s.evaluate(event(11,2)) is None
    assert s.evaluate(event(12,3)) == "buy"


def test_risk_gate_limits_notional():
    gate=RiskGate(max_quantity=10,max_notional=100)
    assert gate.approve(Order("SYNTH","buy",10,10))
    assert not gate.approve(Order("SYNTH","buy",10,10.01))


def test_execution_boundary_rejects_invalid_order():
    result=SimulatedExecutionAdapter().submit(Order("SYNTH","buy",0,10))
    assert not result.accepted
