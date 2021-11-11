import pyodbc
from read_data_base.data_base_query import DataBaseQuery
from typing import Optional
import pandas as pd

class SQLServerCollector:
    def __init__(   self,
                    server,
                    port,
                    database,
                    username,
                    password) -> None:

        self.connection_string = (
            'DRIVER={SQL Server};'
            'SERVER='+server+';'
            'port='+port+';'
            'DATABASE='+database+';'
            'UID='+username+';'
            'PWD='+ password)

        self.connection = None

    def connect(self) -> None:
        self.connection = pyodbc.connect(self.connection_string)

    def get_data(self,query: DataBaseQuery) -> Optional[pd.DataFrame]:
        if self.connection:
            return pd.read_sql_query(query.get_query(),self.connection)

    def disconnect(self) -> None:
        if self.connection:
            self.connection.commit()