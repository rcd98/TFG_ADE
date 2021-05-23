from flask import Flask, render_template,request

from python.calculoPrimasMetodos.calculoPrimaMetodoBS import PrimaMetodoBS
from python.calculoPrimasMetodos.calculoPrimaMetodoBinomial import PrimaMetodoBinomial
from python.estrategias.basicas.estrategiasBasicas import EstrategiasBasicas
from python.estrategias.mixtas.callRatioBackspread import CallRatioBackspread
from python.estrategias.mixtas.putRatioBackspread import PutRatioBackspread
from python.estrategias.mixtas.ratioCallSpread import RatioCallSpread
from python.estrategias.mixtas.ratioPutSpread import RatioPutSpread
from python.estrategias.representacionEstrategias import Representacion
from python.estrategias.tendencia.spreadAlcista import SpreadAlcista
from python.estrategias.tendencia.spreadBajista import SpreadBajista
from python.estrategias.tendencia.tunel import Tunel
from python.estrategias.volatilidad.conoComprado import ConoComprado
from python.estrategias.volatilidad.conoVendido import ConoVendido
from python.estrategias.volatilidad.cunaComprada import CunaComprada
from python.estrategias.volatilidad.cunaVendida import CunaVendida
from python.estrategias.volatilidad.mariposaComprada import MariposaComprada
from python.estrategias.volatilidad.mariposaVendida import MariposaVendida

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

@aplicacion.route("/estrategiasVolatilidad")
def volatilidad():
    titulo = "ESTRATEGIAS DE VOLATILIDAD"
    return render_template("./Estrategias/volatilidad/estrategiasVolatilidad.html", titulo = titulo)

@aplicacion.route("/estrategiasMixtas")
def mixtas():
    titulo = "ESTRATEGIAS MIXTAS"
    return render_template("./Estrategias/mixtas/estrategiasMixtas.html", titulo = titulo)

@aplicacion.route("/conoComprado")
def conoComprado():
    titulo = "CONO COMPRADO"
    return render_template("./Estrategias/volatilidad/conoComprado.html", titulo=titulo)

@aplicacion.route("/representacionConoComprado", methods=['POST'])
def representacionConoComprado():
    if request.method == 'POST':
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
        titulo = "CONO COMPRADO"
        titulo1 = "COMPRA DE CALL"
        titulo2 = "COMPRA DE PUT"

        estrategia = ConoComprado(ejercicio0, prima0, ejercicio1, prima1, contratos0, contratos1)
        r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
    return render_template("./Estrategias/representacion.html", ruta=r.rutaImagen, ejercicio0=ejercicio0, prima0=prima0, ejercicio1= ejercicio1, prima1=prima1, tipo="CALL y PUT", contratos0=contratos0, contratos1=contratos1, titulo=titulo, titulo1=titulo1, titulo2=titulo2)

@aplicacion.route("/conoVendido")
def conoVendido():
    titulo = "CONO VENDIDO"
    return render_template("./Estrategias/volatilidad/conoVendido.html", titulo=titulo)

@aplicacion.route("/representacionConoVendido", methods=['POST'])
def representacionConoVendido():
    if request.method == 'POST':
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
        titulo = "CONO VENDIDO"
        titulo1 = "VENTA DE CALL"
        titulo2 = "VENTA DE PUT"

        estrategia = ConoVendido(ejercicio0, prima0, ejercicio1, prima1, contratos0, contratos1)
        r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
    return render_template("./Estrategias/representacion.html", ruta=r.rutaImagen, ejercicio0=ejercicio0, prima0=prima0, ejercicio1= ejercicio1, prima1=prima1, tipo="CALL y PUT", contratos0=contratos0, contratos1=contratos1, titulo=titulo, titulo1=titulo1, titulo2=titulo2)

@aplicacion.route("/cunaComprada")
def cunaComprada():
    titulo = "CUNA COMPRADA"
    return render_template("./Estrategias/volatilidad/cunaComprada.html", titulo=titulo)

@aplicacion.route("/representacionCunaComprada", methods=['POST'])
def representacionCunaComprada():
    if request.method == 'POST':
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
        titulo = "CUNA COMPRADA"
        titulo1 = "COMPRA DE CALL"
        titulo2 = "COMPRA PUT"

        estrategia = CunaComprada(ejercicio0, prima0, ejercicio1, prima1, contratos0, contratos1)
        r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
    return render_template("./Estrategias/representacion.html", ruta=r.rutaImagen, ejercicio0=ejercicio0, prima0=prima0, ejercicio1= ejercicio1, prima1=prima1, tipo="CALL y PUT", contratos0=contratos0, contratos1=contratos1, titulo=titulo, titulo1=titulo1, titulo2=titulo2)

