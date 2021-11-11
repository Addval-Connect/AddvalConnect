from typing import Protocol

class DataBaseQuery(Protocol):
    def get_query(self) -> str:
        ...