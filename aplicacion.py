from flask import Flask, render_template,request

from python.calculoPrimasMetodos.calculoPrimaMetodoBS import PrimaMetodoBS
from python.calculoPrimasMetodos.calculoPrimaMetodoBinomial import PrimaMetodoBinomial
from python.estrategias.compraVentaCallPut import CompraVentaCallPut



aplicacion = Flask(__name__)

@aplicacion.route("/")
def main():
    return render_template("index.html")

@aplicacion.route("/calcularEstrategiasBasicas")
def calcularEstrategias():
    titulo = "CALCULAR ESTRATEGIAS BASICAS"
    return render_template("calcularEstrategiasBasicas.html", titulo=titulo)

@aplicacion.route("/representacionBasicas", methods=['POST'])
def representacionBasicas():
    if request.method == 'POST':
        tipo = request.form['tipo']
        if tipo == "call":
            tipoN = 0
        else: tipoN = 1
        operacion = request.form['operacion']
        if operacion == "compra":
            operacionN = 0
        else:
            operacionN = 1
        ejercicio = request.form['ejercicio']
        ejercicio = float(ejercicio)
        prima = request.form['prima']
        prima = float(prima)
        contratos = request.form['contratos']
        contratos = float(contratos)

    p = CompraVentaCallPut(ejercicio, prima, operacionN, tipoN, contratos)
    ruta = p.rutaImagen
    return render_template("representacionEstrategiasBasicas.html", ruta=ruta, ejercicio=ejercicio, prima=prima, operacion=operacion, tipo=tipo, contratos=contratos)

@aplicacion.route("/calcularPrimaBinomial")
def calcularBinomial():
    titulo = "CALCULAR PRIMA MÉTODO BINOMIAL"
    return render_template("calcularPrimaMetodoBinomial.html", titulo= titulo)

@aplicacion.route("/calcularPrimaBlackSchol")
def calcularBS():
    titulo = "CALCULAR PRIMA MÉTODO BLACK SCHOLES"
    return render_template("calcularPrimaMetodoBS.html", titulo= titulo)

@aplicacion.route("/calculate", methods=['POST'])
def calculate():
    if request.method == 'POST':
        tipo = request.form['tipo']
        if tipo == "Call":
            tipoN = 0
        else: tipoN = 1
        activoSubyacente = request.form['activoSubyacente']
        activoSubyacente = float(activoSubyacente)
        ejercicio = request.form['ejercicio']
        ejericio = float(ejercicio)
        volatilidad = request.form['volatilidad']
        volatilidad = float(volatilidad)
        anios = request.form['anios']
        anios = float(anios)
        tramos = request.form['tramos']
        tramos = int(tramos)
        tipoInteres = request.form['tipoInteres']
        tipoInteres = float(tipoInteres)

        prima = PrimaMetodoBinomial(tipoN, activoSubyacente, ejericio, anios, volatilidad, tramos, tipoInteres).resultado

    return render_template("primaBinomialCalculada.html", tipo=tipo, activoSubyacente=activoSubyacente, ejercicio=ejercicio, volatilidad=volatilidad, anios=anios, tramos= tramos, tipoInteres=tipoInteres, prima=prima)

@aplicacion.route("/calculateBS", methods=['POST'])
def calculateBS():
    if request.method == 'POST':
        tipo = request.form['tipo']
        if tipo == "Call":
            tipoN = 0
        else: tipoN = 1
        activoSubyacente = request.form['activoSubyacente']
        activoSubyacente = float(activoSubyacente)
        ejercicio = request.form['ejercicio']
        ejericio = float(ejercicio)
        volatilidad = request.form['volatilidad']
        volatilidad = float(volatilidad)
        anios = request.form['anios']
        anios = float(anios)
        tipoInteres = request.form['tipoInteres']
        tipoInteres = float(tipoInteres)

        prima = PrimaMetodoBS(tipoN, activoSubyacente, ejericio, anios, volatilidad, tipoInteres).resultado

    return render_template("primaBSCalculada.html", tipo=tipo, activoSubyacente=activoSubyacente, ejercicio=ejercicio, volatilidad=volatilidad, anios=anios, tipoInteres=tipoInteres, prima=prima)


if __name__ == "__main__":
    aplicacion.run(debug=True)
