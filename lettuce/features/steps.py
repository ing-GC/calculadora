
# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import Calculadora


@step(u'cuando realizo la operación')
def cuando_realizo_la_operacion(step):
    pass

@step(u'Dado que ingreso los numeros para sumar "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_para_sumar_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.suma(int(num1), int(num2))

@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.cal.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

@step(u'entonces el resultado que obtengo es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = world.ed.obtener_edad()
    assert esperado == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+ obtenido


@step(u'Dado que ingreso los numeros para restar "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_para_restar_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.resta(int(num1), int(num2))

@step(u'Dado que ingreso los numeros para multiplicar "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_para_multiplicar_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.multiplicar(int(num1), int(num2))
@step(u'Dado que ingreso los numeros para dividir "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_para_dividir_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.dividir(int(num1), int(num2))
@step(u'Dado que ingreso los numeros para elevar a una potencia "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_para_elevar_a_una_potencia_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.potencia(int(num1), int(num2))
@step(u'Dado que ingreso el numero para obtener su raiz  "([^"]*)"')
def dado_que_ingreso_el_numero_para_obtener_su_raiz_group1(step, num1):
    world.cal = Calculadora()
    world.cal.raiz(int(num1))

