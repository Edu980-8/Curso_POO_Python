import pandas as pd;

class Archivo_csv():
    
    def __init__(self, ruta):
        self.ruta=ruta
    def leerArchivo(self):
        df = pd.read_csv(self.ruta)
        return df
    def analizarArchivo(self,data):
        analisis = data.describe()
        return analisis


ruta = "music.csv"
archivo = Archivo_csv(ruta)
data = archivo.leerArchivo()
print(data)
analisis = archivo.analizarArchivo(data)
print(analisis)

