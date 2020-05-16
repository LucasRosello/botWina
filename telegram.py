
import requests
import json

from config import urlTelegram


class telegram():
    def __init__(self):
        self.mandarMensaje()

    def mandarMensaje(self):
        mensaje = "<b>Resumen semanal</b>\n\nLunes:17000\nMartes:2\nMiercoles:3423423\nJueves:2\nViernes:Tal&parse_mode=HTML"
        requests.get(urlTelegram+mensaje)


bot = telegram()
