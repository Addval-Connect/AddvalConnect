from datetime import datetime

from analisis_cuentas import informe_cuentas_por_cobrar as informe
from clientes.analisis_fuensalida import analisis_fuensalida_params as params
from read_data_base.data_collectors import SQLServerCollector
from read_data_base.softland_querys import QueryTipoDocumentos,QueryAuxiliares,QueryAnalisisMovimientos

# def generar_analisis(   client_name: str, 
#                         client_rut: str,
#                         account: str,
#                         input_date: datetime,
#                         collector: DataFrameCollector,
#                         docs_query: DataBaseQuery,
#                         auxiliares_query: DataBaseQuery,
#                         movimientos_query: DataBaseQuery) -> None:




def main() -> None:
    input_date = datetime.strptime("30/09/2021","%d/%m/%Y")

    collector = SQLServerCollector( params.server,
                                    params.port,
                                    params.database,
                                    params.username,
                                    params.password)

    docs_query = QueryTipoDocumentos()
    auxiliares_query = QueryAuxiliares()
    movimientos_query = QueryAnalisisMovimientos(   params.account,
                                                    input_date)

    informe.generar_analisis(   params.client_name,
                                params.client_rut,
                                params.account,
                                input_date,
                                collector,
                                docs_query,
                                auxiliares_query,
                                movimientos_query)

if __name__ == '__main__':
    main()