import os


class GPIO_PWM():
    def __init__(self, _gpio_pins, _is_inverted=False):        
        cmd = 'sudo ' + os.path.dirname(__file__)  + '/PiBits/ServoBlaster/user/servod --cycle-time=2550 --min=0 --max=255'

        if _is_inverted:
            cmd += ' --invert'

        cmd += ' > /dev/null'

        os.system(cmd)

        self._servo_pins = { 4:0, 17:1, 18:2, 21:3, 27:3, 22:4, 23:5, 24:6, 25:7 }

        for _pin in _gpio_pins:
            os.system('echo ' + str(self._servo_pins[_pin]) + '=0% > /dev/servoblaster')



        

    def write(self,_pin,_pwm):
        os.system('sudo echo ' + str(self._servo_pins[_pin])  + '=' + str(_pwm)  + ' > /dev/servoblaster')


