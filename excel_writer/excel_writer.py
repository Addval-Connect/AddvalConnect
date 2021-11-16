from typing import Protocol

class ExcelGenerator(Protocol):
    def generate_excel(self,file_name: str) -> None:
        ...