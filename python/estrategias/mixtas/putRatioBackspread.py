from datetime import datetime


class PutRatioBackspread(object):

    def __init__(self, pe1, p1, pe2, p2, pe3, p3):
        if (pe1 > pe2  and pe2 == pe3):
            self.precioEjercicio = pe1
            self.precioEjercicio2 = pe2
            self.precioEjercicio3 = pe3
            self.prima = p1
            self.prima2 = p2
            self.prima3 = p3
            self.rutaImagen = ""
            self.eje_x = []
            self.eje_y = []
            self.eje_0 = []
            self.nombre = "Put Ratio Backspread"

            self.rutaImagen, self.eje_x, self.eje_y, self.eje_0 = putRatioBackspread(self.precioEjercicio, self.precioEjercicio2, self.precioEjercicio3, self.prima,self.prima2, self.prima3)
        else:
            raise ValueError("No se complen las condiciones del Put Ratio Backspread")

def putRatioBackspread(precioEjercicio, precioEjercicio2, precioEjercicio3, prima, prima2,prima3):
    multiplo = max(prima, prima2, prima3)
    precioSubyacenteInferior = int(precioEjercicio - (multiplo * 5))
    precioSubyacenteSuperior = int(precioEjercicio + (multiplo * 5))

    precioSubyacenteInferior2 = int(precioEjercicio2 - (multiplo * 5))
    precioSubyacenteSuperior2 = int(precioEjercicio2 + (multiplo * 5))

    precioSubyacenteInferior3 = int(precioEjercicio3 - (multiplo * 5))
    precioSubyacenteSuperior3 = int(precioEjercicio3 + (multiplo * 5))

    precioSubyacenteInferior = min(precioSubyacenteInferior, precioSubyacenteInferior2, precioSubyacenteInferior3)
    precioSubyacenteSuperior = max(precioSubyacenteSuperior, precioSubyacenteSuperior2, precioSubyacenteSuperior3)
    eje_y = []
    eje_x = []
    eje_0 = []
    eje_y1 = []
    eje_y2 = []

    for i in range(precioSubyacenteInferior, precioSubyacenteSuperior + 1):
        eje_x.append(i)
        eje_0.append(0)

        if precioEjercicio - i + precioEjercicio <= precioEjercicio:
            eje_y.append(prima)
        else:
            eje_y.append((precioEjercicio - i - prima) * -1)

        if i >= precioEjercicio2:
            eje_y1.append(-prima2)
        else:
            eje_y1.append((precioEjercicio2 - i - prima2))

        if i >= precioEjercicio3:
            eje_y2.append(-prima3)
        else:
            eje_y2.append((precioEjercicio3 - i - prima3))


    eje_y_def = []
    for i in range(len(eje_x)):
        eje_y_def.append(eje_y[i] + eje_y1[i] + eje_y2[i])

    nombre = str(abs(hash(datetime.now())))
    return './static/imgs/' + nombre + '.png', eje_x, eje_y_def, eje_0
