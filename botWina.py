#Json
import json

#Calendario
from datetime import datetime

#Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Credenciales
from credenciales import varUsuario, varClave





class botWina():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://allaria-ssl.allaria.com.ar/AllariaOnline/VBolsaNet/login.html")

        self.esperar('//*[@id="btnIngresar"]')

        usuario = self.driver.find_element_by_xpath('//*[@id="input_0"]')
        usuario.send_keys(varUsuario)

        clave =  self.driver.find_element_by_xpath('//*[@id="input_1"]')
        clave.send_keys(varClave)

        botonLogin = self.driver.find_element_by_xpath('//*[@id="btnIngresar"]')
        botonLogin.click()

    def leerYGuardarSaldo(self):
        self.esperar('//*[@id="view-container"]/div/div[2]/div/div/div/div/div/ng-transclude/div[1]/span[1]/div')

        saldoDeHoy = self.driver.find_element_by_xpath('//*[@id="view-container"]/div/div[2]/div/div/div/div/div/ng-transclude/div[1]/span[1]/div').text
        saldoSemanal = self.leerArchivoSaldo()
        
        numeroDeDia = int(datetime.today().weekday())
        nombreDiaDeHoy = self.definirDia(numeroDeDia)
        saldoSemanal[nombreDiaDeHoy] = self.limpiarStringMonto(saldoDeHoy)
        
        self.escribirArchivoSaldo(saldoSemanal)

    def enviarResumenSemanal(self):
        if("is_sabado" == "enviarportelegram"):
            print("programar esto")





    def escribirArchivoSaldo(self, saldoSemanal):
        with open('saldo.json', 'w') as file:
            json.dump(saldoSemanal, file, indent=4)

    def leerArchivoSaldo(self):
        with open('saldo.json', 'r') as saldoEnJson:
            return json.load(saldoEnJson)

    def esperar(self, path):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, path)))
        
    def limpiarStringMonto(self, monto):
        monto = monto.replace(".", "")
        monto = monto.replace("$", "")
        monto = monto.replace(",", ".")
        return monto
    
    def definirDia(self, diaInt):
        definirDiaSwitch = {
            0: 'Lunes',
            1: 'Martes',
            2: 'Miercoles',
            3: 'Jueves',
            4: 'Viernes',
            5: 'Sabado',
            6: 'Domingo'
        }
        return definirDiaSwitch.get(diaInt, "Dia Invalido")

     

bot = botWina()
bot.login()
bot.leerYGuardarSaldo()
bot.enviarResumenSemanal()

