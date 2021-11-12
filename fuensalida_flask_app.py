from clientes.analisis_fuensalida.informe_clientes_nacionales import informe_cuentas_por_cobrar_fuensalida
from datetime import datetime
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, flash
# import datetime

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello():
    return render_template("html_user_interface.html")

@app.route("/test")
def buttons():
    input_date = datetime.strptime(request.args["fecha"],"%d/%m/%Y")
    # informe_cuentas_por_cobrar_fuensalida(input_date)
    return str(input_date)
    # return render_template("html_user_interface.html")
    # return request.args
    # input_date = request.form["input-fecha"]
    # flash('This is a flash me', 'success')
    # print(str(input_date)+" - analisis_clientes_nacionales")

# @app.route("/test")
# def analisis_reembolsos():
#     # input_date = request.form["input-fecha"]
#     flash('This is a flash success message', 'success')
#     # print(str(input_date)+" - analisis_reembolsos")
#     return "/analisis_reembolsos"