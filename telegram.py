
import requests
import json

from datetime import datetime

from config import urlTelegram, path


class Telegram():
        

    def mandarMensaje(self):
        mensaje = self.generarMensaje()
        requests.get(urlTelegram+mensaje)

    def generarMensaje(self):
        

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

    def leerArchivoSaldo(self):
        with open(path+'saldo.json', 'r') as saldoEnJson:
            return json.load(saldoEnJson)
  
    def convertirAString(self, s):  
        str1 = "\n" 
        return (str1.join(s)) 

    def guardarEnvioExitoso(self, saldoSemanal):
        saldoSemanal["ultimoReporte"] = int(datetime.today().weekday())
        with open(path+'saldo.json', 'w') as file:
            json.dump(saldoSemanal, file, indent=4)



bot = Telegram()

saldoSemanal = bot.leerArchivoSaldo()
bot.mandarMensaje()



