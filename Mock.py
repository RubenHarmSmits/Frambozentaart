import brickpi3


class Mock:

    def __init__(self, aValueTouch1, aValueTouch2, aValueIR, aValueColour  ):
        bp_test = brickpi3.BrickPi3()
        bp_test.valueTouch1 = aValueTouch1
        bp_test.valueTouch2 = aValueTouch2
        bp_test.ValueIR = aValueIR
        bp_test.ValueColour = aValueColour

    def __init__(self, aValueTouch1):
        bp_test = brickpi3.BrickPi3()
        bp_test.valueTouch1 = aValueTouch1



if __name__ == '__main__':
    Mock.main()

