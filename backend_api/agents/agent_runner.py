import os
import pandas as pd
from agents.intent_extractor import extract_intent
from agents.aggregator import aggregate
from agents.data_reader import read_csv
from semantic_layers.metric_definitions import METRICS

class AgentRunner:
    def __init__(self):
        self.data_dir = "data"

    def run(self, query: str):
        """
        Orchestrates Agent-2 flow with error handling for unknown queries.
        """
        # 1. Extract intent
        intent_output = extract_intent(query)
        
        # 2. CHECK: Is the intent unknown or empty?
        # If the LLM returned "unknown" OR extracted no metrics
        intent_name = intent_output.get("intent", "unknown")
        metrics = intent_output.get("metrics", [])
        
        if intent_name == "unknown" or not metrics:
            return {
                "response": "Data is not available for the mentioned query."
            }

        # 3. Process Valid Metrics
        results = {}
        
        for metric in metrics:
            if metric not in METRICS:
                results[metric] = "Metric not defined in system."
                continue

            metric_info = METRICS[metric]
            source_file = metric_info["source"]
            column = metric_info["column"]
            agg_type = metric_info["agg"]
            
            file_path = os.path.join(self.data_dir, source_file)

            try:
                df = read_csv(file_path)
                val = aggregate(df, column, agg_type)
                results[metric] = val
            except FileNotFoundError:
                results[metric] = "Data file missing."
            except Exception as e:
                results[metric] = f"Error: {str(e)}"

        return {
            "intent": intent_name,
            "metrics_used": metrics,
            "results": results
        }

# Entry point for API
def run_agent(query: str):
    runner = AgentRunner()
    return runner.run(query)