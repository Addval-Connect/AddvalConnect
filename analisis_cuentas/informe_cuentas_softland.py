import pandas as pd

#Descartar mobimientos iniciales, a exepcion de los del primer año
def remove_initial_movements(movimientos: pd.DataFrame) -> pd.DataFrame:
    clean_movements = movimientos.loc[~((movimientos.CpbNum=='00000000')&(movimientos.CpbAno!=movimientos.CpbAno.min())),:]
    # clean_movements = movimientos.loc[[~((movimientos.CpbNum=='00000000')&(movimientos.CpbAno!=movimientos.CpbAno.min()))],:]
    return clean_movements

# Anexar datos de auxiliares a movimientos
def join_movements_auxiliares(movimientos,auxiliares):
    return pd.merge(
                movimientos,
                auxiliares,
                how="left",
                left_on=['CodAux'],
                right_on=['CodAux'],
                suffixes=("", "_"))

#Separar movimientos entre movimientos iniciales y otros movimientos que hacen referencia a estos
def separate_movements(movimientos,all_docs_df):
    # Seleccionar movimientos auto-referenciados
    movimientos_iniciales = movimientos[movimientos['Numero Documento Referencia'] == movimientos['Numero Documento']]
    # Seleccionar movimientos no auto-referenciados
    movimientos_otros = movimientos[~(movimientos['Numero Documento Referencia'] == movimientos['Numero Documento'])]

    # Seleccionar movimientos iniciales de venta
    movimientos_iniciales_venta = movimientos_iniciales[movimientos_iniciales['Tipo Documento'].isin(all_docs_df[all_docs_df['LibDoc']=='V'].CodDoc)]
    # Seleccionar movimientos iniciales de no de venta
    movimientos_iniciales_otros = movimientos_iniciales[~movimientos_iniciales['Tipo Documento'].isin(all_docs_df[all_docs_df['LibDoc']=='V'].CodDoc)]

    # Inicializar movimientos iniciales con movimientos de iniciales de venta
    movimientos_iniciales = movimientos_iniciales_venta.copy()
    # Agregar a movimientos iniciales los documentos iniciales no de venta que no hacen referencia a documentos iniciales de venta
    movimientos_iniciales = pd.concat([movimientos_iniciales,movimientos_iniciales_otros[~movimientos_iniciales_otros['Numero Documento Referencia'].isin(movimientos_iniciales_venta['Numero Documento Referencia'])]])
    # Agregar a movimientos no auto-referenciados los documentos iniciales no de venta que hacen referencia a documentos iniciales de venta
    movimientos_otros = pd.concat([movimientos_otros,movimientos_iniciales_otros[movimientos_iniciales_otros['Numero Documento Referencia'].isin(movimientos_iniciales_venta['Numero Documento Referencia'])]])
    return movimientos_iniciales,movimientos_otros

#Calcua el saldo para todos los movimientos iniciales
def calculate_movement_balance(movimientos_iniciales,movimientos_otros):
    # Resumir otros movimientos por numero de referencia
    saldo_otros = movimientos_otros.groupby(['CodAux','Numero Documento Referencia'])[['Debe','Haber']].sum()
    saldo_otros.index = saldo_otros.index.set_names('Numero Documento', level=1)

    # Indexar movimientos iniciales por numero de documento
    movimientos_iniciales = movimientos_iniciales.set_index(['CodAux','Numero Documento'])


    # Inicializar balance
    balance = movimientos_iniciales.copy()
    # Calcular saldos de movimientos iniciales
    balance['Saldo'] = movimientos_iniciales['Debe']-movimientos_iniciales['Haber']
    
    # Calcular saldo de movimientos iniciales referenciados por otros movimientos
    index_otros = saldo_otros.index
    balance.loc[index_otros,'Saldo'] = movimientos_iniciales.loc[index_otros,'Debe']-movimientos_iniciales.loc[index_otros,'Haber']+saldo_otros['Debe']-saldo_otros['Haber']

    # Agregar a balance los movimientos no iniciales
    balance = pd.concat([balance.reset_index(),movimientos_otros])

    # Ordenar balance
    balance = balance.reset_index()
    balance = balance.sort_values(['CodAux','Numero Documento Referencia','Fecha'])
    return balance

def analisis_cuentas_por_cobrar(all_docs_df: pd.DataFrame,
                                auxiliares: pd.DataFrame,
                                movimientos: pd.DataFrame) -> pd.DataFrame:

    movimientos_limpios = remove_initial_movements(movimientos)

    #Descartar Movimientos Calzados
    movimientos_no_calzados = movimientos_limpios.groupby(['CodAux','Numero Documento Referencia']).filter(lambda group: group.Debe.sum()-group.Haber.sum()!=0)

    #Separar movimientos
    movimientos_iniciales,movimientos_otros =  separate_movements(movimientos_no_calzados,all_docs_df)
    
    #Calculate Movement Balance
    movements_balance = calculate_movement_balance(movimientos_iniciales,movimientos_otros)

    #Anexar datos de auxiliares a movimientos
    movimientos_con_auxiliares = join_movements_auxiliares(movements_balance,auxiliares)

    return movimientos_con_auxiliares