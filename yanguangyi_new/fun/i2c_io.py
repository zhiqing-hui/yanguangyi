




import smbus
# from log import debug, log


class I2C_IO:
    # i2c_index:  the i2c chip index ,
    #    using '$ sudo i2cdetect -l' to check how many i2c chip
    # i2c_addr: the device address, e.g. 0x20, 0x23 , etc.
    #    usging '$ sudo i2cdetect -1' to check how many devices at chip 1
    def __init__(self, i2c_index, i2c_addr):
        self.index= i2c_index
        self.addr = i2c_addr
        self.bus = smbus.SMBus(i2c_index)

    # pin: pin number,  from 0~7
    # value: 0/1 or False/True or LOW/HIGH
    #  only modify the bit according to the pin
    def output(self, pin, value):
        data = self.bus.read_byte( self.addr )
        if value == 1:
            value = (1 << pin) | data
        else:
            value = (~(1 << pin)) & data
        # debug("I2C_IO::output(): old:%s,  new: %s  to pin %s" % (bin(data), bin(value),pin) )
        return self.bus.write_byte( self.addr, value)

    # pin: pin number,  from 0~7
    # return:
    #     the state of the pin, HIGH or LOW
    #     only return the bit according to the pin
    # def input(self, pin):
    #     data = self.read_byte(self.addr)
    #     mask = i<<pin
    #     if mask & data == mask:
    #         return 1
    #     else:
    #         return 0

    def setup(self, pin, direction):
        pass