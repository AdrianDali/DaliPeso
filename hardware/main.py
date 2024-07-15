#!/usr/bin/env python3
import RPi.GPIO as GPIO  # importa GPIO
from HX711 import HX711  # importa la clase HX711
GPIO.setwarnings(False)  # elimina los warnings

try:
    GPIO.setmode(GPIO.BCM)  # Pines GPIO en numeración BCM
    platform_weight = 1530  # Define el peso conocido de la plataforma
    known_ratio = -21.38620475376728  # Define el ratio conocido basado en tus pruebas anteriores
    hx = HX711(dout_pin=20, pd_sck_pin=21, platform_weight=platform_weight)
    
    # Tara inicial
    err = hx.zero()
    if err:
        raise ValueError('La tara no se puede definir.')
    
    # Establecer el ratio conocido directamente
    hx.set_scale_ratio(known_ratio)
    print('Relación de peso establecida utilizando el ratio conocido.')
    print(f"Ratio: {known_ratio}")
    
    # Iniciar recalibración periódica
    hx.start_periodic_recalibration(interval=60)

    print("Ahora, leeré datos en un bucle infinito. Para salir presione 'CTRL + C'")
    input('Presione Enter para comenzar a leer')
    while True:
        peso_actual = hx.get_weight_mean(100)
        print("El peso actual en gramos es de %.2f" % peso_actual)
        if peso_actual < 0:
            print("Advertencia: Peso negativo detectado. Verificar calibración.")

except (KeyboardInterrupt, SystemExit):
    print('Chau :)')

finally:
    GPIO.cleanup()
