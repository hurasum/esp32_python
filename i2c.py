"""
I2C typing class

This class includes full support for using ESP32 I2C peripheral
Both master and slave modes are supported.
Master and slave modes can be used at the same time, on different I2C interfaces.

"""

class I2C:
    def init(self, **args):
        """
        Reinitialize an existing I2C object.
        The arguments are the same as for creating a new i2c instance object.

        """
        pass

    def deinit(self):
        """
        Deinitialize the I2C object, free all used resources.

        """
        pass

    def scan(self):
        """
        Scan for i2c devices on I2C bus. Does not scan reserved 7-bit addresses: 0x00-0x07 & 0x78-0x7F
        Returns the list of detected addresses.
        Can only be used in master mode.

        """
        pass

    def is_ready(self, addr):
        """
        Check if i2c device with address addr is present on i2c bus
        Returns True if the device was detected, `False if not.
        Can only be used in master mode.

        į2c.readfrom(addr, nbytes)

        Read nbytes bytes from i2c device with address addr.
        Bytearray of read bytes is returned.
        Can only be used in master mode.

        į2c.readfrom_into(addr, buf)

        Read from i2c device with address addr into buffer object buf.
        Size of buf bytes are read.
        Can only be used in master mode.

        """
        pass

    def writeto(self, addr, buf, stop=True):
        """
        Write the content of the buffer object buf to the i2c device with address adr
        If optional stop argument is set to False, the stop signal is not issued.
        Can only be used in master mode.

        į2c.readfrom_mem(addr, memaddr, n, adrlen, stop)
        Argument 	Description
        addr 	i2c device address
        memaddr 	memory address to be wtitten before read
        n 	number of bytes to read
        adrlen 	optional; number of addres bytes to write, 1 - 4
        If not given, number of bytes to send is determined from the memaddr value
        stop 	optional; Default: True
        If True, stop signal is issued after address write. Two i2c transactions are actually used, one for writing the address and one for reading the data
        If False, repeated start signal is issued after address write, the operation is performed in one i2c transaction

        Write the address to the i2c device with address addr, then read n bytes from it.
        Bytearray of read bytes is returned.
        Can only be used in master mode.

        į2c.readfrom_mem_into(addr, memaddr, buf, adrlen, stop)
        Argument 	Description
        addr 	i2c device address
        memaddr 	memory address to be wtitten before read
        buf 	Buffer object to read into
        adrlen 	optional; number of addres bytes to write, 1 - 4
        If not given, number of bytes to send is determined from the memaddr value
        stop 	optional; Default: True
        If True, stop signal is issued after address write. Two i2c transactions are actually used, one for writing the address and one for reading the data
        If False, repeated start signal is issued after address write, the operation is performed in one i2c transaction

        Write the address to the i2c device with address addr, then read from itinto buffer object buf.
        Size of buf bytes are read.
        Can only be used in master mode.

        """
        pass

    def writeto_mem(self, addr, memaddr, buf, adrlen):
        """    Argument 	Description
        addr 	i2c device address
        memaddr 	memory address to be wtitten before read
        buf 	Buffer object to write from
        adrlen 	optional; number of addres bytes to write, 1 - 4
        If not given, number of bytes to send is determined from the memaddr value

        Write the address to the i2c device with address addr, then write the content of the buffer object buf to the device
        Can only be used in master mode.

        SLAVE mode

        The I2C device can be configured to run in slave mode.

        In slave mode i2c device with 128-4096 memory is emulated, via the slave buffer. All master's read/write requests for data are handled by the driver's interrupt routine. The user only needs to provide the initial buffer content and, optionally, to handle the master's request from callbacks.

        Master can read from or write to the ESP32 i2c device, providing the memory (slave buffer) address to read from or write to.

        For buffer sizes 128-256 bytes, 8-bit addressing is used, for buffer sizes >256 bytes, 16-bit addressing is used.

        Typical master write sequence is as follows:

        For slave buffer size <= 256 8-bit addressing is used

        _____________________________________________________________________________________
        | start | slave_addr + wr_bit + ack | buff_addr + ack | write n bytes + ack  | stop |
        --------|---------------------------|-----------------|----------------------|------|

        For slave buffer size > 256 16-bit addressing is used

        _____________________________________________________________________________________________________________
        | start | slave_addr + wr_bit + ack | buff_addr_hi + ack | buff_addr_lo + ack | write n bytes + ack  | stop |
        --------|---------------------------|--------------------|--------------------|----------------------|------|

        Typical master read sequence is as follows:

        For slave buffer size <= 256 8-bit addressing is used

        _________________________________________________________________________________________________________________________________________________
        | start | slave_addr + wr_bit + ack | buff_addr + ack | start | slave_addr + rd_bit + ack | read n-1 bytes + ack | read n-th byte + nack | stop |
        --------|---------------------------|-----------------|-------|---------------------------|----------------------|-----------------------|------|

        For slave buffer size > 256 16-bit addressing is used

        _________________________________________________________________________________________________________________________________________________________________________
        | start | slave_addr + wr_bit + ack | buff_addr_hi + ack | buff_addr_lo + ack | start | slave_addr + rd_bit + ack | read n-1 bytes + ack | read n-th byte + nack | stop |
        --------|---------------------------|--------------------|--------------------|-------|---------------------------|---------  -----------|-----------------------|------|

        Optional read only area at the end of the slave buffer can be set. Master can only read from that area, writing to it by the master will be ignored.

        If slave_busy is set to True when the slave i2c object is initialized, the last byte of the slave buffer will be used as status byte.
        Bit #7 of the status byte will be set to 1 by the driver when master sends some data, indicating the slave is busy processing the request.
        Master should read the status register to detect when the slave has precessed the request.
        The application (callback function) should reset the busy bit after processing the request using resetbusy() function.
        Bits 0-6 of the status register can be used as user defined flags.

        The functions to read and write data from/to the slave buffer at any time are provided: setdata() and getdata().

        A callbacks are provided which receives notifications from the i2c driver about the slave events: address set, data sent to master, data received from master. Slave buffer address, number of bytes sent or received and overflow status are available to the slave callback to take some action on slave events.

        It is up to the user to organize the slave buffer in a way most appropriate for the application. Writting to some addresses can, for example, be treated by the slave as commands with optional arguments and some action taken.

        Read only area can contain the slave ID, revision number, sensor data etc.



        """
        pass

    def setdata(buf, addr):
        """
        Set the content of the slave buffer at address addr from buffer object buf
        Can only be used in slave mode.
        Returns True on success, False if failed.

        """
        pass

    def getdata(self, addr, length):
        """
        Get the length bytes from the slave buffer at address addr
        Bytearray of read bytes is returned.
        Can only be used in slave mode.

        """
        pass

    def resetbusy(self):
        """
        Reset the busy bit of the status byte (if used)
        Can only be used in slave mode.

        """
        pass

    def callback(self, func, type):
        """
        Register the callback function for slave events.

        The type argument can be:

            machine.I2C.CBTYPE_NONE no callback enabled
            machine.I2C.CBTYPE_ADDR execute callback when master sets the slave buffer address
            machine.I2C.CBTYPE_RXDATA execute callback when master reads data from slave buffer
            machine.I2C.CBTYPE_TXDATA execute callback when master writes data to slave buffer

        Multiple callback types can or-ed together.

        The callback functions receives the 5-item tupple argument:
        (cb_type, address, length, overflow, data)
        cb_type the callback type
        address the address in the slave buffer
        length number of bytes read or written by master
        overflow number of bytes master has atempted to read or write past the slave buffer size
        data bytearray with data sent or received to/from master

        Can only be used in slave mode.

        Example:

        import machine

        def i2c_cb(res):
            cbtype = res[0] # i2c slave cllback type
            if cbtype == machine.I2C.CBTYPE_TXDATA:
                print("[I2C] Data sent to master: addr={}, len={}, ovf={}, data={}".format(res[1], res[2], res[3], res[4]))
            elif cbtype == machine.I2C.CBTYPE_RXDATA:
                print("[I2C] Data received from master: addr={}, len={}, ovf={}, data: [{}]".format(res[1], res[2], res[3], res[4]))
            elif cbtype == machine.I2C.CBTYPE_ADDR:
                print("[I2C] Addres set: addr={}".format(res[1]))
            else:
                print("Unknown CB type, received: {}".format(res))

        # Create two i2c instance objects, master and slave
        m = machine.I2C(0, sda=21, scl=22, speed=400000)
        # no buffer length is specified, default 256 bytes buffer will be used
        # with 8-bit addressing
        s = machine.I2C(1, mode=machine.I2C.SLAVE, sda=25, scl=26)

        # Enable all slave callbacks
        s.callback(i2c_cb, s.CBTYPE_ADDR | s.CBTYPE_RXDATA | s.CBTYPE_TXDATA)

        #Set some data in slave buffer
        s.setdata("1234567890abcdefghij", 0)
        s.setdata("ABCDEFGHabcdefgh", 0x80)
        s.setdata("BUFFEREND", 0xF7)

        # >>> m
        I2C (Port=0, Mode=MASTER, Speed=400000 Hz, sda=21, scl=22)
        # >>> s
        I2C (Port=1, Mode=SLAVE, Speed=100000 Hz, sda=25, scl=26, addr=32, buffer=256 B, read-only=0 B)
             Callback=True (7)
             I2C task minimum free stack: 320
        # >>>

        # Master: scan the I2C bus
        # >>> m.scan()
        [32]
        # >>> [I2C] Addres set: addr=0
        # >>>
        # Check if devide 32 is ready
        # >>> m.is_ready(32)
        True
        # >>>
        # Master: write 14 bytes message to the slave at address 40
        #         8-bit addressing is used
        # >>> m.writeto_mem(32, 40, "Hi from master")
        14
        # >>> [I2C] Data received from master: addr=40, len=14, ovf=0, data: [b'Hi from master']

        # Master: read 10 bytes from the slave at address 0 in single transaction
        # >>> m.readfrom_mem(32, 0x00, 10, stop=False)
        b'1234567890'
        # >>> [I2C] Data sent to master: addr=0, len=10, ovf=0, data=b'1234567890'

        # Master: read 16 bytes from the slave at address 0x80
        # >>> m.readfrom_mem(32, 0x80, 16)
        b'ABCDEFGHabcdefgh'
        # >>> [I2C] Addres set: addr=128
        [I2C] Data sent to master: addr=128, len=16, ovf=0, data=b'ABCDEFGHabcdefgh'

        # Try to read behind the buffer size
        # requested number of bytes is returned, bytes behind the buffer end are filled with 0xFE
        # Overflow is reported by callback function
        # >>> m.readfrom_mem(32, 0xF7, 16)
        b'BUFFEREND\xfe\xfe\xfe\xfe\xfe\xfe\xfe'
        # >>> [I2C] Addres set: addr=247
        [I2C] Data sent to master: addr=247, len=9, ovf=7, data=b'BUFFEREND'

        I2C Low level commands

        The low level I2C commands are provided.
        It is not recommended to use them for comunication with with I2C devices, but they can be useful in some special usage cases.
        They can also be used to demonstrate the I2C protocol for educational purposes.

        All low level commands must be placed between begin and end command.
        The individual comands are not sent to the device imediately, but are rather queued until the end command is executed.

        The low level commands can only be used in master mode.



        """
        pass

    def begin(self, rxbuf_len):
        """
        Initializes the low level queue and prepares for other low level commands.
        If rxbuf_len is > 0, allocates the low lewel commands receive buffer.
        If no read commands are used between begin - end sequence, no read buffer is used and rxbuf_len can be set to 0

        isc.start()

        Queues the I2C start signal.

        isc.stop()

        Queues the I2C stop signal.

        isc.address(addr, mode)

        Queues the I2C device address and transactiom mode (read or write).
        For mode argument use the constants machine.I2C.WRITE (0) or machine.I2C.READ (1)

        isc.write_byte(val)

        Writes a single byte, val, to the queue.

        isc.write_bytes(buf)

        Writes bytes from buffer object buf to the queue.

        isc.read_byte()

        Queue reading single byte from I2C device.

        isc.read_bytes(length)

        Queue reading length bytes from I2C device.

        """
        pass
