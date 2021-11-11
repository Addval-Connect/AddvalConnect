from typing import Optional, List


class SQLQuery:
    def __init__(   self,table: str,
                    selected_columns: List[str] = ["*"],
                    filters: List[str] = [],
                    groups: List[str] = [],
                    sort_by: List[str] = []) -> None:
        self.table = table
        self.selection = selected_columns
        self.filters = filters
        self.groups = groups
        self.sort_by = sort_by
        pass

    def get_query(self) -> str:
        query = ("select "+
                ",".join(self.selection)+
                " from "+
                self.table)
        if self.filters:
            query = (query+
                    " where "+
                    " and ".join(self.filters))
        if self.groups:
            query = (query+
                    " group by "+
                    ",".join(self.groups))
        if self.sort_by:
            query = (query+
                    " order by "+
                    ",".join(self.sort_by))
        return query
    pass

class QueryTipoDocumentos(SQLQuery):
    def __init__(self) -> None:
        table = "softland.cwttdoc"
        super().__init__(table)
        pass
    pass

class QueryAuxiliares(SQLQuery):
    def __init__(self) -> None:
        table = "softland.cwtauxi"
        selected_columns = ["RutAux as 'Rut'",
                            "NomAux as 'Nombre Cliente'",
                            "CodAux"]
        super().__init__(table,selected_columns)
        pass
    pass

class QueryAnalisisMovimientos(SQLQuery):
    def __init__(self,account: str,closing_date: str) -> None:
        table = "softland.cwmovim A join softland.cwcpbte B on A.CpbNum = B.CpbNum  and A.CpbAno = B.CpbAno"
        selected_columns = ["A.CpbFec as 'Fecha'",
                            "A.MovGlosa as 'Detalle'",
                            "A.NumDoc as 'Numero Documento'",
                            "A.MovNumDocRef as 'Numero Documento Referencia'",
                            "A.TtdCod as 'Tipo Documento'",
                            "A.CodAux",
                            "A.CpbAno",
                            "A.CpbNum",
                            "A.MovDebe as 'Debe'",
                            "A.MovHaber as 'Haber'"]
        filters=[   "A.PctCod = '"+account+"'",
                    "B.CpbEst = 'V'",
                    "A.CpbFec <= '"+closing_date+"'"
                    "A.TtdCod <> '00'",
                    "(A.CpbNum <> '00000000' Or A.CpbAno = MIN(A.CpbAno))"
                ]
        super().__init__(   table=table,
                            selected_columns=selected_columns,
                            filters=filters)
        pass
    pass


# ## Read Movements
# def read_movements(account,date,cnxn):
#     movimientos = movimientos[~((movimientos.CpbNum=='00000000')&(movimientos.CpbAno!='2016'))]
#     return movimientos