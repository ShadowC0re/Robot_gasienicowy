from statistics import mode
from typing_extensions import Self
from Raspi_MotorHAT import Raspi_MototrHat
from gpiozero import DistanceSensor
import atexit
class Robot : 
    #sterowanie  silnikiem i predkoscia
    def _init_(self, motorhat_addr=0x6f):

        #inicjalizacja nakladki sterowania {
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)
        #}

        #ustawienie zmiennych lokalnych dal silnika lewego i prawego{
        self.left_motor = self._mh.getMotor(1)
        self.right_motor = self._mh.getMotor(2)
        #}

        #zatrzymanie silnikow po zatrzymaniu programu{
        atexit.register(self.stop_motors)
        #}    

        # wybor kierunku jazdy oraz skalowanie predkosci{
    def convert_speed(self, speed):
        mode = Raspi_MototrHat.Release #zatrzymany silnik
        #wybor kierunku jazdy
        if speed > 0:
            mode = Raspi_MototrHat.FORWARD
        elif speed < 0 :
            mode = Raspi_MototrHat.BACKWARD
        #}

        #skalowanie predkosci {
        output_speed = (abs(speed)*255)//100
        return mode, int(output_speed)
        #}
        #     
        #}

        #przypisanie predkosci oraz kieruku jazdy do lewego silnika{
    def set_left(self, speed):
        mode , output_speed=self.convert_speed(speed)
        self.left_motor.setSpeed(output_speed)
        self.left_motor.run(mode)    
        # }

        #przypisanie predkosci oraz kieruku jazdy do prawego silnika{
    def set_left(self, speed):
        mode , output_speed=self.convert_speed(speed)
        self.right_motor.setSpeed(output_speed)
        self.right_motor.run(mode)    
        # }

        #wylaczenie silnikow{
    def stop_motors(self):
        self.left_motor.run(Raspi_MototrHat.Release)
        self.right_motor.run(Raspi_MototrHat.Release)
        #}

    #czujniki odleglosci 
        self.left_distance_sensor = DistanceSensor(echo=17, trigger=27, queue_len=2)
        self.right_distance_sensor =DistanceSensor( echo=5, trigger=6, queue_len=2)    
    
    #Wylacz wszystko po zakonczeniu programu
        atexit.register(self.stop_all)