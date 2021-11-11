# # IMPORTS
from datetime import datetime

#LOCAL IMPORTS
from online_indicators.economic_indicators import EconomicIndicators
from excel_writer.analisis_excel_writer import generate_excel
from informe_cuentas_softland import analisis_cuentas_por_cobrar
from read_data_base.data_frame_collector import DataFrameCollector
from read_data_base.data_base_query import DataBaseQuery

def GenerateAnalisis(   client_name: str, 
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

    if all_docs_df and auxiliares and movimientos:
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
