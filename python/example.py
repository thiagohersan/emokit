# This is an example of popping a packet from the Emotiv class's packet queue
# and printing the gyro x and y values to the console. 

from emokit.emotiv import Emotiv
import platform
if platform.system() == "Windows":
    import socket  # Needed to prevent gevent crashing on Windows. (surfly / gevent issue #459)
import gevent

if __name__ == "__main__":
    headset = Emotiv(serial_number="SN201405", vendor_id=0x21a1, product_id=0x0001)
    gevent.spawn(headset.setup)
    gevent.sleep(0)
    try:
        while True:
            packet = headset.dequeue()
            print packet.gyro_x, packet.gyro_y
            gevent.sleep(0)
    except KeyboardInterrupt:
        headset.close()
    finally:
        headset.close()
