from datetime import datetime

class EstrategiasBasicas(object):

    def __init__(self, precioEjercicio, prima, operacion, tipo, numContratos):
        self.precioEjercicio = precioEjercicio
        self.prima = prima
        self.operacion = operacion
        self.tipo = tipo
        self.numContratos = numContratos
        self.numContratos = 1
        self.eje_x = []
        self.eje_y = []
        self.eje_0 = []
        self.nombre = ""
        if self.operacion == 0 and self.tipo == 0:
            self.nombre = "Compra Call"
            self.eje_x, self.eje_y, self.eje_0  = comprarCall(self.precioEjercicio, self.prima, self.numContratos)
        if self.operacion == 0 and self.tipo == 1:
            self.nombre = "Compra Put"
            self.eje_x, self.eje_y, self.eje_0 = comprarPut(self.precioEjercicio, self.prima, self.numContratos)
        if self.operacion == 1 and self.tipo == 0:
            self.nombre = "Venta Call"
            self.eje_x, self.eje_y, self.eje_0 = venderCall(self.precioEjercicio, self.prima, self.numContratos)
        if self.operacion == 1 and self.tipo == 1:
            self.nombre = "Venta Put"
            self.eje_x, self.eje_y, self.eje_0 = venderPut(self.precioEjercicio, self.prima, self.numContratos)

def comprarCall(precioEjercicio, prima, numContratos):
    precioSubyacenteInferior = int(precioEjercicio - (prima * 2))
    precioSubyacenteSuperior = int(precioEjercicio + (prima * 2))
    eje_y = []
    eje_x = []
    eje_0 = []
    for i in range(precioSubyacenteInferior, precioSubyacenteSuperior + 1):
        eje_x.append(i)
        eje_0.append(0)
        if i <=  precioEjercicio:
            eje_y.append(-prima*numContratos)
        else:
            eje_y.append((i - precioEjercicio - prima)*numContratos)

    return eje_x, eje_y, eje_0

def venderCall(precioEjercicio, prima, numContratos):
    precioSubyacenteInferior = int(precioEjercicio - (prima * 2))
    precioSubyacenteSuperior = int(precioEjercicio + (prima * 2))
    eje_y = []
    eje_x = []
    eje_0 = []
    for i in range(precioSubyacenteInferior, precioSubyacenteSuperior + 1):
        eje_x.append(i)
        eje_0.append(0)
        if i <= precioEjercicio:
            eje_y.append(prima * numContratos)
        else:
            eje_y.append((i - precioEjercicio - prima)*-1*numContratos)

    return eje_x, eje_y, eje_0

def comprarPut(precioEjercicio, prima, numContratos):
    precioSubyacenteInferior = int(precioEjercicio - (prima * 2))
    precioSubyacenteSuperior = int(precioEjercicio + (prima * 2))
    eje_y = []
    eje_x = []
    eje_0 = []
    for i in range(precioSubyacenteInferior, precioSubyacenteSuperior + 1):
        eje_x.append(i)
        eje_0.append(0)
        if i >= precioEjercicio:
            eje_y.append(-prima * numContratos)
        else:
            eje_y.append((precioEjercicio - i - prima) * numContratos)

    return eje_x, eje_y, eje_0

def venderPut(precioEjercicio, prima, numContratos):
    precioSubyacenteInferior = int(precioEjercicio - (prima * 2))
    precioSubyacenteSuperior = int(precioEjercicio + (prima * 2))
    eje_y = []
    eje_x = []
    eje_0 = []
    for i in range(precioSubyacenteInferior, precioSubyacenteSuperior + 1):
        eje_x.append(i)
        eje_0.append(0)
        if i >= precioEjercicio:
            eje_y.append(prima * numContratos)
        else:
            eje_y.append((precioEjercicio - i - prima) * -1 * numContratos)

    return eje_x, eje_y, eje_0
