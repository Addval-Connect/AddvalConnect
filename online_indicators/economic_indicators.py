import json
import requests
import datetime
 
class EconomicIndicators:

    def __init__(self, date: datetime.date) -> None:
        self.date = date.strftime('%d-%m-%Y')
    
    def get(self,indicador) -> str:
        # En este caso hacemos la solicitud para el caso de consulta de un indicador en un año determinado
        url = f'https://mindicador.cl/api/{indicador}/{self.date}'
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        return data['serie'][0]['valor']