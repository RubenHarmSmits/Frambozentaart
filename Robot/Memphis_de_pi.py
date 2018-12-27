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

    def move_forward(self, speed):
        self.engine_Left.change_speed(21 / 20 * speed)
        self.engine_Right.change_speed(speed)

    def move_backward(self, speed):
        self.engine_Left.change_speed(21 / 20 * -speed)
        self.engine_Right.change_speed(-speed)

    def turn_right(self, speed):
        self.engine_Left.change_speed(speed)
        self.engine_Right.change_speed(-speed)

    def turn_diagonal_right(self,speed):
        self.engine_Left.change_speed(1.2* speed)
        self.engine_Right.change_speed(speed)

    def turn_left(self, speed):
        self.engine_Left.change_speed(-speed)
        self.engine_Right.change_speed(speed)

    def turn_left_wide(self, speed1, speed2):
        self.engine_Left.change_speed(speed1)
        self.engine_Right.change_speed(speed2)

    def special_right(self):
        self.set_duration(0.5, self.move_backward(10))
        self.set_duration(1, self.turn_right(20))
        self.set_duration(2, self.move_forward(30))
        self.my_IR_Sensor.save_signal()
        self.my_IR_Sensor.save_signal()
        self.my_IR_Sensor.save_signal()
        self.my_IR_Sensor.save_signal()

    def turn_diagonal_left(self,speed):
        self.engine_Left.change_speed(speed)
        self.engine_Right.change_speed(1.2 *speed)

    def stop_move(self):
        self.engine_Left.change_speed(0)
        self.engine_Right.change_speed(0)

    def wip_program_prepare(self):
        print("inside wip program")
        self.set_duration(0.4, self.move_forward(20))
        # self.my_Color_Sensor.set_color_state()
        # print(self.my_Color_Sensor.color_state)

        while self.my_Color_Sensor.get_color() != "Black":
            self.my_IR_Sensor.signal == 0
            self.move_forward(20)
            if self.my_Color_Sensor.get_color() == "Red":
                # self.set_duration(1, self.turn_diagonal_left(20))
                self.turn_diagonal_left(20)
                print("Turning diagonal left")
            else:
                # self.set_duration(1, self.turn_diagonal_right(20))
                self.turn_diagonal_right(20)
                print("Turning diagonal right")
            # self.my_Color_Sensor.get_color_pattern()
            # print(self.my_Color_Sensor.color_state)
            # print("end of wip loop")
        print("outside of wip loop")
        self.set_duration(4, self.move_forward(20))

    #     time.sleep(1.5)
    #     self.adjust_right()
    #     time.sleep(1.5)
    #     self.set_duration(3,self.move_backward(30))
    #     time.sleep(1.5)
    #     self.adjust_left()
    #     time.sleep(1.5)
    #     while not self.my_Touch_Sensor_Wip.get_signal():
    #         self.move_forward(50)
    #     self.wip_program_execute()
    #
    # def wip_program_execute(self):
    #     while not self.my_Touch_Sensor_Wip.get_signal():
    #         if self.my_Color_Sensor.get_color() == "Red":
    #             self.set_duration(1,self.turn_diagonal_left(20))
    #         else:
    #             self.set_duration(1, self.turn_diagonal_right(20))
    #
    # def adjust_right(self):
    #     self.set_duration(0.5, self.turn_right(30))
    #
    # def adjust_left(self):
    #     self.set_duration(0.5, self.turn_left(30))
    #

    def set_duration(self, duration, function):
        t_end = time.time() + duration
        while time.time() < t_end:
            function

    def manage_move(self):
        while True:
            self.my_IR_Sensor.average_signal()
            self.check_state()


            self.move()

            time.sleep(0.02)

    def check_state(self):

        if self.my_IR_Sensor.current_average > 40:
            self.state = "special right"
            print("Special Right")

        elif self.my_Touch_Sensor_Front.get_signal():
            self.state = "turn left"
            print("Turning left")

        elif self.my_Touch_Sensor_Wip.get_signal():
            self.state = "Wip program"
            print("Wip Sensor is on")

        else:
            self.state = "forward"
            print("Moving forward")


    # def check_state(self):
    #
    #     # if self.my_Touch_Sensor_Wip.get_signal():
    #     #     self.state = "Wip program"
    #     if self.my_Touch_Sensor_Front.get_signal() and not self.my_IR_Sensor.average_IR_to_far():
    #         self.state = "turn left"
    #         print("Turning left")
    #     # elif not self.my_IR_Sensor.isTooClose():
    #     #     self.state = "turn right"
    #     #     print("Turning right")
    #     elif self.my_IR_Sensor.average_IR_to_far():
    #         self.state = "special right"
    #         print("Special Right")
    #     elif not self.my_Touch_Sensor_Front.get_signal():
    #         self.state = "forward"
    #         print("Moving forward")

    def move(self):
        if self.state == "turn left":
            if self.my_IR_Sensor.current_average > 20:
                self.set_duration(0.5, self.move_backward(20))
                self.set_duration(1, self.turn_left(17))
            elif self.my_IR_Sensor.current_average <= 20:
                self.set_duration(2, self.move_backward(20))
                self.set_duration(2, self.turn_left_wide(5, 20))
                self.my_IR_Sensor.save_signal()
                self.my_IR_Sensor.save_signal()
                self.my_IR_Sensor.save_signal()
                self.my_IR_Sensor.save_signal()
        elif self.state == "special right":
            self.special_right()
        elif self.state == "forward":
            self.move_forward(40)
        elif self.state == "Wip program":
            print("IT WORKS")
            self.wip_program_prepare()


memphis = Memphis_de_pi()

try:
    # memphis.move_forward(0)
    memphis.manage_move()
    # memphis.my_Color_Sensor.get_color()
except KeyboardInterrupt:
    memphis.stop_move()









    # def drive_straight(self):
    #
    #     r_wheel = 31  # mm
    #     revolutions = get_motor_encoder/ 360   # output motor
    #     dist_travelled = revolutions*2*math.pi()*r_wheel
    #
    #     # misschien het dist_diff pas bij >20mm laten triggeren, anders blijft ie corrigeren
    #
    #     dist1 = 15  # arbitrary value
    #     dist2 = 5  # arbitrary value
    #     dist_diff = dist1 - dist2
    #
    #     alpha = math.degrees(math.atan(dist_diff/dist_travelled))
    #     correction_angle = 15  # degrees
    #     gamma = alpha + correction_angle
    #
    #     correct_distance = 50  # mm
    #     correct_slanted_distance = (correct_distance / math.degrees(math.cos(correction_angle)))
