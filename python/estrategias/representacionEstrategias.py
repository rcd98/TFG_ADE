import matplotlib.pyplot as plt
from datetime import datetime


class Representacion():

    def __init__(self, eje_x, eje_y, eje_0, titulo):
        self.eje_x = eje_x
        self.eje_y = eje_y
        self.eje_0 = eje_0
        plt.clf()
        plt.style.use('ggplot')
        plt.plot(eje_x, eje_y, linestyle='--', linewidth='3')
        plt.plot(eje_x, eje_0, color='black')
        plt.title(titulo)
        plt.xlabel('Precio activo subyacente (S)')
        plt.ylabel('Beneficio / Perdida')
        nombre = str(abs(hash(datetime.now())))
        self.rutaImagen = 'static/imgs/' + nombre + '.png'
        plt.savefig(self.rutaImagen)
        plt.grid(True)
        plt.close()
