
import requests
import json

from datetime import datetime

from config import urlTelegram, path


class Telegram():
        

    def mandarMensaje(self, saldoSemanal):
        mensaje = self.generarMensaje(saldoSemanal)
        requests.get(urlTelegram+mensaje)

    def generarMensaje(self, saldoSemanal):
        

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
    



    def test(self):
        print(datetime.today().day)

    def convertirAString(self, s):  
        str1 = "\n" 
        return (str1.join(s)) 







