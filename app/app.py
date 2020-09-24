# -*- coding: utf-8 -*-

import time
import bluetooth
import threading
import smbus
import time
import math

def getAccl(bus, I2C_ADDR):
    data = bus.read_i2c_block_data(I2C_ADDR, 0x00, 7)
    xAccl = (data[1] * 256 + data[2]) / 16
    if xAccl > 2047:
        xAccl -= 4096
    xAccl = float(xAccl)
    xAccl = xAccl / 100
    yAccl = (data[3] * 256 + data[4]) / 16
    if yAccl > 2047:
        yAccl -= 4096
    yAccl = float(yAccl)
    yAccl = yAccl / 100
    zAccl = (data[5] * 256 + data[6]) / 16
    if zAccl > 2047:
        zAccl -= 4096
    zAccl = float(zAccl)
    zAccl = zAccl / 100
    
    Accl = math.sqrt(xAccl ** 2 + yAccl ** 2 + zAccl ** 2) - 9.8
    if Accl < 0:
        return 0
    else:
        return Accl

def setupAccl(IC2_ADDR):
    bus = smbus.SMBus(1)
    bus.write_byte_data(I2C_ADDR, 0x2A, 0x00)
    bus.write_byte_data(I2C_ADDR, 0x2A, 0x01)
    bus.write_byte_data(I2C_ADDR, 0x0E, 0x00)
    time.sleep(0.5)
    return bus

def send_accl(bus, ADDR):
    while client_socket != None:
        accl = getAccl(bus, ADDR)
        client_socket.send('accel_{:.2f}\n'.format(accl))
        print('Accel-> {:.2f}'.format(accl))
        time.sleep(0.5)

if __name__ == '__main__':
    PORT = 1
    I2C_ADDR = 0x1D

    bus = setupAccl(I2C_ADDR)
    server_socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

    print ("Waiting for connect...")

    server_socket.bind(("",PORT ))
    server_socket.listen(1)

    client_socket, address = server_socket.accept()
    print ("Connection has been established.")

    th = threading.Thread(target=send_accl, name="th", args=(bus, I2C_ADDR))
    th.setDaemon(True)
    th.start()

    while 1:
        try:
            data = client_socket.recv(1024)
            print ("Received: [%s]" % data)
        except KeyboardInterrupt:
            print ("Keyboard Interrupt Detected.")
            client_socket.close()
            server_socket.close()
            client_socket = None
            break
        except:
            print ("Disconnected.")
            client_socket.close()
            server_socket.close()
            client_socket = None
            break