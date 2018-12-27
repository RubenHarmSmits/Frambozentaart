from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division  # ''


import time  # import the time library for the sleep function
# import brickpi3  # import the BrickPi3 drivers
from Touch_Sensor import Touch_sensor_class
from IR_Sensor import IR_sensor_class
from Engine import Engine
from Color_Sensor import Color_sensor_class 


class Memphis_de_pi:

    def __init__(self):
        self.my_Touch_Sensor_Front = Touch_sensor_class(1)
        self.my_Touch_Sensor_Wip = Touch_sensor_class(2)
        self.my_IR_Sensor = IR_sensor_class()
        self.engine_Left = Engine(1)
        self.engine_Right = Engine(2)
        self.my_Color_Sensor = Color_sensor_class()
        self.wheel_bias = 41/40

    def move_forward(self, speed):
        print("Wheel bias %s" % self.wheel_bias)
        self.engine_Left.change_speed(self.wheel_bias * speed)
        self.engine_Right.change_speed(1/self.wheel_bias * speed)

    def move_forward_dps(self, speed):
        self.engine_Left.change_speed_dps(self.wheel_bias * speed)
        self.engine_Right.change_speed_dps(1/self.wheel_bias * speed)

    # def move_forward(self, speed):
    #     self.engine_Left.change_speed(21 / 20 * speed)
    #     self.engine_Right.change_speed(speed)

    def move_backward(self, speed):
        self.engine_Left.change_speed(21 / 20 * -speed)
        self.engine_Right.change_speed(-speed)

    def turn_right(self, speed):
        self.engine_Left.change_speed(speed)
        self.engine_Right.change_speed(-speed)

    def turn_diagonal_right(self,speed):
        self.engine_Left.change_speed(1.2 * speed)
        self.engine_Right.change_speed(speed)

    def turn_left(self, speed):
        self.engine_Left.change_speed(-speed)
        self.engine_Right.change_speed(speed)

    def turn_left_wide(self, speed1, speed2):
        self.engine_Left.change_speed(speed1)
        self.engine_Right.change_speed(speed2)

    def special_right(self):
        self.set_duration(1, self.move_backwards_dps(60))
        self.set_duration(1, self.turn_right(20))
        self.set_duration(2, self.move_forward_dps(135))
        # even stilzetten om alles goed te kunnen observeren
        self.set_duration(3, self.stop_move())
        self.my_IR_Sensor.save_signal()
        self.my_IR_Sensor.save_signal()
        self.my_IR_Sensor.save_signal()
        self.my_IR_Sensor.save_signal()

    def turn_diagonal_left(self,speed):
        self.engine_Left.change_speed(speed)
        self.engine_Right.change_speed(1.2 * speed)

    def execute_smooth_turn(self, directionLeft):
        self.set_duration(2, self.move_backwards_dps(111))
        self.set_duration(4, self.smooth_turn_right(174, directionLeft))
        # even stilzetten om alles goed te kunnen observeren
        self.set_duration(3, self.stop_move())

        
    def smooth_turn(self, speed, directionLeft):
        if directionLeft:
            self.engine_Left.change_speed_dps(0.5 * speed)
            self.engine_Right.change_speed_dps(speed)
        elif not directionLeft:
            self.engine_Left.change_speed_dps(speed)
            self.engine_Right.change_speed_dps(0.5 * speed)
            
    def move_backwards_dps(self, speed):
        self.engine_Left.change_speed_dps(-speed)
        self.engine_Right.change_speed_dps(-speed)
    
    def stop_move(self):
        self.engine_Left.change_speed(0)
        self.engine_Right.change_speed(0)

    def wip_program_execute(self):
        print("inside wip program")
        self.set_duration(3, self.move_backward(20))
        self.move_forward(20)
        while not self.my_Touch_Sensor_Wip.get_signal():
            self.keep_IR_distance(50)
        self.set_duration(0.4, self.move_forward(20))

        while not self.my_Color_Sensor.end_quadrant_check():
            self.move_forward(20)
            if self.my_Color_Sensor.get_color() == "Red":
                # self.set_duration(1, self.turn_diagonal_left(20))
                self.turn_diagonal_left(20)
                print("Turning diagonal left")
            else:
                # self.set_duration(1, self.turn_diagonal_right(20))
                self.turn_diagonal_right(20)
                print("Turning diagonal right")

        print("outside of wip loop")
        self.set_duration(4, self.move_forward(20))

    def keep_IR_distance(self, target_distance):

        print("Keep IR distance")
        if self.my_IR_Sensor.signal >= self.my_IR_Sensor.current_average and self.my_IR_Sensor.signal > (target_distance + 1):
            self.wheel_bias = self.wheel_bias + 0.01
            if self.wheel_bias > 1.1:
                self.wheel_bias = 1.1
        elif self.my_IR_Sensor.signal <= self.my_IR_Sensor.current_average and self.my_IR_Sensor.signal < (target_distance - 1):
            self.wheel_bias = self.wheel_bias - 0.01
            if self.wheel_bias < 0.95:
                self.wheel_bias = 0.95
        elif self.my_IR_Sensor.signal <= (target_distance + 1) and self.my_IR_Sensor.signal >= (target_distance - 1):
            self.wheel_bias = 41/40
        else:
            pass

    def set_duration(self, duration, function):
        t_end = time.time() + duration
        while time.time() < t_end:
            function

    def manage_move(self):
        while True:
            self.my_IR_Sensor.average_signal()
            self.check_state()

            self.keep_IR_distance(15)
            self.move()

            time.sleep(0.02)
            if self.my_Color_Sensor.end_quadrant_check() and self.my_Color_Sensor.get_color() == "Black":
                self.stop_move()

    def check_state(self):

        if self.my_IR_Sensor.current_average > 40:
            self.state = "special right"
            self.wheel_bias = 41/40
            print("Special Right")

        elif self.my_Touch_Sensor_Front.get_signal():
            self.set_duration(1,self.move_forward(20))
            self.state = "turn left"
            self.wheel_bias = 41 / 40
            print("Turning left")

        elif self.my_Touch_Sensor_Wip.get_signal():
            self.state = "Wip program"
            print("Wip Sensor is on")

        else:
            self.state = "forward"
            print("Moving forward")

    def move(self):
        if self.state == "turn left":
            if self.my_IR_Sensor.current_average > 20:
                self.set_duration(0.5, self.move_backward(20))
                self.set_duration(1, self.turn_left(17))
            elif self.my_IR_Sensor.current_average <= 20:
                print("executing smooth turn")
                self.execute_smooth_turn(True)
            self.my_IR_Sensor.new_average()
        elif self.state == "special right":
            self.special_right()
        elif self.state == "forward":
            self.move_forward(10)
        elif self.state == "Wip program":
            print("Wip! ")
            self.wip_program_execute()


memphis = Memphis_de_pi()

try:
    # memphis.move_forward(30)
    memphis.my_IR_Sensor.new_average()
    memphis.manage_move()
    # memphis.my_Color_Sensor.get_color()
except KeyboardInterrupt:
    memphis.stop_move()


