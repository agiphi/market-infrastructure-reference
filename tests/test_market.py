from src.main import MarketEvent, MarketNormalizer, RiskGate, SignalEngine


def test_normalization():
    result = MarketNormalizer().normalize(MarketEvent("X", 0.40, 0.60, 1))
    assert result["mid"] == 0.50
    assert result["spread"] == 0.20


def test_signal():
    engine = SignalEngine()
    assert engine.evaluate(0.60, 0.50) == "UP"
    assert engine.evaluate(0.40, 0.50) == "DOWN"
    assert engine.evaluate(0.50, 0.50) == "FLAT"


def test_risk_gate():
    gate = RiskGate(max_notional=100)
    assert gate.approve(5, 10)
    assert not gate.approve(11, 10)
