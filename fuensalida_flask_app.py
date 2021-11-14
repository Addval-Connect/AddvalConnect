from clientes.analisis_fuensalida.informe_clientes_nacionales import informe_cuentas_por_cobrar_fuensalida
from datetime import datetime
# import pandas as pd
import os
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request,send_file
# import datetime

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello():
    return render_template("html_user_interface.html")

@app.route("/generate-report")
def buttons():
    input_date = datetime.strptime(request.args["fecha"],"%Y-%m-%d")
    informe = request.args["informe"]
    path = os.path.dirname(os.path.realpath(__file__))

    if informe=="clientes-nacionales":
        informe_cuentas_por_cobrar_fuensalida(input_date,path+"/analisis_cuentas.xlsx")
        return send_file(path+"/analisis_cuentas.xlsx", as_attachment=False)
    elif informe=="reembolsos":
        return informe