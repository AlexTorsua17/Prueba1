import time
from os import times_result


class FuncionesGlobales ():
    def __init__(self, driver):
        self.driver = driver


    def Tiempo(self,x):
        t=time.sleep(x)
        return t
