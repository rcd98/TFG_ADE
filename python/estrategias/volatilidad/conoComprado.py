from datetime import datetime


class ConoComprado(object):

    def __init__(self, pe1, p1, pe2, p2, numContratos, numContratos2):
        if (pe1 == pe2):
            self.precioEjercicio = pe1
            self.precioEjercicio2 = pe2
            self.prima = p1
            self.prima2 = p2
            self.numContratos = 1
            self.numContratos2 = 1
            self.rutaImagen = ""
            self.eje_x = []
            self.eje_y = []
            self.eje_0 = []
            self.nombre = "Cono Comprado"

            self.rutaImagen, self.eje_x, self.eje_y, self.eje_0 = conoComprado(self.precioEjercicio, self.precioEjercicio2, self.prima,self.prima2, self.numContratos, self.numContratos2)
        else:
            raise ValueError("Los precio de ejercicio deben de ser iguales")

def conoComprado(precioEjercicio, precioEjercicio2, prima, prima2, numContratos, numContratos2):
    multiplo = max(prima, prima2)
    precioSubyacenteInferior = int(precioEjercicio - (multiplo * 5))
    precioSubyacenteSuperior = int(precioEjercicio + (multiplo * 5))

    precioSubyacenteInferior2 = int(precioEjercicio2 - (multiplo * 5))
    precioSubyacenteSuperior2 = int(precioEjercicio2 + (multiplo * 5))

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

        if precioEjercicio2 - i + precioEjercicio2 <= precioEjercicio2:
            eje_y1.append(-prima2 * numContratos2)
        else:
            eje_y1.append((precioEjercicio2 - i - prima2) * numContratos2)

    eje_y_def = []
    for i in range(len(eje_x)):
        eje_y_def.append(eje_y[i] + eje_y1[i])

    nombre = str(abs(hash(datetime.now())))
    return './static/imgs/' + nombre + '.png', eje_x, eje_y_def, eje_0
