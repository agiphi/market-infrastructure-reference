# Market Infrastructure Reference

A local-first reference implementation of production-oriented market infrastructure.

Demonstrates architectural boundaries for market-data normalization, signal evaluation, risk controls, execution boundaries, event logging, and deterministic replay.

**Important:** synthetic data only. This is an independent reference implementation and is not the source code of any proprietary trading system.

## Architecture

`Synthetic Market Feed → Normalizer → Signal Engine → Risk Gate → Execution Adapter → Event Log`

The execution layer is an interface. No live broker or exchange connection is included.

## Run

```bash
python -m src.main
```

## Design goals

- deterministic behavior where practical
- explicit separation of strategy, controls, and execution
- observable state transitions
- testable components
- no external trading credentials

This project is public technical evidence of systems and infrastructure architecture. It does not provide investment advice or imply trading profitability.
