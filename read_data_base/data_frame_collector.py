from typing import Protocol,Optional
from data_base_query import DataBaseQuery
import pandas as pd

class DataFrameCollector(Protocol):
    def connect(self) -> None:
        ...
    def get_data(self,query: DataBaseQuery) ->Optional[pd.DataFrame]:
        ...
    def disconnect(self) -> None:
        ...