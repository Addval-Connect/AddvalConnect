# # IMPORTS
from datetime import datetime

#LOCAL IMPORTS
from online_indicators.economic_indicators import EconomicIndicators
from read_data_base.data_base_query import DataBaseQuery
from read_data_base.data_frame_collector import DataFrameCollector

from excel_writer.analisis_excel_writer import generate_excel
from analisis_cuentas.informe_cuentas_softland import analisis_cuentas_por_cobrar


def generar_analisis(   client_name: str, 
                        client_rut: str,
                        account: str,
                        input_date: datetime,
                        collector: DataFrameCollector,
                        docs_query: DataBaseQuery,
                        auxiliares_query: DataBaseQuery,
                        movimientos_query: DataBaseQuery) -> None:

    #Connect to database
    collector.connect()

    #Read Doc Types
    all_docs_df = collector.get_data(docs_query)

    #Read Auxiliares
    auxiliares = collector.get_data(auxiliares_query)

    #Read Movements
    movimientos = collector.get_data(movimientos_query)

    if all_docs_df is not None:
        if auxiliares is not None:
            if movimientos is not None:
                movimientos_con_auxiliares = analisis_cuentas_por_cobrar(all_docs_df,auxiliares,movimientos)

                #Generate Excel
                generate_excel( client_name,
                                client_rut,
                                account,
                                input_date,
                                movimientos_con_auxiliares,
                                EconomicIndicators(input_date))
                print("Analisis generado satisfactoriamente")
                return
        
    print("Problemas de Conexion con la base de datos")
    pass