@aplicacion.route("/cunaVendida")
def cunaVendida():
    titulo = "CUNA VENDIDA"
    return render_template("./Estrategias/volatilidad/cunaVendida.html", titulo=titulo)

@aplicacion.route("/representacionCunaVendida", methods=['POST'])
def representacionCunaVendida():
    if request.method == 'POST':
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
        titulo = "CUNA VENDIDA"
        titulo1 = "VENTA DE CALL"
        titulo2 = "VENTA PUT"

        estrategia = CunaVendida(ejercicio0, prima0, ejercicio1, prima1, contratos0, contratos1)
        r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
    return render_template("./Estrategias/representacion.html", ruta=r.rutaImagen, ejercicio0=ejercicio0, prima0=prima0, ejercicio1= ejercicio1, prima1=prima1, tipo="CALL y PUT", contratos0=contratos0, contratos1=contratos1, titulo=titulo, titulo1=titulo1, titulo2=titulo2)

@aplicacion.route("/ratioCallSpread")
def ratioCallSpread():
    titulo = "RATIO CALL SPREAD"
    return render_template("./Estrategias/mixtas/ratioCallSpread.html", titulo=titulo)

@aplicacion.route("/representacionRatioCallSpread", methods=['POST'])
def representacionRatioCallSpread():
    if request.method == 'POST':
        ejercicio0 = request.form['ejercicio0']
        ejercicio0 = float(ejercicio0)
        prima0 = request.form['prima0']
        prima0 = float(prima0)

        ejercicio1 = request.form['ejercicio1']
        ejercicio1 = float(ejercicio1)
        prima1 = request.form['prima1']
        prima1 = float(prima1)

        ejercicio2 = request.form['ejercicio2']
        ejercicio2 = float(ejercicio2)
        prima2 = request.form['prima2']
        prima2 = float(prima2)

        titulo = "RATIO CALL SPREAD"
        titulo1 = "COMPRA DE CALL"
        titulo2 = "VENTA DE CALL"
        titulo3 = "VENTA DE CALL"

        estrategia = RatioCallSpread(ejercicio0, prima0, ejercicio1, prima1, ejercicio2, prima2)
        r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
    return render_template("./Estrategias/representacionMixtas.html", ruta=r.rutaImagen, ejercicio0=ejercicio0, prima0=prima0, ejercicio1= ejercicio1, prima1=prima1, ejercicio2= ejercicio2, prima2=prima2, tipo="CALL", titulo=titulo, titulo1=titulo1, titulo2=titulo2, titulo3=titulo3)

@aplicacion.route("/ratioPutSpread")
def ratioPutSpread():
    titulo = "RATIO PUT SPREAD"
    return render_template("./Estrategias/mixtas/ratioPutSpread.html", titulo=titulo)

@aplicacion.route("/representacionRatioPutSpread", methods=['POST'])
def representacionRatioPutSpread():
    if request.method == 'POST':
        ejercicio0 = request.form['ejercicio0']
        ejercicio0 = float(ejercicio0)
        prima0 = request.form['prima0']
        prima0 = float(prima0)

        ejercicio1 = request.form['ejercicio1']
        ejercicio1 = float(ejercicio1)
        prima1 = request.form['prima1']
        prima1 = float(prima1)

        ejercicio2 = request.form['ejercicio2']
        ejercicio2 = float(ejercicio2)
        prima2 = request.form['prima2']
        prima2 = float(prima2)

        titulo = "RATIO PUT SPREAD"
        titulo1 = "COMPRA DE PUT"
        titulo2 = "VENTA DE PUT"
        titulo3 = "VENTA DE PUT"

        estrategia = RatioPutSpread(ejercicio0, prima0, ejercicio1, prima1, ejercicio2, prima2)
        r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
    return render_template("./Estrategias/representacionMixtas.html", ruta=r.rutaImagen, ejercicio0=ejercicio0, prima0=prima0, ejercicio1= ejercicio1, prima1=prima1, ejercicio2= ejercicio2, prima2=prima2, tipo="PUT", titulo=titulo, titulo1=titulo1, titulo2=titulo2, titulo3=titulo3)

@aplicacion.route("/callRatioBackspread")
def callRatioBackspread():
    titulo = "CALL RATIO BACKSPREAD"
    return render_template("./Estrategias/mixtas/callRatioBackspread.html", titulo=titulo)

