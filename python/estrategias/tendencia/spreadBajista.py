from datetime import datetime



class SpreadBajista(object):

    def __init__(self, pe1, p1, pe2, p2, tipo, numContratos, numContratos2):
        if (pe1 > pe2):
            self.precioEjercicio = pe1
            self.precioEjercicio2 = pe2
            self.prima = p1
            self.prima2 = p2
            self.tipo = tipo
            self.numContratos = 1
            self.numContratos2 = 1
            self.rutaImagen = ""
            self.eje_x = []
            self.eje_y = []
            self.eje_0 = []
            self.nombre = "Spread Bajista"
            if self.tipo == 0:
                self.rutaImagen, self.eje_x, self.eje_y, self.eje_0 = spreadBajistaCall(self.precioEjercicio, self.precioEjercicio2, self.prima,self.prima2, self.numContratos, self.numContratos2)
            if  self.tipo == 1:
                self.rutaImagen, self.eje_x, self.eje_y, self.eje_0 = spreadBajistaPut(self.precioEjercicio, self.precioEjercicio2, self.prima,self.prima2, self.numContratos, self.numContratos2)
        else:
            raise ValueError("El precio de ejercicio de la compra tiene que ser mayor que el de la venta")

def spreadBajistaCall(precioEjercicio, precioEjercicio2, prima, prima2, numContratos, numContratos2):
    multiplo = max(prima, prima2)
    precioSubyacenteInferior = int(precioEjercicio - (multiplo * 2))
    precioSubyacenteSuperior = int(precioEjercicio + (multiplo * 2))

    precioSubyacenteInferior2 = int(precioEjercicio2 - (multiplo * 2))
    precioSubyacenteSuperior2 = int(precioEjercicio2 + (multiplo * 2))

    precioSubyacenteInferior = min(precioSubyacenteInferior, precioSubyacenteInferior2)
    precioSubyacenteSuperior = max(precioSubyacenteSuperior, precioSubyacenteSuperior2)
    eje_y = []
    eje_x = []
    eje_0 = []
    eje_y1 = []
    for i in range(precioSubyacenteInferior, precioSubyacenteSuperior + 1):
        eje_x.append(i)
        eje_0.append(0)
        if i <= precioEjercicio:
            eje_y.append(-prima * numContratos)
        else:
            eje_y.append((i - precioEjercicio - prima) * numContratos)

        if i <= precioEjercicio2:
            eje_y1.append(prima2 * numContratos2)
        else:
            eje_y1.append((i - precioEjercicio2 - prima2) * -1 * numContratos2)

    eje_y_def = []
    for i in range(len(eje_x)):
        eje_y_def.append(eje_y[i] + eje_y1[i])

    nombre = str(abs(hash(datetime.now())))
    return './static/imgs/' + nombre + '.png', eje_x, eje_y_def, eje_0

def spreadBajistaPut(precioEjercicio, precioEjercicio2, prima, prima2, numContratos, numContratos2):
    multiplo = max(prima, prima2)
    precioSubyacenteInferior = int(precioEjercicio - (multiplo * 2))
    precioSubyacenteSuperior = int(precioEjercicio + (multiplo * 2))

    precioSubyacenteInferior2 = int(precioEjercicio2 - (multiplo * 2))
    precioSubyacenteSuperior2 = int(precioEjercicio2 + (multiplo * 2))

    precioSubyacenteInferior = min(precioSubyacenteInferior, precioSubyacenteInferior2)
    precioSubyacenteSuperior = max(precioSubyacenteSuperior, precioSubyacenteSuperior2)

    eje_y = []
    eje_x = []
    eje_0 = []
    eje_y1 = []

    for i in range(precioSubyacenteInferior, precioSubyacenteSuperior + 1):
        eje_x.append(i)
        eje_0.append(0)
        if i >= precioEjercicio:
            eje_y.append(-prima * numContratos)
        else:
            eje_y.append((precioEjercicio - i - prima) * numContratos)

        if i >= precioEjercicio2:
            eje_y1.append(prima2 * numContratos2)
        else:
            eje_y1.append((precioEjercicio2 - i - prima2) * -1 * numContratos2)

    eje_y_def = []
    for i in range(len(eje_x)):
        eje_y_def.append(eje_y[i] + eje_y1[i])
    nombre = str(abs(hash(datetime.now())))
    return './static/imgs/' + nombre + '.png', eje_x, eje_y_def, eje_0
