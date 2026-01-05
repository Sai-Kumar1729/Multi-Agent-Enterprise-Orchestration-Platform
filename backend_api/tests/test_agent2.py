from agents.intent_extractor import extract_intent

query = "Why did defect rates increase in Q3 manufacturing?"

intent = extract_intent(query)
print(intent)
