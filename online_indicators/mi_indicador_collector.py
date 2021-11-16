import json
import requests
from datetime import datetime
from online_indicators.economic_indicator import EconomicIndicator
from typing import Optional,List,Dict
 


def remove_none_values(economic_dict: Dict[str,Optional[str]]) -> EconomicIndicator:
    valid_dict = EconomicIndicator()
    for key,value in economic_dict.items():
        if value is not None:
            valid_dict[key] = value
    return valid_dict

class MiIndicadorCollector:
    def __init__(self, date: datetime) -> None:
        self.date = date.strftime('%d-%m-%Y')

    def translate(self,indicator_type: str) -> Optional[str]:
            indicator_dict={
                "US_DOLLAR":'dolar',
                "UF":'uf',
                "IPC":'ipc',
                "UTM":'utm'
             }
            if indicator_type in indicator_dict:
                return indicator_dict[indicator_type]
    
    def get_indicator(self,indicator_type: str) -> Optional[str]:
        indicator_str = self.translate(indicator_type)
        if indicator_str is None:
            return
        url = f'https://mindicador.cl/api/{indicator_str}/{self.date}'
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        if data['serie']:
            return data['serie'][0]['valor']
        

    def get(self,indicator_types: List[str]) -> EconomicIndicator:
        indicators = {indicator_type:self.get_indicator(indicator_type) for indicator_type in indicator_types}
        valid_indicators = remove_none_values(indicators)
        if "IPC" in valid_indicators:
            valid_indicators["IPC"] = valid_indicators["IPC"]/100.0
            pass
        return valid_indicators