@aplicacion.route("/representacionCallRatioBackspread", methods=['POST'])
def representacionCallRatioBackspread():
    if request.method == 'POST':
        ejercicio0 = request.form['ejercicio0']
        ejercicio0 = float(ejercicio0)
        prima0 = request.form['prima0']
        prima0 = float(prima0)

        ejercicio1 = request.form['ejercicio1']
        ejercicio1 = float(ejercicio1)
        prima1 = request.form['prima1']
        prima1 = float(prima1)

        ejercicio2 = request.form['ejercicio2']
        ejercicio2 = float(ejercicio2)
        prima2 = request.form['prima2']
        prima2 = float(prima2)

        titulo = "CALL RATIO BACKSPREAD"
        titulo1 = "VENTA DE CALL"
        titulo2 = "COMPRA DE CALL"
        titulo3 = "COMPRA DE CALL"

        estrategia = CallRatioBackspread(ejercicio0, prima0, ejercicio1, prima1, ejercicio2, prima2)
        r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
    return render_template("./Estrategias/representacionMixtas.html", ruta=r.rutaImagen, ejercicio0=ejercicio0, prima0=prima0, ejercicio1= ejercicio1, prima1=prima1, ejercicio2= ejercicio2, prima2=prima2, tipo="CALL", titulo=titulo, titulo1=titulo1, titulo2=titulo2, titulo3=titulo3)

@aplicacion.route("/putRatioBackspread")
def putRatioBackspread():
    titulo = "PUT RATIO BACKSPREAD"
    return render_template("./Estrategias/mixtas/putRatioBackspread.html", titulo=titulo)

@aplicacion.route("/representacionPutRatioBackspread", methods=['POST'])
def representacionPutRatioBackspread():
    if request.method == 'POST':
        ejercicio0 = request.form['ejercicio0']
        ejercicio0 = float(ejercicio0)
        prima0 = request.form['prima0']
        prima0 = float(prima0)

        ejercicio1 = request.form['ejercicio1']
        ejercicio1 = float(ejercicio1)
        prima1 = request.form['prima1']
        prima1 = float(prima1)

        ejercicio2 = request.form['ejercicio2']
        ejercicio2 = float(ejercicio2)
        prima2 = request.form['prima2']
        prima2 = float(prima2)

        titulo = "PUT RATIO BACKSPREAD"
        titulo1 = "VENTA DE PUT"
        titulo2 = "COMPRA DE PUT"
        titulo3 = "COMPRA DE PUT"

        estrategia = PutRatioBackspread(ejercicio0, prima0, ejercicio1, prima1, ejercicio2, prima2)
        r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
    return render_template("./Estrategias/representacionMixtas.html", ruta=r.rutaImagen, ejercicio0=ejercicio0, prima0=prima0, ejercicio1= ejercicio1, prima1=prima1, ejercicio2= ejercicio2, prima2=prima2, tipo="PUT", titulo=titulo, titulo1=titulo1, titulo2=titulo2, titulo3=titulo3)

@aplicacion.route("/mariposaComprada")
def mariposaComprada():
    titulo = "MARIPOSA COMPRADA"
    return render_template("./Estrategias/volatilidad/mariposaComprada.html", titulo=titulo)

@aplicacion.route("/representacionMariposaComprada", methods=['POST'])
def representacionMariposaComprada():
    if request.method == 'POST':
        ejercicio0 = request.form['ejercicio0']
        ejercicio0 = float(ejercicio0)
        prima0 = request.form['prima0']
        prima0 = float(prima0)

        ejercicio1 = request.form['ejercicio1']
        ejercicio1 = float(ejercicio1)
        prima1 = request.form['prima1']
        prima1 = float(prima1)

        ejercicio2 = request.form['ejercicio2']
        ejercicio2 = float(ejercicio2)
        prima2 = request.form['prima2']
        prima2 = float(prima2)

        ejercicio3 = request.form['ejercicio3']
        ejercicio3 = float(ejercicio3)
        prima3 = request.form['prima3']
        prima3 = float(prima3)

        titulo = "MARIPOSA COMPRADA"
        titulo1 = "COMPRA DE CALL"
        titulo2 = "VENTA DE CALL"
        titulo3 = "VENTA DE CALL"
        titulo4 = "COMPRA DE CALL"

        estrategia = MariposaComprada(ejercicio0, prima0, ejercicio1, prima1, ejercicio2, prima2, ejercicio3, prima3)
        r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
    return render_template("./Estrategias/representacionMariposas.html", ruta=r.rutaImagen, ejercicio0=ejercicio0, prima0=prima0, ejercicio1= ejercicio1, prima1=prima1, ejercicio2= ejercicio2, prima2=prima2, ejercicio3=ejercicio3, prima3 = prima3,  tipo="CALL", titulo=titulo, titulo1=titulo1, titulo2=titulo2, titulo3=titulo3, titulo4=titulo4)

