#Imports Base
from selenium import webdriver
from time import sleep

#Json
import json

#Calendario
from datetime import datetime




from credenciales import varUsuario, varClave

class botWina():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://allaria-ssl.allaria.com.ar/AllariaOnline/VBolsaNet/login.html")

        sleep(3)

        usuario = self.driver.find_element_by_xpath('//*[@id="input_0"]')
        usuario.send_keys(varUsuario)

        clave =  self.driver.find_element_by_xpath('//*[@id="input_1"]')
        clave.send_keys(varClave)

        botonLogin = self.driver.find_element_by_xpath('//*[@id="btnIngresar"]')
        botonLogin.click()

        sleep(15)

        #Me traigo el saldo
        saldo = self.driver.find_element_by_xpath('//*[@id="view-container"]/div/div[2]/div/div/div/div/div/ng-transclude/div[1]/span[1]/div').text

        #creo un json para guardar todo
        saldoSemanal = {}
        dia = self.definirDia()
        saldoSemanal[dia] = saldo
        
       
        
        

        

        #guardo el json en un archivo
        with open('saldo.json', 'w') as file:
            json.dump(saldoSemanal, file, indent=4)

    def test(self):
        
        print(datetime.today().weekday())
    
    def definirDia(diaInt):
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

