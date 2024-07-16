# worker.py

import time
from PyQt5.QtCore import QObject, pyqtSignal
import RPi.GPIO as GPIO
from hardware.HX711 import HX711

class WeightReader(QObject):
    weight_updated = pyqtSignal(float)

    def __init__(self):
        super().__init__()
        self.hx = None

    def read_weight(self):
        GPIO.setmode(GPIO.BCM)
        platform_weight = 1530
        known_ratio = -21.38620475376728
        self.hx = HX711(dout_pin=20, pd_sck_pin=21, platform_weight=platform_weight)

        # Tara inicial
        err = self.hx.zero()
        if err:
            raise ValueError('La tara no se puede definir.')

        # Establecer el ratio conocido directamente
        self.hx.set_scale_ratio(known_ratio)
        print('Relación de peso establecida utilizando el ratio conocido.')
        print(f"Ratio: {known_ratio}")

        while True:
            peso_actual = self.hx.get_weight_mean(100)
            self.weight_updated.emit(peso_actual)
            time.sleep(1)  # Intervalo de actualización
