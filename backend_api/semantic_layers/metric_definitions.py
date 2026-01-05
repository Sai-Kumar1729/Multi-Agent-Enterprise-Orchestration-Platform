METRICS = {
    "avg_yield": {
        "source": "manufacturing_metrics.csv",
        "column": "yield_percent",
        "agg": "mean"
    },
    "avg_defect_rate": {
        "source": "manufacturing_metrics.csv",
        "column": "defect_rate",
        "agg": "mean"
    },
    "total_units": {
        "source": "manufacturing_metrics.csv",
        "column": "units_produced",
        "agg": "sum"
    },
    "avg_downtime": {
        "source": "manufacturing_metrics.csv",
        "column": "downtime_minutes",
        "agg": "mean"
    },
    "avg_cycle_time": {
        "source": "operations_logs.csv",
        "column": "cycle_time_sec",
        "agg": "mean"
    },
    "energy_usage": {
        "source": "operations_logs.csv",
        "column": "energy_consumption_kwh",
        "agg": "sum"
    }
}
