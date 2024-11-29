from behave import *
from selenium import webdriver
from Funciones.FuncionesTest_01 import FuncionesGlobales


@given(u'Soy un usuario')
def step_impl(context):
    print (u'STEP: Given Soy un usuario')


@when(u'Invoque a la url')
def step_impl(context):
    global driver,f
    context.driver=webdriver.Chrome()
    f=FuncionesGlobales(context.driver)
    context.driver.get("https://www.facebook.com/")
    context.driver.maximize_window()
    f.Tiempo(2)




@then(u'Coloco mis datos e ingreso')
def step_impl(context):
    global driver, f
    f = FuncionesGlobales(context.driver)
    f.Datos()
    f.Tiempo(5)
