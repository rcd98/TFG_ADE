import matplotlib.pyplot as plt
from datetime import datetime

class CompraVentaCallPut(object):

    def __init__(self, precioEjercicio, prima, operacion, tipo, numContratos):
        self.precioEjercicio = precioEjercicio
        self.prima = prima
        self.operacion = operacion
        self.tipo = tipo
        self.rutaImagen = ""
        self.numContratos = numContratos
        if self.operacion == 0 and self.tipo == 0:
            self.rutaImagen = comprarCall(self.precioEjercicio, self.prima, self.numContratos)
        if self.operacion == 0 and self.tipo == 1:
            self.rutaImagen = comprarPut(self.precioEjercicio, self.prima, self.numContratos)
        if self.operacion == 1 and self.tipo == 0:
            self.rutaImagen = venderCall(self.precioEjercicio, self.prima, self.numContratos)
        if self.operacion == 1 and self.tipo == 1:
            self.rutaImagen = venderPut(self.precioEjercicio, self.prima, self.numContratos)

def comprarCall(precioEjercicio, prima, numContratos):
    margen = precioEjercicio * 0.2
    precioSubyacenteInferior = int(precioEjercicio - margen)
    precioSubyacenteSuperior = int(precioEjercicio + margen)
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
    plt.clf()
    plt.style.use('ggplot')
    plt.plot(eje_x,eje_y, linestyle='--', linewidth='3')
    plt.plot(eje_x, eje_0, color='black')
    plt.title('Compra CALL')
    plt.xlabel('Precio activo subyacente (S)')
    plt.ylabel('Beneficio / Perdida')
    plt.grid(True)

    nombre = str(abs(hash(datetime.now())))
    plt.savefig('C:/Users/cxb0354/PycharmProjects/TFG _ADE/static/imgs/' + nombre + '.png')
    return './static/imgs/' + nombre + '.png'

def venderCall(precioEjercicio, prima, numContratos):
    margen = precioEjercicio * 0.2
    precioSubyacenteInferior = int(precioEjercicio - margen)
    precioSubyacenteSuperior = int(precioEjercicio + margen)
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
    plt.clf()
    plt.style.use('ggplot')
    plt.plot(eje_x, eje_y, linestyle='--', linewidth='3')
    plt.plot(eje_x, eje_0, color='black')
    plt.title('venta CALL')
    plt.xlabel('Precio activo subyacente (S)')
    plt.ylabel('Beneficio / Perdida')
    plt.grid(True)

    nombre = str(abs(hash(datetime.now())))
    plt.savefig('C:/Users/cxb0354/PycharmProjects/TFG _ADE/static/imgs/' + nombre + '.png')
    return './static/imgs/' + nombre + '.png'

def comprarPut(precioEjercicio, prima, numContratos):
    margen = precioEjercicio * 0.2
    precioSubyacenteInferior = int(precioEjercicio - margen)
    precioSubyacenteSuperior = int(precioEjercicio + margen)
    eje_y = []
    eje_x = []
    eje_0 = []
    for i in range(precioSubyacenteSuperior, precioSubyacenteInferior - 1, -1):
        eje_x.append(i)
        eje_0.append(0)
        if i <= precioEjercicio:
            eje_y.append(-prima * numContratos)
        else:
            eje_y.append((i - precioEjercicio - prima)* numContratos)
    eje_x = list(eje_x[::-1])

    plt.clf()
    plt.style.use('ggplot')
    plt.plot(eje_x, eje_y, linestyle='--', linewidth='3')
    plt.plot(eje_x, eje_0, color='black')
    plt.title('Compra PUT')
    plt.xlabel('Precio activo subyacente (S)')
    plt.ylabel('Beneficio / Perdida')
    plt.grid(True)

    nombre = str(abs(hash(datetime.now())))
    plt.savefig('C:/Users/cxb0354/PycharmProjects/TFG _ADE/static/imgs/' + nombre + '.png')
    return './static/imgs/' + nombre + '.png'

def venderPut(precioEjercicio, prima, numContratos):
    margen = precioEjercicio * 0.2
    precioSubyacenteInferior = int(precioEjercicio - margen)
    precioSubyacenteSuperior = int(precioEjercicio + margen)
    eje_y = []
    eje_x = []
    eje_0 = []
    for i in range(precioSubyacenteSuperior, precioSubyacenteInferior - 1, -1):
        eje_x.append(i)
        eje_0.append(0)
        if i <= precioEjercicio:
            eje_y.append(prima * numContratos)
        else:
            eje_y.append((i - precioEjercicio - prima) * -1 * numContratos)
    eje_x = list(eje_x[::-1])

    plt.clf()
    plt.style.use('ggplot')
    plt.plot(eje_x, eje_y, linestyle='--', linewidth='3')
    plt.plot(eje_x, eje_0, color='black')
    plt.title('venta PUT')
    plt.xlabel('Precio activo subyacente (S)')
    plt.ylabel('Beneficio / Perdida')
    plt.grid(True)

    nombre = str(abs(hash(datetime.now())))
    plt.savefig('C:/Users/cxb0354/PycharmProjects/TFG _ADE/static/imgs/' + nombre + '.png')
    return './static/imgs/' + nombre + '.png'


