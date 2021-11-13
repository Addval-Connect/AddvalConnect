# from clientes.analisis_fuensalida.informe_clientes_nacionales import informe_cuentas_por_cobrar_fuensalida
# from datetime import datetime
import pandas as pd
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
    input_date = request.args["fecha"]
    informe = request.args["informe"]

    output_df = pd.DataFrame([[0,1,2,3],[0,1,2,3],[0,1,2,3]])
    output_df.iloc[1,:] = input_date
    path = os.path.dirname(os.path.realpath(__file__))

    if informe=="clientes-nacionales":
        output_df.iloc[0,:] = informe
    elif informe=="reembolsos":
        output_df.iloc[2,:] = informe

    output_df.to_excel(path+"/fake_excel.xlsx")
    return send_file(path+"/fake_excel.xlsx", as_attachment=False)
