from flask import Flask, render_template,request

from python.calculoPrimasMetodos.calculoPrimaMetodoBS import PrimaMetodoBS
from python.calculoPrimasMetodos.calculoPrimaMetodoBinomial import PrimaMetodoBinomial
from python.estrategias.basicas.estrategiasBasicas import EstrategiasBasicas
from python.estrategias.representacionEstrategias import Representacion
from python.estrategias.tendencia.spreadAlcista import SpreadAlcista
from python.estrategias.tendencia.spreadBajista import SpreadBajista
from python.estrategias.tendencia.tunel import Tunel

aplicacion = Flask(__name__)

@aplicacion.route("/")
def main():
    return render_template("index.html")

@aplicacion.route("/calcularEstrategiasBasicas")
def calcularEstrategias():
    titulo = "CALCULAR ESTRATEGIAS BASICAS"
    return render_template("./Estrategias/calcularEstrategiasBasicas.html", titulo=titulo)

@aplicacion.route("/calcularEstrategiasComplejas")
def complejas():
    titulo = "ESTRATEGIAS COMPLEJAS"
    return render_template("./Estrategias/calcularEstrategiasComplejas.html", titulo = titulo)

@aplicacion.route("/spreadBajista")
def spreadBajista():
    titulo = "SPREAD BAJISTA"
    return render_template("./Estrategias/tendencia/spreadBajista.html", titulo=titulo)

@aplicacion.route("/spreadAlcista")
def spreadAlcista():
    titulo = "SPREAD ALCISTA"
    return render_template("./Estrategias/tendencia/spreadAlcista.html", titulo=titulo)

@aplicacion.route("/tunelAlcista")
def tunelAlcista():
    titulo = "TÚNEL ALCISTA"
    return render_template("./Estrategias/tendencia/tunelAlcista.html", titulo=titulo)

@aplicacion.route("/tunelBajista")
def tunelBajista():
    titulo = "TÚNEL BAJISTA"
    return render_template("./Estrategias/tendencia/tunelBajista.html", titulo=titulo)

@aplicacion.route("/estrategiasTendencia")
def tendencia():
    titulo = "ESTRATEGIAS DE TENDENCIA"
    return render_template("./Estrategias/tendencia/estrategiasTendencia.html", titulo = titulo)

@aplicacion.route("/representacionTendencia", methods=['POST'])
def representacionTendencia():
    if request.method == 'POST':
        tipo = request.form['tipo']
        if tipo == "Call":
            tipoN = 0
        else:
            tipoN = 1
        ejercicio0 = request.form['ejercicio0']
        ejercicio0 = float(ejercicio0)
        prima0 = request.form['prima0']
        prima0 = float(prima0)
        contratos0 = request.form['contratos0']
        contratos0 = float(contratos0)
        ejercicio1 = request.form['ejercicio1']
        ejercicio1 = float(ejercicio1)
        prima1 = request.form['prima1']
        prima1 = float(prima1)
        contratos1 = request.form['contratos1']
        contratos1 = float(contratos1)
        if (request.form['estrategia'] == "spreadBajista"):
            titulo = "SPREAD BAJISTA"
            estrategia = SpreadBajista(ejercicio0, prima0, ejercicio1, prima1, tipoN, contratos0, contratos1)
        if (request.form['estrategia'] == "spreadAlcista"):
            titulo = "SPREAD ALCISTA"
            estrategia = SpreadAlcista(ejercicio0, prima0,ejercicio1, prima1, tipoN, contratos0,contratos1)
        if (request.form['estrategia'] == "tunelAlcista"):
            tipo=0
            titulo = "TUNEL ALCISTA"
            estrategia = Tunel(ejercicio0, prima0,ejercicio1, prima1, tipo, contratos0,contratos1)
            r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
            return render_template("./Estrategias/tendencia/representacionTendencia.html", ruta=r.rutaImagen,
                                   ejercicio0=ejercicio0, prima0=prima0, ejercicio1=ejercicio1, prima1=prima1,
                                   tipo="Compra call y Venta put", contratos0=contratos0, contratos1=contratos1, titulo=titulo)
        if (request.form['estrategia'] == "tunelBajista"):
            tipo=1
            titulo = "TUNEL BAJISTA"
            estrategia = Tunel(ejercicio0, prima0,ejercicio1, prima1, tipo, contratos0,contratos1)

    r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
    return render_template("./Estrategias/tendencia/representacionTendencia.html", ruta=r.rutaImagen, ejercicio0=ejercicio0, prima0=prima0, ejercicio1= ejercicio1, prima1=prima1, tipo=tipo, contratos0=contratos0, contratos1=contratos1, titulo=titulo)

@aplicacion.route("/representacionBasicas", methods=['POST'])
def representacionBasicas():
    if request.method == 'POST':
        tipo = request.form['tipo']
        if tipo == "Call":
            tipoN = 0
        else: tipoN = 1
        operacion = request.form['operacion']
        if operacion == "Compra":
            operacionN = 0
        else:
            operacionN = 1
        ejercicio = request.form['ejercicio']
        ejercicio = float(ejercicio)
        prima = request.form['prima']
        prima = float(prima)
        contratos = request.form['contratos']
        contratos = float(contratos)

    estrategia = EstrategiasBasicas(ejercicio, prima, operacionN, tipoN, contratos)
    r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
    return render_template("/Estrategias/representacionEstrategiasBasicas.html", ruta=r.rutaImagen, ejercicio=ejercicio, prima=prima, operacion=operacion, tipo=tipo, contratos=contratos)

@aplicacion.route("/calcularPrimaBinomial")
def calcularBinomial():
    titulo = "CALCULAR PRIMA MÉTODO BINOMIAL"
    return render_template("./MetodoBinomial/calcularPrimaMetodoBinomial.html", titulo= titulo)

@aplicacion.route("/calcularPrimaBlackSchol")
def calcularBS():
    titulo = "CALCULAR PRIMA MÉTODO BLACK SCHOLES"
    return render_template("./MetodoBS/calcularPrimaMetodoBS.html", titulo= titulo)

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
        if tipoInteres == "i":
            interesLibre = 0
            interesAnual = float(request.form['interesDef'])
            value = float(request.form['interesDef'])

        else:
            interesAnual = 0
            interesLibre = float(request.form['interesDef'])
            value = float(request.form['interesDef'])

        prima = PrimaMetodoBinomial(tipoN, activoSubyacente, ejericio, anios, volatilidad, tramos, interesAnual, interesLibre).resultado
    return render_template("./MetodoBinomial/primaBinomialCalculada.html", tipo=tipo, activoSubyacente=activoSubyacente, ejercicio=ejercicio, volatilidad=volatilidad, anios=anios, tramos= tramos, tipoInteres=tipoInteres, prima=prima, value=value)

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
        if tipoInteres == "i":
            interesLibre = 0
            interesAnual = float(request.form['interesDef'])
            value = float(request.form['interesDef'])

        else:
            interesAnual = 0
            interesLibre = float(request.form['interesDef'])
            value = float(request.form['interesDef'])

        prima = PrimaMetodoBS(tipoN, activoSubyacente, ejericio, anios, volatilidad, interesAnual, interesLibre).resultado

    return render_template("./MetodoBS/primaBSCalculada.html", tipo=tipo, activoSubyacente=activoSubyacente, ejercicio=ejercicio, volatilidad=volatilidad, anios=anios, tipoInteres=tipoInteres, prima=prima, value=value)


if __name__ == "__main__":
    aplicacion.run(debug=True)
