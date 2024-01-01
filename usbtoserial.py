import serial
import time

# # Replace 'COMx' with the actual COM port your ESP32 is connected to
# # serial_port = serial.Serial('COM7', 9600, timeout=1)
# # Open the serial port
# serial_port = serial.Serial('COM7', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1)

# # 'N' for no parity, 8 data bits, 1 stop bit is the default configuration

# def send_signal_to_esp32(signal):
#     serial_port.write(signal.encode())

# # Example: Send the signal '1' to ESP32
# send_signal_to_esp32('1')
# time.sleep(1)

# # Close the serial port when done
# serial_port.close()

import serial

# Replace 'COMx' with the actual COM port your ESP32 is connected to
serial_port = serial.Serial('COM7', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1)
def send_signal_to_esp32(signal):
    serial_port.write(signal.encode())
try:
    while True:
        # Read a line of data from the serial port


        # Example: Send the signal '1' to ESP32
        send_signal_to_esp32('1')
        time.sleep(0.5)

        serial_data = serial_port.readline().decode('utf-8').strip()

        # Print the received data
        print(f"---- {serial_data}")

except serial.SerialException as e:
    print(f"Error: {e}")

finally:
    # Close the serial port when done
    serial_port.close()
