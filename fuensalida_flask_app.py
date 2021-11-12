from clientes.analisis_fuensalida.informe_clientes_nacionales import informe_cuentas_por_cobrar_fuensalida
from datetime import datetime
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
# import datetime

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello():
    return render_template("main_page.html")

@app.route("/analisis_clientes_nacionales", methods=["POST"])
def analisis_clientes_nacionales():
    input_date = request.form["input-fecha"]
    print(str(input_date)+" - analisis_clientes_nacionales")

@app.route("/analisis_reembolsos", methods=["POST"])
def analisis_reembolsos():
    input_date = request.form["input-fecha"]
    print(str(input_date)+" - analisis_reembolsos")