import numpy as np
import math as math
from scipy.stats import binom

class PrimaMetodoBinomial(object):

    def __init__(self, tipo,  precioActivoSubyacente , precioEjercicio , tiempo, volatilidad, pasos, interesNormal, interesLibre):
        self.tipo = tipo
        self.precioActivoSubyacente = precioActivoSubyacente
        self.precioEjercicio = precioEjercicio
        self.volatilidad = volatilidad / 100

        self.tiempo = tiempo
        self.pasos = pasos
        self.incremento = tiempo / pasos
        if interesLibre == 0:
            self.interes = interesNormal / 100
            self.interesLibreRiesgo = np.log(1 + self.interes)

        else:
            self.interes = math.exp(interesLibre / 100) - 1
            self.interesLibreRiesgo = interesLibre / 100

        self.factorSubida = math.exp(self.volatilidad * math.sqrt(self.incremento))
        self.factorBajada = 1 / self.factorSubida

        self.probabilidadSubida = (math.exp(self.incremento * self.interesLibreRiesgo) - self.factorBajada) / (self.factorSubida - self.factorBajada)
        self.probabilidadBajada = 1 - self.probabilidadSubida

        self.resultado = self.calcularPrima()

    def calcularPrima(self):
        rama = []
        preciosActivoSubyacente = []
        valoresIntrinsecos = []
        valoresBinomial = []
        resultado = 0.0

        for i in range(self.pasos + 1):
            rama.append(i)
        for i in range(self.pasos + 1):
            preciosActivoSubyacente.append(self.precioActivoSubyacente * pow(self.factorSubida, self.pasos - i) * pow(self.factorBajada, i)  )
        for i in range(self.pasos + 1):
            if self.tipo == 0:
                valoresIntrinsecos.append(max(0, preciosActivoSubyacente[i] - self.precioEjercicio))
            else:
                valoresIntrinsecos.append(max(0, self.precioEjercicio - preciosActivoSubyacente[i]))
        for i in range(self.pasos + 1):
            valoresBinomial.append(binom.pmf(self.pasos - i, self.pasos, self.probabilidadSubida))
            resultado += valoresIntrinsecos[i] * valoresBinomial[i]

        return resultado / pow((1 + self.interes), self.tiempo)
