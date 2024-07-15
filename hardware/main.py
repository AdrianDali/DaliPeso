#!/usr/bin/env python3
import RPi.GPIO as GPIO  # importa GPIO
from HX711 import HX711  # importa la clase HX711
GPIO.setwarnings(False)  # elimina los warnings
 
try:
    GPIO.setmode(GPIO.BCM)  # Pines GPIO en numeración BCM
    platform_weight = 1530  # Define el peso conocido de la plataforma
    hx = HX711(dout_pin=20, pd_sck_pin=21, platform_weight=platform_weight)
    err = hx.zero()
    if err:
        raise ValueError('La tara no se puede definir.')
    hx.start_periodic_recalibration(interval=60)
    reading = hx.get_raw_data_mean()
    if reading:
        print('Datos restados por compensación pero todavía no convertidos a unidades:',
              reading)
    else:
        print('Dato invalido', reading)
 
    input('Coloque un peso conocido en la balanza y luego presione Enter')
    reading = hx.get_data_mean()
    if reading:
        print('Valor medio de HX711 restado para compensar:', reading)
        known_weight_grams = input(
            'Escriba cuántos gramos eran y presiona Enter: ')
        try:
            value = float(known_weight_grams)
            print(value, 'gramos')
        except ValueError:
            print('Entero o flotante esperado y tengo:',
                  known_weight_grams)
        # muestra uno:  -21.423023147428925
        # -22.38620475376728
        #"-21.391952773030912"
        # -21.283206462637875
        #-21.0812490290508

        ratio = reading / value
        print("reading",reading)
        print("value", value)
        print("RATio:", ratio)
        hx.set_scale_ratio(ratio)
        print('Relación de peso establecida.')
    else:
        raise ValueError('No se puede calcular el valor medio . ERROR', reading)
 
    print("Ahora, leeré datos en un bucle infinito. Para salir presione 'CTRL + C'")
    input('Presione Enter para comenzar a leer')
    while True:
        print("El peso actual en gramos es de %.2f" % (hx.get_weight_mean(100)))
 
except (KeyboardInterrupt, SystemExit):
    print('Chau :)')
 
finally:
    GPIO.cleanup()
