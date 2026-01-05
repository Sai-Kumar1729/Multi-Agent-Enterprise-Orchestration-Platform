from pydantic import BaseModel
from typing import List

class DataRequest(BaseModel):
    intent: str
    metrics: List[str]
    time_range: str
    business_unit: str
