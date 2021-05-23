import numpy as np

from python.calculoPrimasMetodos.calculoPrimaMetodoBS import PrimaMetodoBS
from python.calculoPrimasMetodos.calculoPrimaMetodoBinomial import PrimaMetodoBinomial
from python.estrategias.basicas.estrategiasBasicas import EstrategiasBasicas
from python.estrategias.mixtas.callRatioBackspread import CallRatioBackspread
from python.estrategias.mixtas.putRatioBackspread import PutRatioBackspread
from python.estrategias.mixtas.ratioCallSpread import RatioCallSpread
from python.estrategias.mixtas.ratioPutSpread import RatioPutSpread
from python.estrategias.representacionEstrategias import Representacion
from python.estrategias.tendencia.spreadBajista import SpreadBajista
from python.estrategias.tendencia.tunel import Tunel
from python.estrategias.volatilidad.conoComprado import ConoComprado
from python.estrategias.volatilidad.conoVendido import ConoVendido
from python.estrategias.volatilidad.cunaComprada import CunaComprada
from python.estrategias.volatilidad.cunaVendida import CunaVendida
from python.estrategias.volatilidad.mariposaComprada import MariposaComprada
from python.estrategias.volatilidad.mariposaVendida import MariposaVendida

"""
estrategia = EstrategiasBasicas(100, 5, 0, 0, 1)
Representacion(estrategia.rutaImagen, estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)

estrategia = EstrategiasBasicas(100, 50, 0, 1, 1)
Representacion(estrategia.rutaImagen, estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)

estrategia = EstrategiasBasicas(100, 5, 1, 0, 1)
Representacion(estrategia.rutaImagen, estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)


estrategia = EstrategiasBasicas(100, 5, 1, 1, 1)
Representacion(estrategia.rutaImagen, estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)

estrategia = SpreadAlcista(135,6, 145, 1, 0, 1, 1)
Representacion(estrategia.rutaImagen, estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)

estrategia = SpreadBajista(44,0.7, 42, 1.65, 0, 1, 1)
Representacion(estrategia.rutaImagen, estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)

estrategia = Tunel(17,0.15, 16, 0.2, 1, 1)
Representacion(estrategia.rutaImagen, estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)
estrategia = EstrategiasBasicas(100, 5, 0, 0, 1)
Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)


"""
estrategia = ConoVendido(100, 5, 100, 5,1,1)
print(estrategia.eje_x)
print(estrategia.eje_y)
print(estrategia.eje_0)
Representacion(estrategia.eje_x, estrategia.eje_y, estrategia.eje_0, estrategia.nombre)