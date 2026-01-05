from agents.agent_runner import run_agent

request = {
    "intent": "plant_efficiency",
    "metrics": [
        "avg_yield",
        "avg_cycle_time",
        "energy_usage"
    ]
}

output = run_agent(request)
print(output)
print("Request:", request)
