import statistics as stat
import time
import RPi.GPIO as GPIO
import threading

class HX711:
    """
    HX711 represents chip for reading load cells.
    """

    def __init__(self, dout_pin, pd_sck_pin, platform_weight=0, gain_channel_A=128, select_channel='A'):
        """
        Init a new instance of HX711

        Args:
            dout_pin(int): Raspberry Pi pin number where the Data pin of HX711 is connected.
            pd_sck_pin(int): Raspberry Pi pin number where the Clock pin of HX711 is connected.
            platform_weight(float): Known weight of the platform.
            gain_channel_A(int): Optional, by default value 128. Options (128 || 64)
            select_channel(str): Optional, by default 'A'. Options ('A' || 'B')

        Raises:
            TypeError: if pd_sck_pin or dout_pin are not int type
        """
        if isinstance(dout_pin, int):
            if isinstance(pd_sck_pin, int):
                self._pd_sck = pd_sck_pin
                self._dout = dout_pin
            else:
                raise TypeError('pd_sck_pin must be type int. '
                                'Received pd_sck_pin: {}'.format(pd_sck_pin))
        else:
            raise TypeError('dout_pin must be type int. '
                            'Received dout_pin: {}'.format(dout_pin))

        self._gain_channel_A = 0
        self._offset_A_128 = 0  # offset for channel A and gain 128
        self._offset_A_64 = 0  # offset for channel A and gain 64
        self._offset_B = 0  # offset for channel B
        self._last_raw_data_A_128 = 0
        self._last_raw_data_A_64 = 0
        self._last_raw_data_B = 0
        self._wanted_channel = ''
        self._current_channel = ''
        self._scale_ratio_A_128 = 1  # scale ratio for channel A and gain 128
        self._scale_ratio_A_64 = 1  # scale ratio for channel A and gain 64
        self._scale_ratio_B = 1  # scale ratio for channel B
        self._debug_mode = False
        self._data_filter = outliers_filter  # default it is used outliers_filter

        self._rounding_threshold = 0.9  # Puedes ajustar este umbral según sea necesario
        self._platform_weight = platform_weight  # Peso de la plataforma conocida

        GPIO.setup(self._pd_sck, GPIO.OUT)  # pin _pd_sck is output only
        GPIO.setup(self._dout, GPIO.IN)  # pin _dout is input only
        self.select_channel(select_channel)
        self.set_gain_A(gain_channel_A)
        #self._calibrate()
        
    

    def _calibrate(self):
        """
        Calibrate the HX711 by setting the offset based on the known platform weight.
        """
        initial_reading = self.get_raw_data_mean(30)
        if initial_reading is not False:
            self._offset_A_128 = initial_reading
        else:
            raise Exception("Calibración inicial fallida.")

    def start_periodic_recalibration(self, interval=60):
        """
        Start periodic recalibration to adjust the offset periodically.

        Args:
            interval(int): Interval in seconds for recalibration. Default is 300 seconds (5 minutes).
        """
        def recalibrate():
            while True:
                time.sleep(interval)
                current_weight = self.get_weight_mean(30)  # Obtener el peso actual
                print(f"Peso actual: {current_weight} g")  # Imprimir el peso actual para depuración
                if current_weight < 1.5:  # Verificar si el peso es menor a uno
                    print("Inicia recalibración")
                    self.zero()

        recalibration_thread = threading.Thread(target=recalibrate)
        recalibration_thread.daemon = True
        recalibration_thread.start()


    def _custom_round(self, value, threshold=0.1):
        if abs(value) < threshold:
            return 0.0
        return round(value, 2)

    def select_channel(self, channel):
        """
        select_channel method evaluates if the desired channel
        is valid and then sets the _wanted_channel variable.

        Args:
            channel(str): the channel to select. Options ('A' || 'B')
        Raises:
            ValueError: if channel is not 'A' or 'B'
        """
        channel = channel.capitalize()
        if channel == 'A':
            self._wanted_channel = 'A'
        elif channel == 'B':
            self._wanted_channel = 'B'
        else:
            raise ValueError('Parameter "channel" has to be "A" or "B". '
                             'Received: {}'.format(channel))
        # after changing channel or gain it has to wait 50 ms to allow adjustment.
        # the data before is garbage and cannot be used.
        self._read()
        time.sleep(0.5)

    def set_gain_A(self, gain):
        """
        set_gain_A method sets gain for channel A.
        
        Args:
            gain(int): Gain for channel A (128 || 64)
        
        Raises:
            ValueError: if gain is different than 128 or 64
        """
        if gain == 128:
            self._gain_channel_A = gain
        elif gain == 64:
            self._gain_channel_A = gain
        else:
            raise ValueError('gain has to be 128 or 64. '
                             'Received: {}'.format(gain))
        # after changing channel or gain it has to wait 50 ms to allow adjustment.
        # the data before is garbage and cannot be used.
        self._read()
        time.sleep(0.5)

    def zero(self, readings=30):
        """
        zero es un método que establece los datos actuales como un offset
        para un canal particular. Se puede usar para restar el peso del empaque.
        También conocido como tara.

        Args:
            readings(int): Número de lecturas para el promedio. Valores permitidos 1..99

        Raises:
            ValueError: si readings no está en el rango 1..99

        Returns: True si ocurrió un error.
        """
        if readings > 0 and readings < 100:
            result = self.get_raw_data_mean(readings)
            if result != False:
                if self._current_channel == 'A' and self._gain_channel_A == 128:
                    self._offset_A_128 = result
                    return False
                elif self._current_channel == 'A' and self._gain_channel_A == 64:
                    self._offset_A_64 = result
                    return False
                elif self._current_channel == 'B':
                    self._offset_B = result
                    return False
                else:
                    if self._debug_mode:
                        print('No se puede poner a cero () canal y ganancia no coinciden.\n'
                            'canal actual: {}\n'
                            'ganancia A: {}\n'.format(self._current_channel,
                                                        self._gain_channel_A))
                    return True
            else:
                if self._debug_mode:
                    print('Desde el método "zero()".\n'
                        'get_raw_data_mean(readings) devolvió False.\n')
                return True
        else:
            raise ValueError('El parámetro "readings" '
                            'debe estar en el rango de 1 a 99. '
                            'Recibido: {}'.format(readings))


    def set_offset(self, offset, channel='', gain_A=0):
        """
        set offset method sets desired offset for specific
        channel and gain. Optional, by default it sets offset for current
        channel and gain.
        
        Args:
            offset(int): specific offset for channel
            channel(str): Optional, by default it is the current channel.
                Or use these options ('A' || 'B')
        
        Raises:
            ValueError: if channel is not ('A' || 'B' || '')
            TypeError: if offset is not int type
        """
        channel = channel.capitalize()
        if isinstance(offset, int):
            if channel == 'A' and gain_A == 128:
                self._offset_A_128 = offset
                return
            elif channel == 'A' and gain_A == 64:
                self._offset_A_64 = offset
                return
            elif channel == 'B':
                self._offset_B = offset
                return
            elif channel == '':
                if self._current_channel == 'A' and self._gain_channel_A == 128:
                    self._offset_A_128 = offset
                    return
                elif self._current_channel == 'A' and self._gain_channel_A == 64:
                    self._offset_A_64 = offset
                    return
                else:
                    self._offset_B = offset
                    return
            else:
                raise ValueError('Parameter "channel" has to be "A" or "B". '
                                 'Received: {}'.format(channel))
        else:
            raise TypeError('Parameter "offset" has to be integer. '
                            'Received: ' + str(offset) + '\n')

    def set_scale_ratio(self, scale_ratio, channel='', gain_A=0):
        """
        El método set_scale_ratio establece la relación de conversión
        para calcular el peso en las unidades deseadas. Para encontrar esta relación,
        por ejemplo en gramos o kg, debe conocerse un peso conocido.

        Args:
            scale_ratio(float): número > 0.0 que se usa para
                la conversión a unidades de peso.
            channel(str): Opcional, por defecto es el canal actual.
                O usar estas opciones ('a'|| 'A' || 'b' || 'B')
            gain_A(int): Opcional, por defecto es el canal actual.
                O usar estas opciones (128 || 64)
        Raises:
            ValueError: si el canal no es ('A' || 'B' || '')
            TypeError: si el offset no es de tipo int
        """
        channel = channel.capitalize()  # Capitaliza el canal para asegurar que sea 'A' o 'B'
        if isinstance(gain_A, int):  # Verifica que gain_A sea de tipo int
            if channel == 'A' and gain_A == 128:
                self._scale_ratio_A_128 = scale_ratio
                return
            elif channel == 'A' and gain_A == 64:
                self._scale_ratio_A_64 = scale_ratio
                return
            elif channel == 'B':
                self._scale_ratio_B = scale_ratio
                return
            elif channel == '':
                if self._current_channel == 'A' and self._gain_channel_A == 128:
                    self._scale_ratio_A_128 = scale_ratio
                    return
                elif self._current_channel == 'A' and self._gain_channel_A == 64:
                    self._scale_ratio_A_64 = scale_ratio
                    return
                else:
                    self._scale_ratio_B = scale_ratio
                    return
            else:
                raise ValueError('El parámetro "channel" tiene que ser "A" o "B". '
                                'recibido: {}'.format(channel))
        else:
            raise TypeError('El parámetro "gain_A" tiene que ser un entero. '
                            'Recibido: ' + str(gain_A) + '\n')


    def set_data_filter(self, data_filter):
        """
        set_data_filter method sets data filter that is passed as an argument.

        Args:
            data_filter(data_filter): Data filter that takes list of int numbers and
                returns a list of filtered int numbers.
        
        Raises:
            TypeError: if filter is not a function.
        """
        if callable(data_filter):
            self._data_filter = data_filter
        else:
            raise TypeError('Parameter "data_filter" must be a function. '
                            'Received: {}'.format(data_filter))

    def set_debug_mode(self, flag=False):
        """
        set_debug_mode method is for turning on and off
        debug mode.
        
        Args:
            flag(bool): True turns on the debug mode. False turns it off.
        
        Raises:
            ValueError: if flag is not bool type
        """
        if flag == False:
            self._debug_mode = False
            print('Debug mode DISABLED')
            return
        elif flag == True:
            self._debug_mode = True
            print('Debug mode ENABLED')
            return
        else:
            raise ValueError('Parameter "flag" can be only BOOL value. '
                             'Received: {}'.format(flag))

    def _save_last_raw_data(self, channel, gain_A, data):
        """
        _save_last_raw_data guarda la última lectura de datos en bruto para un canal y ganancia específicos.
        
        Args:
            channel(str): El canal seleccionado ('A' o 'B').
            gain_A(int): La ganancia seleccionada (128 o 64 para el canal A).
            data(int): La última lectura de datos en bruto.

        Returns: False si ocurrió un error.
        """
        if channel == 'A' and gain_A == 128:
            self._last_raw_data_A_128 = data
        elif channel == 'A' and gain_A == 64:
            self._last_raw_data_A_64 = data
        elif channel == 'B':
            self._last_raw_data_B = data
        else:
            return False


    def _ready(self):
        """
        _ready method check if data is prepared for reading from HX711

        Returns: bool True if ready else False when not ready        
        """
        # if DOUT pin is low data is ready for reading
        if GPIO.input(self._dout) == 0:
            return True
        else:
            return False

    def _set_channel_gain(self, num):
        """
        _set_channel_gain is called only from _read method.
        It finishes the data transmission for HX711 which sets
        the next required gain and channel.

        Args:
            num(int): how many ones it sends to HX711
                options (1 || 2 || 3)
        
        Returns: bool True if HX711 is ready for the next reading
            False if HX711 is not ready for the next reading
        """
        for _ in range(num):
            start_counter = time.perf_counter()
            GPIO.output(self._pd_sck, True)
            GPIO.output(self._pd_sck, False)
            end_counter = time.perf_counter()
            # check if hx 711 did not turn off...
            if end_counter - start_counter >= 0.00006:
                # if pd_sck pin is HIGH for 60 us and more than the HX 711 enters power down mode.
                if self._debug_mode:
                    print('Not enough fast while setting gain and channel')
                    print(
                        'Time elapsed: {}'.format(end_counter - start_counter))
                # hx711 has turned off. First few readings are inaccurate.
                # Despite it, this reading was ok and data can be used.
                result = self.get_raw_data_mean(6)  # set for the next reading.
                if result == False:
                    return False
        return True

    def _read(self):
        """
        _read method reads bits from hx711, converts to INT
        and validate the data.
        
        Returns: (bool || int) if it returns False then it is false reading.
            if it returns int then the reading was correct
        """
        GPIO.output(self._pd_sck, False)  # start by setting the pd_sck to 0
        ready_counter = 0
        while (not self._ready() and ready_counter <= 40):
            time.sleep(0.01)  # sleep for 10 ms because data is not ready
            ready_counter += 1
            if ready_counter == 50:  # if counter reached max value then return False
                if self._debug_mode:
                    print('self._read() not ready after 40 trials\n')
                return False

        # read first 24 bits of data
        data_in = 0  # 2's complement data from hx 711
        for _ in range(24):
            start_counter = time.perf_counter()
            # request next bit from hx 711
            GPIO.output(self._pd_sck, True)
            GPIO.output(self._pd_sck, False)
            end_counter = time.perf_counter()
            if end_counter - start_counter >= 0.00006:  # check if the hx 711 did not turn off...
                # if pd_sck pin is HIGH for 60 us and more than the HX 711 enters power down mode.
                if self._debug_mode:
                    print('Not enough fast while reading data')
                    print(
                        'Time elapsed: {}'.format(end_counter - start_counter))
                return False
            # Shift the bits as they come to data_in variable.
            # Left shift by one bit then bitwise OR with the new bit.
            data_in = (data_in << 1) | GPIO.input(self._dout)

        if self._wanted_channel == 'A' and self._gain_channel_A == 128:
            if not self._set_channel_gain(1):  # send only one bit which is 1
                return False  # return False because channel was not set properly
            else:
                self._current_channel = 'A'  # else set current channel variable
                self._gain_channel_A = 128  # and gain
        elif self._wanted_channel == 'A' and self._gain_channel_A == 64:
            if not self._set_channel_gain(3):  # send three ones
                return False  # return False because channel was not set properly
            else:
                self._current_channel = 'A'  # else set current channel variable
                self._gain_channel_A = 64
        else:
            if not self._set_channel_gain(2):  # send two ones
                return False  # return False because channel was not set properly
            else:
                self._current_channel = 'B'  # else set current channel variable

        if self._debug_mode:  # print 2's complement value
            print('Binary value as received: {}\n'.format(bin(data_in)))

        #check if data is valid
        if (data_in == 0x7fffff
                or  # 0x7fffff is the highest possible value from hx711
                data_in == 0x800000
           ):  # 0x800000 is the lowest possible value from hx711
            if self._debug_mode:
                print('Invalid data detected: {}\n'.format(data_in))
            return False  # return false because the data is invalid

        # calculate int from 2's complement
        signed_data = 0
        # 0b1000 0000 0000 0000 0000 0000 check if the sign bit is 1. Negative number.
        if (data_in & 0x800000):
            signed_data = -(
                (data_in ^ 0xffffff) + 1)  # convert from 2's complement to int
        else:  # else do not do anything the value is positive number
            signed_data = data_in

        if self._debug_mode:
            print('Converted 2\'s complement value: {}\n'.format(signed_data))

        return signed_data

    def get_raw_data_mean(self, readings=30):
        """
        get_raw_data_mean devuelve el valor medio de las lecturas.

        Args:
            readings(int): Número de lecturas para el promedio.

        Returns: (bool || int) si es False, entonces la lectura es inválida.
            si devuelve un int, la lectura es válida.
        """
        # Realizar una copia de respaldo del canal y ganancia actuales antes de las lecturas para su uso posterior
        backup_channel = self._current_channel
        backup_gain = self._gain_channel_A
        data_list = []
        
        # Realizar el número requerido de lecturas
        for _ in range(readings):
            data_list.append(self._read())
        
        data_mean = False
        if readings > 2 and self._data_filter:
            # Aplicar el filtro de datos para eliminar valores atípicos
            filtered_data = self._data_filter(data_list)
            if self._debug_mode:
                print('Lista de datos: {}'.format(data_list))
                print('Lista de datos filtrados: {}'.format(filtered_data))
                print('Media de datos:', stat.mean(filtered_data))
            # Calcular la media de los datos filtrados
            data_mean = stat.mean(filtered_data)
        else:
            # Calcular la media directamente de la lista de datos
            data_mean = stat.mean(data_list)
        
        # Guardar la última lectura en bruto
        self._save_last_raw_data(backup_channel, backup_gain, data_mean)
        
        return int(data_mean)


    def get_data_mean(self, readings=30):
        """
        get_data_mean devuelve el valor promedio de las lecturas menos
        el offset para el canal que se está leyendo.

        Args:
            readings(int): Número de lecturas para el promedio

        Returns: (bool || int) False si la lectura no fue correcta.
            Si devuelve un int, la lectura fue correcta.
        """
        result = self.get_raw_data_mean(readings)
        if result != False:
            if self._current_channel == 'A' and self._gain_channel_A == 128:
                return result - self._offset_A_128
            elif self._current_channel == 'A' and self._gain_channel_A == 64:
                return result - self._offset_A_64
            else:
                return result - self._offset_B
        else:
            return False

    def get_weight_mean(self, readings=30):
        """
        Obtiene el valor promedio del peso a partir de un número especificado de lecturas.
        
        Args:
            readings (int): Número de lecturas para calcular el promedio.

        Returns:
            (bool || float): Devuelve False si la lectura no fue correcta.
                            Si devuelve un float, la lectura fue correcta.
        """
        result = self.get_raw_data_mean(readings)  # Obtiene la media de las lecturas en bruto
        if result != False:
            if self._current_channel == 'A' and self._gain_channel_A == 128:
                weight = float((result - self._offset_A_128) / self._scale_ratio_A_128)
            elif self._current_channel == 'A' and self._gain_channel_A == 64:
                weight = float((result - self._offset_A_64) / self._scale_ratio_A_64)
            else:
                weight = float((result - self._offset_B) / self._scale_ratio_B)

            # Ajustar el peso de la plataforma
            #adjusted_weight = weight - self._platform_weight

            # Aplicar el redondeo personalizado
            return self._custom_round(weight, self._rounding_threshold)
        else:
            return False


    def get_current_channel(self):
        """
        get current channel returns the value of current channel.

        Returns: ('A' || 'B')
        """
        return self._current_channel

    def get_data_filter(self):
        """
        get data filter.

        Returns: self._data_filter
        """
        return self._data_filter

    def get_current_gain_A(self):
        """
        get current gain A returns the value of current gain on channel A

        Returns: (128 || 64) current gain on channel A
        """
        return self._gain_channel_A

    def get_last_raw_data(self, channel='', gain_A=0):
        """
        get last raw data returns the last read data for a
        channel and gain. By default for current one.

        Args:
            channel(str): select channel ('A' || 'B'). If not then it returns the current one.
            gain_A(int): select gain (128 || 64). If not then it returns the current one.
        
        Raises:
            ValueError: if channel is not ('A' || 'B' || '') or gain_A is not (128 || 64 || 0)
                '' and 0 is default value.

        Returns: int the last data that was received for the chosen channel and gain
        """
        channel = channel.capitalize()
        if channel == 'A' and gain_A == 128:
            return self._last_raw_data_A_128
        elif channel == 'A' and gain_A == 64:
            return self._last_raw_data_A_64
        elif channel == 'B':
            return self._last_raw_data_B
        elif channel == '':
            if self._current_channel == 'A' and self._gain_channel_A == 128:
                return self._last_raw_data_A_128
            elif self._current_channel == 'A' and self._gain_channel_A == 64:
                return self._last_raw_data_A_64
            else:
                return self._last_raw_data_B
        else:
            raise ValueError(
                'Parameter "channel" has to be "A" or "B". '
                'Received: {} \nParameter "gain_A" has to be 128 or 64. Received {}'
                .format(channel, gain_A))

    def get_current_offset(self, channel='', gain_A=0):
        """
        get current offset returns the current offset for
        a particular channel and gain. By default the current one.

        Args:
            channel(str): select for which channel ('A' || 'B')
            gain_A(int): select for which gain (128 || 64)
        
        Raises:
            ValueError: if channel is not ('A' || 'B' || '') or gain_A is not (128 || 64 || 0)
                '' and 0 is default value.

        Returns: int the offset for the chosen channel and gain
        """
        channel = channel.capitalize()
        if channel == 'A' and gain_A == 128:
            return self._offset_A_128
        elif channel == 'A' and gain_A == 64:
            return self._offset_A_64
        elif channel == 'B':
            return self._offset_B
        elif channel == '':
            if self._current_channel == 'A' and self._gain_channel_A == 128:
                return self._offset_A_128
            elif self._current_channel == 'A' and self._gain_channel_A == 64:
                return self._offset_A_64
            else:
                return self._offset_B
        else:
            raise ValueError(
                'Parameter "channel" has to be "A" or "B". '
                'Received: {} \nParameter "gain_A" has to be 128 or 64. Received {}'
                .format(channel, gain_A))

    def get_current_scale_ratio(self, channel='', gain_A=0):
        """
        get current scale ratio returns the current scale ratio
        for a particular channel and gain. By default
        the current one.

        Args:
            channel(str): select for which channel ('A' || 'B')
            gain_A(int): select for which gain (128 || 64)

        Returns: int the scale ratio for the chosen channel and gain
        """
        channel = channel.capitalize()
        if channel == 'A' and gain_A == 128:
            return self._scale_ratio_A_128
        elif channel == 'A' and gain_A == 64:
            return self._scale_ratio_A_64
        elif channel == 'B':
            return self._scale_ratio_B
        elif channel == '':
            if self._current_channel == 'A' and self._gain_channel_A == 128:
                return self._scale_ratio_A_128
            elif self._current_channel == 'A' and self._gain_channel_A == 64:
                return self._scale_ratio_A_64
            else:
                return self._scale_ratio_B
        else:
            raise ValueError(
                'Parameter "channel" has to be "A" or "B". '
                'Received: {} \nParameter "gain_A" has to be 128 or 64. Received {}'
                .format(channel, gain_A))

    def power_down(self):
        """
        power down method turns off the hx711.
        """
        GPIO.output(self._pd_sck, False)
        GPIO.output(self._pd_sck, True)
        time.sleep(0.01)

    def power_up(self):
        """
        power up function turns on the hx711.
        """
        GPIO.output(self._pd_sck, False)
        time.sleep(0.01)

    def reset(self):
        """
        reset method resets the hx711 and prepare it for the next reading.

        Returns: True if error encountered
        """
        self.power_down()
        self.power_up()
        result = self.get_raw_data_mean(6)
        if result:
            return False
        else:
            return True


def outliers_filter(data_list):
    """
    It filters out outliers from the provided list of int.
    Median is used as an estimator of outliers.

    Args:
        data_list([int]): List of int. It can contain Bool False that is removed.
    
    Returns: list of filtered data. Excluding outliers.
    """
    data = []
    for num in data_list:
        if num:
            data.append(num)
    # set 'm' to lower value to remove more outliers
    # set 'm' to higher value to keep more data samples (also some outliers)
    m = 2.0
    # It calculates the absolute distance to the median.
    # Then it scales the distances by their median value (again)
    # so they are on a relative scale to 'm'.
    data_median = stat.median(data)
    abs_distance = []
    for num in data:
        abs_distance.append(abs(num - data_median))
    mdev = stat.median(abs_distance)
    s = []
    if mdev:
        for num in abs_distance:
            s.append(num / mdev)
    else:
        # mdev is 0. Therefore all data samples in the list data have the same value.
        return data
    filtered_data = []
    for i in range(len(data)):
        if s[i] < m:
            filtered_data.append(data[i])
    return filtered_data
