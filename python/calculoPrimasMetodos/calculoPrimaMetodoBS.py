import numpy as np
import math as math
from scipy.stats import norm

class PrimaMetodoBS(object):

    def __init__(self, tipo,  precioActivoSubyacente , precioEjercicio , tiempo, volatilidad, interesNormal, interesLibre ):
        self.tipo = tipo
        self.precioActivoSubyacente = precioActivoSubyacente
        self.precioEjercicio = precioEjercicio
        self.volatilidad = volatilidad / 100

        if interesLibre == 0:
            self.interes = interesNormal / 100
            self.interesLibreRiesgo = np.log(1 + self.interes)

        else:
            self.interes = math.exp(interesLibre / 100) - 1
            self.interesLibreRiesgo = interesLibre / 100
        self.tiempo = tiempo

        self.d1 = (np.log(self.precioActivoSubyacente / self.precioEjercicio) + (self.interesLibreRiesgo + math.pow(self.volatilidad, 2) / 2) * self.tiempo) / (self.volatilidad * math.sqrt(self.tiempo))
        self.d2 = self.d1 - (self.volatilidad * math.sqrt(self.tiempo))
        self.resultado = self.calcularPrima()

    def calcularPrima(self):
        normald1 = norm.cdf(self.d1)
        normald2 = norm.cdf(self.d2)
        exponencial = math.exp(-self.interesLibreRiesgo * self.tiempo)
        resultado = (self.precioActivoSubyacente * normald1) - (self.precioEjercicio * exponencial * normald2)
        if self.tipo == 0:
            return resultado
        else:
            resultado = resultado + self.precioEjercicio * exponencial - self.precioActivoSubyacente
            return resultado



