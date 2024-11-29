import time
from os import times_result


class FuncionesGlobales ():
    def __init__(self, driver):
        self.driver = driver


    def Tiempo(self,x):
        t=time.sleep(x)
        return t

    def Datos(self):
        driver=self.driver
        us = driver.find_element("xpath", '//*[@id="email"]')
        us.send_keys("alex_torres_suazo@hotmail.com")
        time.sleep(2)

        us1= driver.find_element("xpath", '//*[@id="pass"]')
        us1.send_keys("Alex970725743*")
        time.sleep(2)

        us2 = driver.find_element("xpath", '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
        us2.click()
        time.sleep(2)
