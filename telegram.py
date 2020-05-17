
import requests
import json

from config import urlTelegram, path


class telegram():
    def __init__(self):
        
        self.mandarMensaje()

    def mandarMensaje(self):
        mensaje = self.generarMensaje()
        requests.get(urlTelegram+mensaje)

    def generarMensaje(self):
        saldoSemanal = self.leerArchivoSaldo()

        mensaje= []
        mensaje.append("<b>Resumen Semanal Wina</b>")
        mensaje.append("")
        mensaje.append("Lunes: "+saldoSemanal["Lunes"])
        mensaje.append("Martes: "+saldoSemanal["Martes"])
        mensaje.append("Miercoles: "+saldoSemanal["Miercoles"])
        mensaje.append("Jueves: "+saldoSemanal["Jueves"])
        mensaje.append("Viernes: "+saldoSemanal["Viernes"])
        mensaje.append("Sabado: "+saldoSemanal["Sabado"])
        mensaje.append("Domingo: "+saldoSemanal["Domingo"])
        # mensaje.append("")
        # mensaje.append("")
        # mensaje.append("<b>Resumen Detallado Wina</b>")
        # mensaje.append("")

        return self.convertirAString(mensaje)
    




    def leerArchivoSaldo(self):
        with open(path+'saldo.json', 'r') as saldoEnJson:
            return json.load(saldoEnJson)
  
    def convertirAString(self, s):  
        str1 = "\n" 
        return (str1.join(s)) 





bot = telegram()
