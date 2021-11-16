from clientes.analisis_fuensalida.informe_clientes_nacionales_anywhere import informe_cuentas_por_cobrar_fuensalida
from datetime import datetime
## pyodbc setup ##
import os
os.environ["ODBCSYSINI"] = "/home/jtguzman"
## ## ## ## ## ##

from flask import Flask, render_template, request,send_file

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello():
    return render_template("Portal Datos/index.html")

@app.route("/generate-report")
def buttons():

    informe = request.args["tipo-informe"]
    if informe=="clientes-nacionales":
        input_date = datetime.strptime(request.args["fecha-reporte"],"%d/%m/%Y")
        path = os.path.dirname(os.path.realpath(__file__))
        file_name = input_date,path+"/analisis_cuentas.xlsx"
        informe_cuentas_por_cobrar_fuensalida(input_date,path+"/analisis_cuentas.xlsx")
        return send_file(file_name, as_attachment=False)
    elif informe=="reembolsos":
        return request.args