@aplicacion.route("/mariposaVendida")
def mariposaVendida():
    titulo = "MARIPOSA VENDIDA"
    return render_template("./Estrategias/volatilidad/mariposaVendida.html", titulo=titulo)

@aplicacion.route("/representacionMariposaVendida", methods=['POST'])
def representacionMariposaVendida():
    if request.method == 'POST':
        ejercicio0 = request.form['ejercicio0']
        ejercicio0 = float(ejercicio0)
        prima0 = request.form['prima0']
        prima0 = float(prima0)

        ejercicio1 = request.form['ejercicio1']
        ejercicio1 = float(ejercicio1)
        prima1 = request.form['prima1']
        prima1 = float(prima1)

        ejercicio2 = request.form['ejercicio2']
        ejercicio2 = float(ejercicio2)
        prima2 = request.form['prima2']
        prima2 = float(prima2)

        ejercicio3 = request.form['ejercicio3']
        ejercicio3 = float(ejercicio3)
        prima3 = request.form['prima3']
        prima3 = float(prima3)

        titulo = "MARIPOSA VENDIDA"
        titulo1 = "VENTA DE CALL"
        titulo2 = "COMPRA DE CALL"
        titulo3 = "COMPRA DE CALL"
        titulo4 = "VENTA DE CALL"

        estrategia = MariposaVendida(ejercicio0, prima0, ejercicio1, prima1, ejercicio2, prima2, ejercicio3, prima3)
        r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
    return render_template("./Estrategias/representacionMariposas.html", ruta=r.rutaImagen, ejercicio0=ejercicio0, prima0=prima0, ejercicio1= ejercicio1, prima1=prima1, ejercicio2= ejercicio2, prima2=prima2, ejercicio3=ejercicio3, prima3 = prima3,  tipo="CALL", titulo=titulo, titulo1=titulo1, titulo2=titulo2, titulo3=titulo3, titulo4=titulo4)

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
            titulo1 = "COMPRA DE " + tipo.upper()
            titulo2 = "VENTA DE " + tipo.upper()
            estrategia = SpreadBajista(ejercicio0, prima0, ejercicio1, prima1, tipoN, contratos0, contratos1)
        if (request.form['estrategia'] == "spreadAlcista"):
            titulo = "SPREAD ALCISTA"
            titulo1 = "COMPRA DE " + tipo.upper()
            titulo2 = "VENTA DE " + tipo.upper()
            estrategia = SpreadAlcista(ejercicio0, prima0,ejercicio1, prima1, tipoN, contratos0,contratos1)
        if (request.form['estrategia'] == "tunelAlcista"):
            tipo=0
            titulo = "TUNEL ALCISTA"
            titulo1 = "COMPRA DE CALL"
            titulo2 = "VENTA DE PUT"
            estrategia = Tunel(ejercicio0, prima0,ejercicio1, prima1, tipo, contratos0,contratos1)
            r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
            return render_template("./Estrategias/representacion.html", ruta=r.rutaImagen,
                                   ejercicio0=ejercicio0, prima0=prima0, ejercicio1=ejercicio1, prima1=prima1,
                                   tipo="CALL y PUT", contratos0=contratos0, contratos1=contratos1, titulo=titulo, titulo1=titulo1, titulo2=titulo2)
        if (request.form['estrategia'] == "tunelBajista"):
            tipo=1
            titulo = "TUNEL BAJISTA"
            titulo2 = "VENTA DE CALL"
            titulo1 = "COMPRA DE PUT"
            estrategia = Tunel(ejercicio0, prima0,ejercicio1, prima1, tipo, contratos0,contratos1)
            r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
            return render_template("./Estrategias/representacion.html", ruta=r.rutaImagen,
                                   ejercicio0=ejercicio1, prima0=prima1, ejercicio1=ejercicio0, prima1=prima0,
                                   tipo="CALL y PUT", contratos0=contratos0, contratos1=contratos1,
                                   titulo=titulo, titulo1=titulo1, titulo2=titulo2)


    r = Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
    return render_template("./Estrategias/representacion.html", ruta=r.rutaImagen, ejercicio0=ejercicio0, prima0=prima0, ejercicio1= ejercicio1, prima1=prima1, tipo=tipo, contratos0=contratos0, contratos1=contratos1, titulo=titulo, titulo1=titulo1, titulo2=titulo2)

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
