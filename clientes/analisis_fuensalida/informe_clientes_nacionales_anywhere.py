from datetime import datetime

from analisis_cuentas import informe_cuentas_por_cobrar as informe
from clientes.analisis_fuensalida import analisis_fuensalida_params as params
from read_data_base.data_collectors import PythonAnywhereSQLServerCollector
from read_data_base.softland_querys import QueryTipoDocumentos,QueryAuxiliares,QueryAnalisisMovimientos
from online_indicators.mi_indicador_collector import MiIndicadorCollector


def informe_cuentas_por_cobrar_fuensalida(input_date: datetime,file_name: str) -> None:
    collector = PythonAnywhereSQLServerCollector( 
                                    params.database,
                                    params.username,
                                    params.password)

    docs_query = QueryTipoDocumentos()
    auxiliares_query = QueryAuxiliares()
    movimientos_query = QueryAnalisisMovimientos(   params.clientes_nacionales,
                                                    input_date)


    indicator_collector = MiIndicadorCollector(input_date)

    informe.generar_analisis(   params.client_name,
                                params.client_rut,
                                params.clientes_nacionales,
                                input_date,
                                collector,
                                docs_query,
                                auxiliares_query,
                                movimientos_query,
                                indicator_collector,
                                file_name)