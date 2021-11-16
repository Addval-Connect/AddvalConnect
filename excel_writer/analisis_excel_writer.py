# # IMPORTS
import pandas as pd
import xlsxwriter
from online_indicators.economic_indicator import EconomicIndicator
from online_indicators.economic_indicator_collector import EconomicIndicatorCollector
from datetime import datetime
import os

# # GENERATE EXCEL
class InformeCuentasExcelGenerator:
    def __init__(self,  client_name: str,
                        client_rut: str,
                        account: str,
                        user_date: datetime,
                        movimientos_df: pd.DataFrame,
                        ) -> None:
        self.client_name = client_name
        self.client_rut = client_rut
        self.account = account
        self.user_date = user_date
        self.movimientos_df = movimientos_df
        self.indicators = {}

    def get_indicators(self, collector: EconomicIndicatorCollector) -> None:
        self.indicators = collector.get(["US_DOLLAR","UF","IPC","UTM"])

    def generate_excel(self,file_name: str) -> None:
        # Creates Excel file
        workbook = xlsxwriter.Workbook(file_name)

        # Adds worksheet
        worksheet = workbook.add_worksheet()

        # Cell formating
        full_border = workbook.add_format({
            "border": 1,
            "border_color": "#000000"
        })

        full_border_date = workbook.add_format({
            "border": 1,
            "border_color": "#000000",
            "num_format": "dd/mm/yy"
        })

        full_border_currency = workbook.add_format({
            "border": 1,
            "border_color": "#000000",
            "num_format": "#,##0"
        })

        full_border_bold = workbook.add_format({
            "border": 1,
            "border_color": "#000000",
            "bold": True
        })

        left_border = workbook.add_format({
            "left": 1,
            "border_color": "#000000"
        })
        right_border_percentage = workbook.add_format({
            "right": 1,
            "border_color": "#000000",
            "num_format": "0.0%"
        })

        right_border = workbook.add_format({
            "right": 1,
            "border_color": "#000000"
        })

        top_border = workbook.add_format({
            "top": 1,
            "border_color": "#000000"
        })

        top_left_border = workbook.add_format({
            "top": 1,
            "left":1,
            "border_color": "#000000"
        })

        top_right_border = workbook.add_format({
            "top": 1,
            "right": 1,
            "border_color": "#000000"
        })

        top_right_border_date = workbook.add_format({
            "top": 1,
            "right": 1,
            "border_color": "#000000",
            "num_format": "dd/mm/yy"
        })

        bottom_border = workbook.add_format({
            "bottom": 1,
            "border_color": "#000000"
        })
        
        decimal = workbook.add_format({
            "num_format": "#,##0.00",
        })

        bottom_border_decimal = workbook.add_format({
            "bottom": 1,
            "border_color": "#000000",
            "num_format": "#,##0.00",
        })

        bottom_border_currency = workbook.add_format({
            "bottom": 5,
            "border_color": "#000000",
            "num_format": "#,##0",
            "bold": True
        })

        bottom_border_bold = workbook.add_format({
            "bottom": 5,
            "border_color": "#000000",
            "bold": True
        })

        bottom_right_border = workbook.add_format({
            "bottom": 1,
            "right": 1,
            "border_color": "#000000"
        })

        bottom_right_border_decimal = workbook.add_format({
            "bottom": 1,
            "right": 1,
            "border_color": "#000000",
            "num_format": "#,##0.00"
        })

        bottom_left_border = workbook.add_format({
            "bottom": 1,
            "left": 1,
            "border_color": "#000000"
        })

        bold = workbook.add_format({
            "bold": True,
            "align": "center"
        })

        # Sets column width
        worksheet.set_column(
            "B:C",
            13
        )

        worksheet.set_column(
            "D:D",
            42
        )

        worksheet.set_column(
            "E:I",
            13
        )

        # Variables to generate header
        usDollar = ""
        if 'US_DOLLAR' in self.indicators:
            usDollar =  self.indicators['US_DOLLAR']
        uf = ""
        if 'UF' in self.indicators:
            uf =  self.indicators['UF']
        cm = ""
        if 'IPC' in self.indicators:
            cm =  self.indicators['IPC']
        utmMonth = ""
        if 'UTM' in self.indicators:
            utmMonth =  self.indicators['UTM']
        emitDate = self.user_date.strftime('%d/%m/%Y')

        # Writes main header company title

        worksheet.write(0, 3, 'Análisis de cuentas', bold)
        worksheet.write(1, 3, self.client_name, bold)
        worksheet.write(2, 3, self.client_rut, bold)
        file_path = os.path.dirname(os.path.realpath(__file__))
        worksheet.insert_image(0, 7, file_path+'/../resources/logo_addval.png', {'x_scale': 1, 'y_scale': 1})
        # worksheet.insert_image(0, 5, resource_path('AnalisisFuensalida\\logo_addval.png'), {'x_scale': 1, 'y_scale': 1})

        # Modifies starting point of column (Sub header and client records)
        row = 5
        column = 1

        # Writes Sub header
        worksheet.write(row + 0, column + 0, 'Código Cuenta:', top_left_border)
        worksheet.write(row + 0, column + 1, self.account, top_border)
        worksheet.write(row + 1, column + 0, 'U.F Cierre:', left_border)
        worksheet.write(row + 1, column + 1, uf,decimal)
        worksheet.write(row + 2, column + 0, 'Dólar Cierre:', bottom_left_border)
        worksheet.write(row + 2, column + 1, usDollar, bottom_border_decimal)

        worksheet.write(row + 0, column + 2, '', top_border)
        worksheet.write(row + 0, column + 3, '', top_border)
        worksheet.write(row + 1, column + 2, '')
        worksheet.write(row + 1, column + 3, '')
        worksheet.write(row + 2, column + 2, '', bottom_border)
        worksheet.write(row + 2, column + 3, '', bottom_border)

        worksheet.write(row + 0, column + 4, '', top_border)
        worksheet.write(row + 0, column + 5, '', top_border)
        worksheet.write(row + 1, column + 4, '')
        worksheet.write(row + 1, column + 5, '')
        worksheet.write(row + 2, column + 4, '', bottom_border)
        worksheet.write(row + 2, column + 5, '', bottom_border)

        worksheet.write(row + 0, column + 6, 'Conciliación al:', top_border)
        worksheet.write(row + 0, column + 7, emitDate, top_right_border_date)
        worksheet.write(row + 1, column + 6, 'C.M. Periodo:')
        worksheet.write(row + 1, column + 7, cm, right_border_percentage)
        worksheet.write(row + 2, column + 6, 'U.T.M:', bottom_border)
        worksheet.write(row + 2, column + 7, utmMonth, bottom_right_border_decimal)

        worksheet.write(row + 4, column + 0, 'COMPOSICIÓN DEL SALDO DE LA CONCILIACIÓN', bottom_border_bold)
        worksheet.write(row + 4, column + 1, '', bottom_border_bold)
        worksheet.write(row + 4, column + 2, '', bottom_border_bold)
        worksheet.write(row + 4, column + 3, '', bottom_border_bold)
        worksheet.write(row + 4, column + 4, '', bottom_border_bold)
        worksheet.write(row + 4, column + 5, '', bottom_border_bold)
        worksheet.write(row + 4, column + 6, '', bottom_border_bold)
        worksheet.write(row + 4, column + 7, int(self.movimientos_df.Saldo.sum()), bottom_border_currency)

        # Define variable to breakline
        breakColumn = 7 + row

        # for client in range(len(dataToArray)):
        for rut,cliente in self.movimientos_df.groupby('Rut', sort=False):

            # Writes all the title of each client
            worksheet.write(breakColumn, column + 0, 'Fecha', full_border_bold)         # Write Fecha title
            worksheet.write(breakColumn, column + 1, 'RUT', full_border_bold)           # Writes Rut title
            worksheet.write(breakColumn, column + 2, 'Detalle', full_border_bold)       # Writes Nombre title
            worksheet.write(breakColumn, column + 3, 'N Documento', full_border_bold)   # Writes N Documento title
            worksheet.write(breakColumn, column + 4, 'N Referencia', full_border_bold)  # Writes N Referencia title
            worksheet.write(breakColumn, column + 5, 'Debe', full_border_bold)          # Writes Debe title
            worksheet.write(breakColumn, column + 6, 'Haber', full_border_bold)         # Writes Haber title
            worksheet.write(breakColumn, column + 7, 'Saldo', full_border_bold)         # Writes Saldo title

            breakColumn += 1

            for _,movimiento in cliente.iterrows():

                movimiento = movimiento.fillna('')
                # Writes all the records of each client
                worksheet.write(breakColumn, column + 0, movimiento.Fecha.strftime("%d-%m-%Y"), full_border_date)  # Writes Fecha
                worksheet.write(breakColumn, column + 1, rut, full_border)  # Writes RUT
                worksheet.write(breakColumn, column + 2, movimiento.Detalle, full_border)                          # Write Detalle
                worksheet.write(breakColumn, column + 3, movimiento['Numero Documento'], full_border)              # Writes N Documento
                worksheet.write(breakColumn, column + 4, movimiento['Numero Documento Referencia'], full_border)   # Writes N Referencia
                worksheet.write(breakColumn, column + 5, movimiento.Debe, full_border_currency)                    # Writes Debe
                worksheet.write(breakColumn, column + 6, movimiento.Haber, full_border_currency)                   # Writes Haber
                worksheet.write(breakColumn, column + 7, movimiento.Saldo, full_border_currency)                   # Writes Saldo

                breakColumn += 1
            # Writes total of saldo for each client
            worksheet.write(breakColumn, column + 6, 'Total', bottom_border_bold)     # Writes Total title
            worksheet.write(breakColumn, column + 7, cliente.Saldo.sum(), bottom_border_currency)     # Writes Total
            breakColumn += 2

        # Close and save Excel file
        workbook.close()

