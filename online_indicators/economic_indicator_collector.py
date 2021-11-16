from typing import Protocol,List
from online_indicators.economic_indicator import EconomicIndicator
from datetime import datetime

class EconomicIndicatorCollector(Protocol):
    def __init__(self, date: datetime) -> None:
        ...

    def get(self,indicator_types: List[str]) -> EconomicIndicator:
        ...