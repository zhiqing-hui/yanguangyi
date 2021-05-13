import i2c_io
import RPi.GPIO as GPIO
# from log import debug, log


class G_IO:
        # GPIO_mode:  GPIO_BCM or GPIO_BOARD
        # i2c_index:  the i2c chip index ,
        #    using '$ sudo i2cdetect -l' to check how many i2c chip
        # i2c_addr: the device address, e.g. 0x20, 0x23 , etc.
        #    usging '$ sudo i2cdetect -1' to check how many devices at chip 1
        def __init__(self, GPIO_mode=None, i2c_index=None, i2c_addr=None):
                if i2c_index != None and i2c_addr != None:
                        self.i2c_io = i2c_io.I2C_IO( i2c_index, i2c_addr)
                if GPIO_mode != None:
                        GPIO.setmode(GPIO_mode)

        # using the 'port' parameter to determin whether it is a GPIO port
        def _is_GPIO(self, port):
                # it is the GPIO port when its type is int
                if type(port) == type(1):
                        return True
                elif type(port) == type("str"):
                        # it is the GPIO port when it can be translate to int,
                        #  because the i2c io start with 'I'
                        try:
                                int(port)
                                return True
                        except ValueError:
                                return False
                else:
                        # error( "G_IO::_is_GPIO():Error! the type of 'port' should be str or int. now is %s. " % port)
                        return None

        # get the port value from a port string like 'I2', 'I7'
        def get_port_value(self, port):
                return int( port[1:] )


        # setup the io direction, only effect to GPIO io
        def setup(self, port, direction ):
                #debug("G_IO::setup(): set direciton %d for port %s" % (direction,port) )
                if self._is_GPIO(port):
                        GPIO.setup(port, direction)
                else:
                        self.i2c_io.setup(port, direction)

        # output to the port
        # the value only suport the HIGH or LOW
        def output(self, port, value):
                # debug("G_IO::output(): set output value %d for port %s" % (value,port) )
                if self._is_GPIO(port):
                        GPIO.output(port, value)
                else:
                        port = self.get_port_value(port)
                        self.i2c_io.output(port,value)

        # input from a port
        def input(self, port):
                # debug("G_IO::output(): get input value from port %s" % (port) )
                if self._is_GPIO(port):
                        return GPIO.input(port)
                else:
                        port = self.get_port_value(port)
                        return self.i2c_io.input(port)