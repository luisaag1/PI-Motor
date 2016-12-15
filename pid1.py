#!/usr/bin/python

import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

ADC.setup()
GPIO.setup("P8_11", GPIO.IN)
PWM.start("P8_13", 0)

while GPIO.input("P8_11") == 0:
	sp = ADC.read("P9_33") * 10
	print round(sp, 2)
	time.sleep(.5)

print "el valor del set point es:", sp
print " "
kp = input("Escribir valor de kp:")
ki = input("Escribir valor de ki:")
print " "
print "El valor de kp es:", kp
print "El valor de ki es:", ki
print " "

inicio = 0

while inicio == 0:
	inicio = input("Presiona 1 para iniciar control... ")
	time.sleep(1)
print "Iniciando control PI de velocidad de  motor de CD de Imanes permanentes..."

e = 1
integrador = 0
integrador_max = 500
integrador_min = -500

while e != 0:
	retro = ADC.read("P9_35") * 4
	print "Motor: ", retro
	e = sp - retro
	pd = kp * e

	integrador = integrador + e
	if integrador > integrador_max:
		integrador = integrador_max
		print "+"
	elif integrador < integrador_min:
		integrador = integrador_min
		print "-"

	pi = integrador * ki
	control = pd + pi
	if control < 0:
		control = 0
	if control > 11:
		control = 11
	controlout = (control * 100) / 11
	for i in range (0, 5):
		PWM.set_duty_cycle("P8_13", controlout)
		time.sleep(.1)		

print "Control terminado, el valor del error es igual a 0"
