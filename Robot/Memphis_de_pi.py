from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division  # ''

import sys
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
        self.wheel_bias = 1.05
        self.disable_wip = False
        self.standard_speed = 20
        self.isInSecondQuadrant = False

    def move_forward(self, speed):
        # print("Wheel bias %s" % self.wheel_bias)
        self.engine_Left.change_speed(self.wheel_bias * speed)
        self.engine_Right.change_speed(1/self.wheel_bias * speed)

    def move_forward_dps(self, speed, bias):
        self.wheel_bias = bias
        self.engine_Left.change_speed_dps(self.wheel_bias * speed)
        self.engine_Right.change_speed_dps(1/self.wheel_bias * speed)
        self.wheel_bias = 1.05

    # def move_forward(self, speed):
    #     self.engine_Left.change_speed(21 / 20 * speed)
    #     self.engine_Right.change_speed(speed)

    def move_backward(self, speed):
        self.engine_Left.change_speed(1.05 * -speed)
        self.engine_Right.change_speed(-speed)

    def move_backwards_dps(self, speed):
        self.engine_Left.change_speed_dps(1.05 * -speed)
        self.engine_Right.change_speed_dps(-speed)

    # def turn_right1(self, speed):
    #     self.engine_Left.change_speed_dps(0)
    #     self.engine_Right.change_speed_dps(-speed)

    def turn_right2(self, speed):
        self.engine_Left.change_speed_dps(speed)
        self.engine_Right.change_speed_dps(0)

    def turn_diagonal_right(self, speed):
        self.engine_Left.change_speed(1.4 * speed)
        self.engine_Right.change_speed(speed)

    def move_onto_bridge(self, speed):
        self.engine_Left.change_speed(1.9 * speed)
        self.engine_Right.change_speed(speed)

    def turn_left(self, speed):
        self.engine_Left.change_speed_dps(-speed)
        self.engine_Right.change_speed_dps(speed)

    def standard_move(self, speed1, speed2):
        self.engine_Left.change_speed_dps(speed1)
        self.engine_Right.change_speed_dps(speed2)

    def special_right(self):
        # even stilzetten om alles goed te kunnen observeren
        self.set_duration(1, self.stop_move())
        self.set_duration(1.5, self.move_backwards_dps(95))
        self.set_duration(1, self.turn_right2(345))
        # even stilzetten om alles goed te kunnen observeren
        self.set_duration(1, self.stop_move())
        self.set_duration(2, self.move_forward_dps(270, 0.98))
        # even stilzetten om alles goed te kunnen observeren
        self.set_duration(1, self.stop_move())
        self.my_IR_Sensor.new_average()

    def turn_diagonal_left(self,speed):
        self.engine_Left.change_speed(speed)
        self.engine_Right.change_speed(speed)

    def execute_smooth_turn(self, directionLeft):
        self.set_duration(2, self.standard_move(-222, -200))
        self.set_duration(3.5, self.smooth_turn(170, directionLeft))
        # even stilzetten om alles goed te kunnen observeren
        self.set_duration(1, self.stop_move())

    def turn_left_second_quadrant(self, directionLeft):
        self.set_duration(4.6, self.move_backwards_dps(207))
        self.set_duration(7.5, self.smooth_turn_second_quadrant(170, directionLeft))
        # even stilzetten om alles goed te kunnen observeren
        self.set_duration(1, self.stop_move())

    def smooth_turn(self, speed, directionLeft):
        if directionLeft:
            self.engine_Left.change_speed_dps(0.5 * speed)
            self.engine_Right.change_speed_dps(speed)
        elif not directionLeft:
            self.engine_Left.change_speed_dps(speed)
            self.engine_Right.change_speed_dps(0.5 * speed)

    def smooth_turn_second_quadrant(self, speed, directionLeft):
        if directionLeft:
            self.engine_Left.change_speed_dps(0.80 * speed)
            self.engine_Right.change_speed_dps(speed)
        elif not directionLeft:
            self.engine_Left.change_speed_dps(speed)
            self.engine_Right.change_speed_dps(0.80 * speed)

    def stop_move(self):
        self.engine_Left.change_speed(0)
        self.engine_Right.change_speed(0)

    def wip_program_execute(self):
        print("inside wip program")
        # self.set_duration(3, self.move_backward(20))
        #self.set_duration(1.5, self.move_onto_bridge(25))
        self.set_duration(1, self.move_forward(25))
        self.set_duration(0.2, self.move_forward(60))
        self.stop_move()
        # while not self.my_Touch_Sensor_Wip.get_signal():
        #     self.keep_IR_distance(50)
        # self.set_duration(0.4, self.move_forward(20))

        while not self.my_Touch_Sensor_Front.get_signal():
            if self.my_Color_Sensor.get_color() == "Red" or self.my_Color_Sensor.get_color() == "Brown":
                # self.set_duration(1, self.turn_diagonal_left(20))
                self.set_duration(0.5, self.turn_left(30))
                self.set_duration(0.2, self.move_forward(20))
                print("Turning diagonal left")
            else:
                # self.set_duration(1, self.turn_diagonal_right(20))
                self.turn_diagonal_right(20)
                print("Turning diagonal right")

        print("outside of wip loop")
        self.stop_move()
        self.execute_smooth_turn(True)
        self.disable_wip = True
        self.isInSecondQuadrant = False

    def keep_IR_distance(self, target_distance):
        # print("Keep IR distance")
        if self.my_IR_Sensor.signal >= self.my_IR_Sensor.current_average and self.my_IR_Sensor.signal > (target_distance + 1):
            self.wheel_bias = self.wheel_bias + 0.01
            if self.wheel_bias > 1.1:
                self.wheel_bias = 1.1
        elif self.my_IR_Sensor.signal <= self.my_IR_Sensor.current_average and self.my_IR_Sensor.signal < (target_distance - 1):
            self.wheel_bias = self.wheel_bias - 0.01
            if self.wheel_bias < 0.95:
                self.wheel_bias = 0.95
        elif self.my_IR_Sensor.signal <= (target_distance + 1) and self.my_IR_Sensor.signal >= (target_distance - 1):
            self.wheel_bias = 1.05
        else:
            pass

    def set_duration(self, duration, function):
        t_end = time.time() + duration
        while time.time() < t_end:
            function

    def manage_move(self):
        while True:
            self.my_IR_Sensor.average_signal()
            print("In second quadrant %s:" % self.isInSecondQuadrant)
            self.check_state()
            if self.my_Color_Sensor.get_color() == "Black":
                self.standard_speed = self.standard_speed + 1
            elif self.my_Color_Sensor.get_color() == "Blue":
                self.standard_speed = 20
            if self.my_Color_Sensor.end_quadrant_check() and not self.isInSecondQuadrant and not self.disable_wip:
                self.isInSecondQuadrant = True

            self.move()

            time.sleep(0.02)

            # if self.my_Color_Sensor.end_parcours() and self.my_Touch_Sensor_Front.get_signal():
            #     self.stop_move()
            #     print("Stopped")
            #     break
            # else:
            #     pass

    def check_state(self):
        if self.my_IR_Sensor.current_average > 40 and not self.isInSecondQuadrant:
            self.state = "special right"
            print("Special Right")

        elif self.my_Touch_Sensor_Front.get_signal():
            if self.my_Color_Sensor.end_quadrant_check() and not self.isInSecondQuadrant:
                self.state = "end of the parcours"
            else:
                self.set_duration(1,self.move_forward_dps(180, 1.05))
                self.state = "turn left"
                print("Turning left")

        elif self.my_Touch_Sensor_Wip.get_signal() and not self.disable_wip:
            self.state = "Wip program"
            print("Wip Sensor is on")

        else:
            self.state = "forward"

    def move(self):
        if self.state == "turn left" and not self.isInSecondQuadrant:
            if self.my_IR_Sensor.current_average > 20:
                self.set_duration(0.5, self.move_backward(20))
                self.set_duration(1, self.turn_left(174))
            elif self.my_IR_Sensor.current_average <= 20:
                print("executing smooth turn")
                self.execute_smooth_turn(True)
            self.my_IR_Sensor.new_average()
        elif self.state == "turn left" and self.isInSecondQuadrant:
            # self.keep_IR_distance(15)
            if self.my_IR_Sensor.current_average > 20:
                self.set_duration(1.5, self.move_backward(15))
                self.set_duration(1, self.turn_left(174))
            elif self.my_IR_Sensor.current_average <= 20:
                self.turn_left_second_quadrant(True)
                self.isInSecondQuadrant = False
        elif self.state == "special right":
            self.special_right()
        elif self.state == "forward":
            self.move_forward(self.standard_speed)
        elif self.state == "Wip program":
            print("Wip! ")
            self.wip_program_execute()
        elif self.state == "end of the parcours":

            self.set_duration(1, self.move_forward(self.standard_speed))
            if self.my_Color_Sensor() == "Black":
                print("STOPPED")
                sys.exit()


memphis = Memphis_de_pi()

try:
    # while True:
    #     memphis.my_Color_Sensor.get_color()
    # memphis.move_forward(40)
    # memphis.my_IR_Sensor.new_average()
    # print(memphis.my_IR_Sensor.signal)
    memphis.my_IR_Sensor.update_signal()
    memphis.manage_move()

except KeyboardInterrupt:
    memphis.stop_move()


