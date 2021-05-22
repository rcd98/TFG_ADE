from datetime import datetime


class MariposaVendida(object):

    def __init__(self, pe1, p1, pe2, p2, pe3, p3, pe4, p4):
        if (pe1 < pe2 and pe1 < pe3 and pe1 < pe4 and pe2 == pe3 and pe3 < pe4):
            self.precioEjercicio = pe1
            self.precioEjercicio2 = pe2
            self.precioEjercicio3 = pe3
            self.precioEjercicio4 = pe4
            self.prima = p1
            self.prima2 = p2
            self.prima3 = p3
            self.prima4 = p4
            self.rutaImagen = ""
            self.eje_x = []
            self.eje_y = []
            self.eje_0 = []
            self.nombre = "Mariposa Vendida"

            self.rutaImagen, self.eje_x, self.eje_y, self.eje_0 = mariposaVendida(self.precioEjercicio, self.precioEjercicio2, self.precioEjercicio3, self.precioEjercicio4, self.prima,self.prima2, self.prima3, self.prima4)
        else:
            raise ValueError("No se complen las condiciones de la mariposa vendida")

def mariposaVendida(precioEjercicio, precioEjercicio2, precioEjercicio3, precioEjercicio4, prima, prima2,prima3, prima4):
    multiplo = max(prima, prima2)
    precioSubyacenteInferior = int(precioEjercicio - (multiplo * 5))
    precioSubyacenteSuperior = int(precioEjercicio + (multiplo * 5))

    precioSubyacenteInferior2 = int(precioEjercicio2 - (multiplo * 5))
    precioSubyacenteSuperior2 = int(precioEjercicio2 + (multiplo * 5))

    precioSubyacenteInferior3 = int(precioEjercicio3 - (multiplo * 5))
    precioSubyacenteSuperior3 = int(precioEjercicio3 + (multiplo * 5))

    precioSubyacenteInferior4 = int(precioEjercicio4 - (multiplo * 5))
    precioSubyacenteSuperior4 = int(precioEjercicio4 + (multiplo * 5))

    precioSubyacenteInferior = min(precioSubyacenteInferior, precioSubyacenteInferior2, precioSubyacenteInferior3, precioSubyacenteInferior4)
    precioSubyacenteSuperior = max(precioSubyacenteSuperior, precioSubyacenteSuperior2, precioSubyacenteSuperior3, precioSubyacenteSuperior4)
    eje_y = []
    eje_x = []
    eje_0 = []
    eje_y1 = []
    eje_y2 = []
    eje_y3 = []

    for i in range(precioSubyacenteInferior, precioSubyacenteSuperior + 1):
        eje_x.append(i)
        eje_0.append(0)

        if i <= precioEjercicio:
            eje_y.append(prima)
        else:
            eje_y.append((i - precioEjercicio - prima)*-1)

        if i <= precioEjercicio2:
            eje_y1.append(-prima2)
        else:
            eje_y1.append(i - precioEjercicio2 - prima2)

        if i <= precioEjercicio3:
            eje_y2.append(-prima3)
        else:
            eje_y2.append(i - precioEjercicio3 - prima3)

        if i <= precioEjercicio4:
            eje_y3.append(prima4)
        else:
            eje_y3.append((i - precioEjercicio4 - prima4)*-1)

    eje_y_def = []
    for i in range(len(eje_x)):
        eje_y_def.append(eje_y[i] + eje_y1[i] + eje_y2[i] + eje_y3[i])

    nombre = str(abs(hash(datetime.now())))
    return './static/imgs/' + nombre + '.png', eje_x, eje_y_def, eje_0
