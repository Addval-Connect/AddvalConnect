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
    return render_template("html_user_interface.html")

@app.route("/generate-report")
def buttons():

    informe = request.args["informe"]
    if informe=="clientes-nacionales":
        input_date = datetime.strptime(request.args["fecha"],"%Y-%m-%d")
        path = os.path.dirname(os.path.realpath(__file__))
        informe_cuentas_por_cobrar_fuensalida(input_date,path+"/analisis_cuentas.xlsx")
        return send_file(path+"/analisis_cuentas.xlsx", as_attachment=False)
    elif informe=="reembolsos":
        return informe