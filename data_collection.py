from serial.tools import list_ports
import serial
import time
import csv

# Identify the correct port
ports = list_ports.comports()
for port in ports:
    print(port)

# Open the serial com
serialCom = serial.Serial('COM6', 9600)

# Toggle DTR to reset the Arduino
serialCom.setDTR(False)
time.sleep(1)
serialCom.flushInput()
serialCom.setDTR(True)

# How many data points to record
kmax = 500

# Store data in a list
data = []

# Loop through and collect data as it is available
for k in range(kmax):
    try:
        # Read the line
        s_bytes = serialCom.readline()
        decoded_bytes = s_bytes.decode("utf-8").strip('\r\n')

        # Parse the line
        values = [float(x) for x in decoded_bytes.split()]
        data.append(values)

    except:
        print("Error encountered, line was not recorded.")

# Transpose the data
transposed_data = list(map(list, zip(*data)))

# Create CSV file
csv_file = "disease123.csv"
with open(csv_file, "w", newline='') as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerows(transposed_data)

print("Data collected")
